## 3. Process
In the process phase of this case study, we focused on ensuring data integrity, conducting a thorough data cleaning process, and documenting each step to facilitate transparent, reproducible analysis.

### 3.1. Tools and Approach
We used Python and its libraries, specifically Pandas, for data cleaning and manipulation. Python was chosen for its robust data handling capabilities, which allowed for efficient handling of multiple datasets, transforming data, and verifying data integrity.
### 3.2. Steps Taken to Ensure Data Integrity and Cleanliness
The following steps were implemented to prepare the data for analysis.

**Loading and Initial Inspection of the Data**
The data consisted of 18 CSV files, which were inspected individually.
Using pd.read_csv, each dataset was loaded into a Pandas DataFrame for preliminary exploration, including checks for structural consistency across files.

**Removing Duplicates**
We removed any duplicate entries using drop_duplicates(), ensuring that each observation was unique and accurately represented.

**Handling Missing Values**
We assessed missing values across each column using isnull().sum(). This helped identify potential gaps in the data, and if it was necessary removed. The same process for NA values using df = df.dropna()

**Clean and Rename Columns**
All column names were converted to lowercase to maintain a uniform naming convention, making them easier to reference in a case-insensitive environment and improving readability.
By standardizing column names using df.columns = df.columns.str.lower(), we reduced the risk of errors during analysis and ensured a cleaner dataset structure.

**Ensuring Unique Identifiers**
Unique user identifiers were crucial for analyzing trends and user behavior. We verified the uniqueness of IDs with df['Id'].nunique(), ensuring accurate representation of user activities without redundancies.

**Data Type Conversion**
Date and Time Conversion:
Columns representing dates and times, such as ActivityDate and ActivityTime, were converted to appropriate formats for ease of use in temporal analysis.
For ActivityDate, we used pd.to_datetime() to convert the format, handling errors with errors='coerce' to manage inconsistencies.
In the case of ActivityTime, which required a 12-hour AM/PM format, the same function was applied to standardize entries across datasets.

**Rounding Numerical Values**
In datasets containing numerical values with decimal points, specific columns were rounded to two decimal places using round(2). This step was essential to maintain precision while simplifying numerical comparisons.

**Saving Cleaned Datasets**
Each cleaned dataset was saved to a designated directory with a standardized naming convention for organized storage and easier future access. The cleaned files were saved as new CSV files using to_csv(), ensuring no modifications were made to the original data.

### 3.3. Challenges Faced
- Some heart rate data was too granular (minute-level intervals) and needed aggregation to hour-level intervals.
- Data for certain users was incomplete, limiting analysis.
