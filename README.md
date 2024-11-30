# 🌟 Bellabeat-Case-Study
📊 Analyzing fitness data to provide actionable insights for Bellabeat

## Summary
This case study analyzes smart device fitness data to uncover trends and provide actionable insights for Bellabeat, a high-tech wellness company. The goal was to guide Bellabeat's marketing strategy by understanding consumer behavior and identifying growth opportunities for its products.

## 🎯 Objectives
1. **Analyze** user behavior trends in smart device usage.
2. **Recommend** actionable marketing strategies.
3. **Enhance** a specific Bellabeat product with data insights.
4. **Showcase** data analysis and visualization expertise.

## 📂 Repository Structure
| Section      | Description                                                                |
|--------------|----------------------------------------------------------------------------|
| **Process**  | Steps for data cleaning and analysis.                                      |
| **Analysis** | Python scripts, notebooks, charts, and insights from the analysis.         |
| **Data**     | Links to external datasets.                                                |


## 🔍 Key Findings
1. **Positive Correlation Between Steps and Calories:** More steps lead to higher calorie burn.
2. **Peak Activity Hours:** Late afternoon (5–7 PM) sees maximum calorie burn.
3. **User Segmentation:** Many users are sedentary or lightly active, offering growth potential.
4. **Activity Distribution:** Light activities dominate, with minimal moderate/intense activity.
5. **Weekend Trends:** Saturdays are most active; Sundays show notable inactivity.
6. **Weekday Sleep Deficit:** Weekday sleep averages below 8 hours; weekends exceed this.

## ✅ Recommendations
1. **Target Low-Activity Users:** Launch motivational campaigns with rewards.
2. **Leverage Peak Hours:** Send notifications during 5–7 PM.
3. **Promote Sunday Activity:** Encourage light exercises to reduce inactivity.
4. **Incentivize Sleep:** Introduce rewards for consistent weekday sleep habits.
5. **Personalized Insights:** Highlight activity trends for better user engagement.
6. **Gamification Features:** Add challenges and badges to increase engagement.


## 1. Ask
### Business Task:
- Identify key usage trends in non-Bellabeat smart device data to understand customer needs.
- Analyze behavioral differences between Bellabeat and non-Bellabeat users, highlighting gaps and opportunities.
- Develop data-driven insights to position Bellabeat’s competitive advantages.
- Guide targeted campaigns to drive user acquisition and engagement

## 2. Prepare
### 2.1. Data Source
**Dataset:** FitBit Fitness Tracker Data
**Source:** Kaggle, provided by Mobius.
**Format:** 17 .csv files, public domain, gathered via Amazon Mechanical Turk.
**Data Period: March–May 2016.

### 2.2. Assessing Data Credibility (ROCC Framework)

| Aspect            | Assessment                            |
|-------------------|---------------------------------------|
| **Reliable**      | Low (small sample size, bias)         |
| **Original**      | High (direct from Fitbit)             |
| **Comprehensive** | Moderate (granular but short-term)    |
| **Current**       | Low (dated from 2016)                 |
| **Cited**         | Moderate (attributed to Mobius)       |


