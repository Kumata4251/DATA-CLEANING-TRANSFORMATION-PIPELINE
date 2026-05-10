# key excerpt
import csv
from abc import ABC, abstractmethod

class SteamGame:
    def __init__(self, raw_dict):
        self.raw = raw_dict
        self.cleaned = {}

class BasicCleaner:
    def clean_record(self, game):
        c = {}
        c['price_usd'] = float(game.raw['price_usd']) if game.raw['price_usd'] else 0.0
        c['is_free'] = game.raw['is_free'] == "TRUE"
        c['developer'] = game.raw['developer'] or "Unknown"
        game.cleaned = c

class CleanerBase:
    def clean(self, record): raise NotImplementedError

class PriceCleaner(CleanerBase):
    def clean(self, record):
        price = float(record.raw.get('price_usd') or 0)
        record.cleaned['price_usd'] = 0.0 if record.raw.get('is_free')=='TRUE' else price

class CleaningOrchestrator:
    def __init__(self, cleaners):
        self.cleaners = cleaners

    def process(self, record):
        for cleaner in self.cleaners:
            cleaner.clean(record)
        if record.cleaned['price_usd'] > 60:
            record.cleaned['price_tier'] = 'premium'

class Record:
    def __init__(self, raw_dict):
        self.raw = raw_dict
        self.cleaned = {}

def make_cleaner(func):
    return func

@make_cleaner
def clean_genres(rec):
    rec.cleaned['genres'] = [g.strip() for g in rec.raw['genres'].split(',')]

def clean_numeric(rec):
    rec.cleaned['price_usd'] = float(rec.raw.get('price_usd') or 0)
    rec.cleaned['is_free'] = rec.raw.get('is_free') == 'TRUE'

def clean_platforms(rec):
    rec.cleaned['platforms'] = [p.strip() for p in rec.raw['platforms'].split(',')]

class FunctionalPipeline:
    def __init__(self, cleaners):
        self.cleaners = cleaners

    def process(self, record):
        for cleaner in self.cleaners:
            cleaner(record)

def read_stream(path):
    for row in csv.DictReader(open(path)):
        yield Record(row)

pipe = FunctionalPipeline([clean_numeric, clean_genres, clean_platforms])

class DataValidationError(Exception): pass

class CleaningStrategy(ABC):
    @abstractmethod
    def apply(self, record): pass

class RobustPipeline:
    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.errors = []

    def notify(self, status, name):
        print(f"{status}: {name}")

    def run(self, records):
        for i, rec in enumerate(records):
            try:
                self.pipeline.process(rec)
                self.notify("CLEANED", rec.raw.get('name', 'Unknown'))
            except DataValidationError as e:
                self.errors.append((i, str(e)))          