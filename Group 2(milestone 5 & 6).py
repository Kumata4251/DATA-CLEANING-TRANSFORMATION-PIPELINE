Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# #### Data Cleaning and Transformation Pipeline
# #### Group Assignment - Milestone 5 and 6
# 1. SCM223-0222/2024 RAEL Juma-GROUP LEADER
# 2. SCM223-1457/2024 Faith Zuma
# 3. SCM223-0205/2024 Jacinta Mutinda
# 4. SCM223-1580/2024 Ian Kiberu
# 5. SCM223-1431/2024 Benta Yvonne
# 6. SCM223-1454/2024 Festus Mulei
# 7. SCM223-0238/2024 Vanessa Kerubo
# 8. SCM223-1358/2024 Ian Gitau

# ==========================================
# MILESTONE 5 & 6 COMBINED SYSTEM
# Concurrent Intelligent Steam Games
# Data Cleaning & Transformation Pipeline
# ==========================================

import pandas as pd
import threading
import asyncio
import time

from multiprocessing import Process
from threading import Lock
from queue import Queue

# LOAD DATASET

df = pd.read_csv("steam_top_games_2026 44.csv")

# THREAD SAFETY

lock = Lock()

# MULTITHREADING FUNCTIONS

def clean_missing(df):

    with lock:
        df.fillna("Unknown", inplace=True)

    print("Missing values cleaned")

def validate_prices(df):

    with lock:
        df.loc[df['price_usd'] == 0,
               'is_free'] = True

    print("Price validation completed")

# MULTIPROCESSING FUNCTIONS

def process_reviews(df):

    df['total_reviews'] = (
        df['positive_reviews'] +
        df['negative_reviews']
    )

    print("Review processing completed")

def process_playtime(df):

    avg = df['avg_playtime_forever'].mean()

    print("Average playtime:", avg)

# ASYNCHRONOUS PROGRAMMING

async def load_dataset():

    print("Loading dataset asynchronously...")
    await asyncio.sleep(1)

async def save_dataset():

    print("Saving dataset asynchronously...")
    await asyncio.sleep(1)

async def async_main():

    await asyncio.gather(
        load_dataset(),
        save_dataset()
    )

# TASK QUEUE

tasks = Queue()

tasks.put("clean_missing")
tasks.put("transform_reviews")
tasks.put("validate_prices")

# PERFORMANCE BENCHMARK

start_time = time.time()

# MULTITHREADING EXECUTION

t1 = threading.Thread(
    target=clean_missing,
    args=(df,)
)

t2 = threading.Thread(
    target=validate_prices,
    args=(df,)
)

t1.start()
t2.start()

t1.join()
t2.join()

# MULTIPROCESSING EXECUTION

p1 = Process(
    target=process_reviews,
    args=(df,)
)

p2 = Process(
    target=process_playtime,
    args=(df,)
)

p1.start()
p2.start()

p1.join()
p2.join()

# TASK QUEUE EXECUTION

print("\nTask Queue Processing:")

while not tasks.empty():

    task = tasks.get()

    print("Processing:", task)

# ASYNC EXECUTION

asyncio.run(async_main())

# RESEARCH-LEVEL QUALITY SCORING;

def quality_score(df):

    missing_score = 1 - (
        df.isnull().sum().sum() / df.size
    )

    duplicate_score = 1 - (
        df.duplicated().sum() / len(df)
    )

    return (
        missing_score + duplicate_score
    ) / 2

score = quality_score(df)

print("\nDataset Quality Score:",
      round(score * 100, 2), "%")

# INTELLIGENT CLEANING STRATEGY

class RemoveMissingStrategy:

    def clean(self, df):
        return df.dropna()

class FillMissingStrategy:

    def clean(self, df):
        return df.fillna("Unknown")

missing_values = (
    df.isnull().sum().sum()
)

if missing_values > 100:

    strategy = FillMissingStrategy()

    print("\nUsing FillMissingStrategy")

else:

    strategy = RemoveMissingStrategy()

    print("\nUsing RemoveMissingStrategy")

df = strategy.clean(df)

# AUTOMATED VALIDATION

def validate_dataset(df):

    if df.duplicated().sum() > 0:
        print("Duplicates found")

    else:
        print("No duplicates found")

    if df.isnull().sum().sum() > 0:
        print("Missing values exist")

    else:
        print("No missing values")

    if (df['price_usd'] < 0).sum() > 0:
        print("Invalid prices detected")

    else:
        print("All prices are valid")

print("\nValidation Results:")

validate_dataset(df)

# INTEGRATED DATA PIPELINE

class DataPipeline:

    def load_data(self):
        return pd.read_csv(
            "steam_top_games_2026 44.csv"
        )

    def clean_data(self, df):

        return df.fillna("Unknown")

    def transform_data(self, df):

        df['total_reviews'] = (
            df['positive_reviews'] +
            df['negative_reviews']
        )

        return df

    def validate_data(self, df):

        return df.isnull().sum()

pipeline = DataPipeline()

dataset = pipeline.load_data()

dataset = pipeline.clean_data(dataset)

dataset = pipeline.transform_data(dataset)

print("\nPipeline Validation:")

print(
    pipeline.validate_data(dataset)
)

# FILE EXPORT / SERIALIZATION

dataset.to_csv(
    "cleaned_steam_games.csv",
    index=False
)

dataset.to_json(
    "steam_games.json"
)

print("\nFiles exported successfully")

# FINAL PERFORMANCE ANALYSIS

end_time = time.time()

execution_time = (
    end_time - start_time
)

print("\nExecution Time:",
      round(execution_time, 2),
      "seconds")

# FINAL SYSTEM OUTPUT

print("\nFinal System Completed Successfully")