## 3. Process
The full Python script for data cleaning is available in the [process](https://github.com/Pegah-Asadi/Bellabeat-Case-Study/blob/main/process/data_cleaning.py) folder.

Python was chosen for its robust data handling capabilities, enabling efficient processing and transformation of large datasets.

### 3.1. Tools and Approach
- **Programming Language:** Python
- **Libraries Used:**
    - **Pandas:** For data manipulation and cleaning.
    - **Numpy:** For numerical operations.
    - **Matplotlib/Seaborn:** For exploratory visualizations.

### 3.2. Steps for Data Cleaning
The data cleaning process involved the following steps:

**1. Loading and Inspecting the Data**
- **Action:** Loaded 17 CSV files using pd.read_csv().
- **Purpose:** Checked for structural consistency across datasets with:

   `df.info()`

  `df.describe()`

**2. Removing Duplicates**
- **Action:** Used drop_duplicates() to eliminate duplicate entries:

  `df = df.drop_duplicates()`

**3. Handling Missing Values**
- **Action:** Identified missing values:

  `missing_values = df.isnull().sum()`

  Removed rows with missing values if deemed non-critical:

  `df = df.dropna()`

- **Purpose:** Addressed gaps to improve data reliability.

**4. Standardizing Column Names**
- **Action:** Converted all column names to lowercase for consistency:

  `df.columns = df.columns.str.lower()`

- **Purpose:** Simplified column referencing and ensured uniformity.

**5. Verifying Unique Identifiers**
- **Action:** Checked the uniqueness of user IDs:

  `unique_ids = df['id'].nunique()`

- **Purpose:** Confirmed accurate user representation without redundancies.

**6. Converting Data Types**
- **Action:**
Converted dates using pd.to_datetime():

  `df['date'] = pd.to_datetime(df['date'], errors='coerce')`
Standardized time formats for temporal analysis.

- **Purpose:** Enabled efficient date/time-based operations.

**7. Rounding Numerical Values**
- **Action:** Rounded numerical columns to two decimal places:

  `df['column_name'] = df['column_name'].round(2)`

- **Purpose:** Simplified comparisons without sacrificing precision.

**8. Saving Cleaned Datasets**
- **Action:** Saved cleaned datasets with descriptive names:

  `df.to_csv('cleaned_data.csv', index=False)`

- **Purpose:** Ensured reproducibility and retained original raw files.

### 3.3. Challenges
- Granularity of Heart Rate Data: Minute-level intervals required aggregation to hourly intervals.
- Incomplete Data: Missing records for certain users limited some analyses.


## 4. Analyze
In this phase, I performed detailed data exploration and analysis to uncover insights and trends. Below are the steps and technical details of the analysis process.

### 4.1 Steps Taken
1. **Import Necessary Libraries**

I started by importing essential Python libraries for data manipulation, analysis, and visualization:
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
```

2. **Load the Datasets**

The datasets were loaded into Pandas DataFrames using pd.read_csv() for efficient handling of tabular data:
```python
# Load datasets
df1 = pd.read_csv('DailyActivity.csv')
df2 = pd.read_csv('HourlyCalories.csv')
```
3. **Combine Datasets**

The data was split into two groups:

Group 1: Records from March 12, 2016, to April 11, 2016.

Group 2: Records from April 12, 2016, to May 12, 2016.

I used `pd.concat()` to combine these datasets into a single DataFrame for comprehensive analysis:
```python
# Combine datasets row-wise
combined_df = pd.concat([df1, df2], axis=0, ignore_index=True)
```
- Key considerations:

  - Row-wise Concatenation (axis=0): Stacked Group 2 below Group 1.
  - Ignore Index: Ensured seamless row numbering in the combined dataset.

4. **Explore the Data**

Basic data exploration helped me understand the dataset structure and identify anomalies:
```python
# View basic structure
combined_df.info()

# Statistical summary
combined_df.describe()

# Preview the first few rows
combined_df.head()
```
This provided insights into column types, missing values, and descriptive statistics.

5. **Merge Datasets (if Necessary)**

For advanced analysis across multiple time granularities, I merged datasets using common keys like ID and Date:
```python
# Merge on a single key
merged_data = pd.merge(dataset1, dataset2, on='common_key')

# Merge on multiple keys
merged_data = pd.merge(dataset1, dataset2, on=['id', 'date'])
```

6. **Exploratory Data Analysis (EDA)**
- Investigated the relationship between total steps and calories burned, revealing a positive correlation.
- Analyzed hourly activity and calorie burn patterns to identify peak activity times (late afternoon to early evening).
- Segmented users based on activity levels and categorized them as sedentary, lightly active, fairly active, or very active.

7. **Visualization**
- Generated scatter plots to visualize relationships between activity intensity and calorie burn.
- Created bar charts to display average activity levels and calories burned by hour, day type (weekday vs. weekend), and user category.
- Illustrated sleep trends across weekdays and weekends, highlighting consistency gaps.

8. **Statistical Analysis**
- Computed averages, standard deviations, and activity level distributions to understand user behavior.
- Assessed user engagement trends by correlating daily steps with calories burned over time.
- Identified activity variances based on usage factors, such as weekday routines versus weekend relaxation.

9. **Findings Extraction**
- Extracted key patterns, such as high activity levels on Saturdays and calorie burn peaking in the late afternoon.
- Highlighted user groups (e.g., sedentary users) with potential for increased engagement through targeted campaigns.
- Emphasized opportunities to encourage consistent sleep patterns during weekdays and promote light activities on Sundays.

## 5. Share

You can find the visualizations of the analysis phase with the related Python codes and insights in analysis folder, [Analysis.ipynb file](https://github.com/Pegah-Asadi/Bellabeat-Case-Study/blob/main/analysis/Analysis.ipynb).

### Insights:
- **Positive Correlation Between Steps and Calories:**

Increased steps directly lead to higher calorie expenditure, emphasizing the importance of promoting physical activity.

- **Peak Activity and Calorie Burn Hours:**

Activity levels and calorie burn peak between 10:00 AM and 7:00 PM, particularly in the late afternoon (5:00–7:00 PM), aligning with typical daily routines.

- **Weekday vs. Weekend Patterns:**

Saturday is the most active day, driven by leisure or recreational activities, while Sunday shows a significant dip in activity. Weekday activity is consistent but lower, influenced by workday routines.

- **Sleep Patterns:**

Weekday sleep consistently falls below the recommended 8 hours, while weekend sleep exceeds it, suggesting recovery from the workweek.

- **User Segmentation:**

37% of users are sedentary (<5000 steps/day), highlighting a significant segment for targeted engagement. Only 20% of users are highly active, indicating room for growth in active user numbers.

- **User Retention:**

60% of users are high-use (engaging with the app for over 40 days), demonstrating strong retention, but moderate-use users (34.3%) offer an opportunity for improvement.

- **Variance in Calories Burned:**

Differences in calorie burn for similar activity levels suggest personalization opportunities based on user characteristics like age or metabolism.

## 6. Act

**Recommendations for Marketing and Product Teams**

### 6.1 Marketing Strategies
- **Target Sedentary and Lightly Active Users:**
  - Design motivational campaigns to encourage movement, such as daily step challenges, gamified rewards, and group activities.
  - Use personalized messages emphasizing the link between activity levels and calorie burn for health benefits.

- **Capitalize on Peak Hours:**
  - Launch in-app notifications or reminders for workouts during peak activity hours (late afternoon).
  - Promote "power hour" challenges to maximize calorie burn during high-activity periods.

- **Leverage Weekend Activity Patterns:**
  - Focus on Saturday campaigns promoting outdoor or recreational activities.
  - Encourage light activity on Sundays to reduce the steep drop in engagement.

- **Highlight Sleep Health:**
  - Introduce campaigns or content to educate users on the importance of consistent sleep routines.
  - Use sleep tracking insights to offer tailored tips or bedtime reminders.


### 6.2 Product Development
- **Enhance Personalization:**
  - Incorporate adaptive goals based on individual calorie burn variance, such as tailoring step targets or workout intensity recommendations.
  - Use user segmentation data to suggest personalized activity plans.

- **Improve Engagement Features:**
  - Add gamification elements like badges for consecutive active days or sleep consistency.
  - Provide insights through dynamic charts that showcase progress in steps, calories burned, and sleep patterns.

- **Support Weekday Activity:**
  - Develop quick, work-friendly exercises or productivity tips to maintain consistent activity during weekdays.
  - Include reminders for movement during work hours to combat sedentary behavior.

- **Focus on Retention:**
  - Convert moderate-use users into high-use by sending re-engagement notifications or offering exclusive content for consistent app usage.
  - Provide milestone-based incentives for users maintaining high engagement.