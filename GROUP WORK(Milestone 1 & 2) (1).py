#!/usr/bin/env python
# coding: utf-8

# #### Data Cleaning and Transformation Pipeline
# #### Group Assignment - Milestone 1
# 1. SCM223-0222/2024 RAEL Juma-GROUP LEADER
# 2. SCM223-1457/2024 Faith Zuma
# 3. SCM223-0205/2024 Jacinta Mutinda
# 4. SCM223-1580/2024 Ian Kiberu
# 5. SCM223-1431/2024 Benta Yvonne
# 6. SCM223-1454/2024 Festus Mulei
# 7. SCM223-0238/2024 Vanessa Kerubo
# 8. SCM223-1358/2024 Ian Gitau
# Objective:
# Build an object-oriented prototype that:
# - Loads raw data
# - Cleans data
# - Transforms data
# - Produces cleaned output

# In conclusion, our prototype demonstrates how a data cleaning and transformation
# pipeline can be modeled using OOP principles. It forms a foundation for future milestones
# involving inheritance, advanced structures and scalability

# #### SAMPLE RAW DATASET
# #### We create a messy dataset with:
# #### - duplicates
# #### - missing values
# #### - inconsistent name formatting
# #### - salaries stored as text
# 

# In[10]:


raw_data = [
    {"Name":"john", "Age":None, "Salary":"50000"},
    {"Name":"john", "Age":None, "Salary":"50000"},
    {"Name":"MARY", "Age":30, "Salary":"60000"},
    {"Name":"peter", "Age":25, "Salary":"70000"},
    {"Name":"ann", "Age":None, "Salary":"45000"}
]

print("RAW DATASET")
for row in raw_data:
    print(row)


# ## DATASET CLASS
# ## stores dataset and displays it

# In[11]:


class Dataset:
    # constructor
    def __init__(self, name, records):
        self.dataset_name = name
        self.records = records

    # display records
    def display_data(self):
        print("\nDataset:", self.dataset_name)
        for record in self.records:
            print(record)


# ### CLASS FOR CLEANING DATA

# In[12]:


class DataCleaner:

    # remove duplicate records
    def remove_duplicates(self, data):

        unique_records=[]
        seen=[]

        for row in data:
            if row not in seen:
                unique_records.append(row)
                seen.append(row)

        return unique_records


    # replace missing ages
    def fill_missing_values(self, data):

        for row in data:
            if row["Age"] is None:
                row["Age"] = 28

        return data


# #### TRANSFORMATION CLASS:standardizes and converts cleaned data into a consistent structure suitable for analysis.

# In[13]:


class DataTransformer:

    # standardize names
    def standardize_names(self, data):

        for row in data:
            row["Name"] = row["Name"].title()

        return data


    # convert salary from text to float
    def convert_salary(self,data):

        for row in data:
            row["Salary"] = float(row["Salary"])

        return data


# #### PIPELINE MANAGER: basically a controller that organizes and runs a series of steps (a “pipeline”) on your data in a fixed order.
# - It manages a workflow such as:
# - Receive raw data (dataset)
# - Clean the data (handled by DataCleaner)
# - Transform the data (handled by DataTransformer)
# - Return final processed data

# In[14]:


class PipelineManager:

    def __init__(self, dataset):

        self.dataset = dataset
        self.cleaner = DataCleaner()
        self.transformer = DataTransformer()


    def run_pipeline(self):

        print("\nSTEP 1: ORIGINAL DATA")
        self.dataset.display_data()

        # get records
        data=self.dataset.records


        # Cleaning stage
        print("\nSTEP 2: Removing duplicates...")
        data=self.cleaner.remove_duplicates(data)


        print("Filling missing values...")
        data=self.cleaner.fill_missing_values(data)


        # Transformation stage
        print("Standardizing names...")
        data=self.transformer.standardize_names(data)


        print("Converting salary data type...")
        data=self.transformer.convert_salary(data)


        # Final output
        print("\nSTEP 3: CLEANED DATA")
        for row in data:
            print(row)

        return data


# In[15]:


# Create dataset object
employee_data = Dataset("Employee Dataset", raw_data)

# Create pipeline object
pipeline = PipelineManager(employee_data)

# Run pipeline and store cleaned data
cleaned_data = pipeline.run_pipeline()


# In[16]:


print("\nPIPELINE REPORT")
print("Records after cleaning:", len(cleaned_data))

for row in cleaned_data:
    print(row)


# We used Object-Oriented Programming by creating four classes:
# Dataset class for storing raw data.
# DataCleaner class for cleaning tasks.
# DataTransformer class for transformations.
# PipelineManager class to coordinate the full pipeline.
# This is our raw dataset with duplicates, missing values and inconsistent capitalization.
# Next, these classes perform cleaning and transformation. The PipelineManager runs all
# stages in sequence.
# From the output we can see: duplicate records were removed, missing ages were filled,
# names were standardized, salaries were converted from strings to numeric values. This
# produces cleaned data ready for analysis.
# We applied: Encapsulation: Each class contains related data and methods. Abstraction:
# Users only run the pipeline while internal processing happens automatically.

# In[ ]:




