## 4. Analyze

### Steps Taken
1. **Import Necessary Libraries**
First, import the essential Python libraries (Pandas, Numpy, Seaborn, Matplotlib Pyplot) for data manipulation and visualization.
2. **Load the Datasets**
Read the datasets into pandas DataFrames using pd.read_csv().
3. **Combine Datasets**
Our data is split into two groups:
Group 1: Contains records from the time period March 12, 2016 (03.12.2016) to April 11, 2016 (04.11.2016).
Group 2: Contains records from the time period April 12, 2016 (04.12.2016) to May 12, 2016 (05.12.2016).
Each group represents a different chunk of the overall dataset for the two months. However, to perform a comprehensive analysis covering the entire two-month period, we need to combine these datasets into a single DataFrame. This allows us to work with all the data at once without needing to repeatedly analyze each group separately.
To combine these two datasets for each type of data (e.g., daily activity, hourly calories), we used **pd.concat()**, a function provided by pandas. 
Here's why:
pd.concat() merges multiple DataFrames either row-wise or column-wise. In our case, we combine them row-wise (axis=0) to stack the data from Group 2 below Group 1.
This operation maintains the structure of the datasets, ensuring that all rows and columns are retained.
4. **Explore the Data**
- *Descriptive Statistics*: Use dataset_name.head() to view the first few rows, dataset_name.info() to check the structure, and dataset_name.describe() for a statistical summary of the dataset.
5. **Merge Datasets if Necessary**
To analyze data across different time granularities, combine datasets using a common key:
*Merge datasets on a common identifier*
merged_data = pd.merge(dataset1, dataset2, on='common_key')

*Merge datasets on multiple keys (e.g., ID and date)*
merged_data = pd.merge(dataset1, dataset2, on=['common_key', 'date_key'])
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
- Identified activity variances based on demographic or usage factors, such as weekday routines versus weekend relaxation.

9. **Findings Extraction**
- Extracted key patterns, such as high activity levels on Saturdays and calorie burn peaking in the late afternoon.
- Highlighted user groups (e.g., sedentary users) with potential for increased engagement through targeted campaigns.
- Emphasized opportunities to encourage consistent sleep patterns during weekdays and promote light activities on Sundays.


