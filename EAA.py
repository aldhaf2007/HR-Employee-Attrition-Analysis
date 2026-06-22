#!/usr/bin/env python
# coding: utf-8
##Environment Setup & Data Loading
import pandas as pd
import matplotlib.pyplot as plt

# Import your custom plotting functions from plots.py
import plots

# Load the source dataset
emp = pd.read_csv("Employee.csv")


##Data Schema Transformation (Renaming)

# Rename long or messy columns for easier access
emp.rename(
    columns={
        "ExperienceInCurrentDomain": "Years_of_Experience",
        "LeaveOrNot": "Attrition_Status",
    },
    inplace=True,
)

# Standardize: Strip any unexpected spaces from headers and replace with underscores
emp.columns = emp.columns.str.replace(" ", "_")


##Data Cleaning & Quality Assessment

# 1. Missing Data Handling
#print("--- Missing Values Count ---")
print(emp.isnull().sum())
emp.dropna(inplace=True)  # Removes rows containing missing fields safely

# 2. Duplicate Removal
#print(f"\nTotal Duplicated Rows Found: {emp.duplicated().sum()}")
emp.drop_duplicates(inplace=True)  # Drops identical row copies


# 3. Categorical Values Standardization
#print("\nUnique Cities Before Strip:", emp["City"].unique())
#print("Unique Genders:", emp["Gender"].unique())
emp["City"] = emp["City"].str.strip()  # Fixes hidden trailing/leading spaces


# 4. Outlier Analysis & Descriptive Statistics
#print("\n--- Structural Summary Statistics ---")
#print(emp.describe())


##Statistical Aggregation (GroupBy Analysis)

print("\n================ STATISTICAL INSIGHTS ================")

# 1. Regional Breakdown: Highest attrition risk down to lowest
city_summary = emp.groupby("City")["Attrition_Status"].mean().reset_index()
city_summary = city_summary.sort_values(by="Attrition_Status", ascending=False)
print("\n--- Attrition Rate by City Location ---")
print(city_summary)

# 2. Demographic Intersection: Attrition trends across Salary and Gender combined
gender_tier_summary = (
    emp.groupby(["PaymentTier", "Gender"])["Attrition_Status"].mean().reset_index()
)
print("\n--- Attrition by Payment Tier and Gender Intersection ---")
print(gender_tier_summary)

# 3. Time-Series Analysis: Retention performance by annual employee intake cohorts
year_details = (
    emp.groupby("JoiningYear")["Attrition_Status"].agg(["mean", "count"]).reset_index()
)
print("\n--- Attrition Mean & Intake Size per Joining Year ---")
print(year_details)

# 4. Total Baseline: Overall global company attrition breakdown
print("\n--- Overall Company Attrition Distribution (%) ---")
overall = emp["Attrition_Status"].value_counts(normalize=True) * 100
print(overall)

# CALLING THE SEPARATE CHART FUNCTIONS ---
print("\nGenerating charts via plots module...")
plots.plot_city_attrition(city_summary)
plots.plot_intersection_attrition(gender_tier_summary)
plots.plot_year_attrition(year_details)
plots.plot_overall_distribution(overall)

print("All charts generated!")
# --- THE COHESIVE ANCHOR ---
plt.show()  # This empty blocking show keeps ALL currently open windows active on your desktop!
