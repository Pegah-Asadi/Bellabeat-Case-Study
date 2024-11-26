import pandas as pd
import os

# Common cleaning functions
def remove_duplicates(df):
    return df.drop_duplicates()

def check_missing_values(df):
    missing_values = df.isnull().sum()
    print("Missing values in each column:\n", missing_values)
    return missing_values

def standardize_column_names(df):
    df.columns = df.columns.str.lower()
    print("Updated column names:\n", df.columns)
    return df

def count_unique_ids(df, column_name='id'):
    if column_name in df.columns:
        unique_id_count = df[column_name].nunique()
        print(f"Number of unique IDs in column '{column_name}':", unique_id_count)
        return unique_id_count
    else:
        print(f"Column '{column_name}' not found in DataFrame.")
        return None

def convert_to_date(df, column_name, new_column_name=None):
    if column_name in df.columns:
        if new_column_name:
            df[new_column_name] = pd.to_datetime(df[column_name], errors='coerce').dt.date
        else:
            df[column_name] = pd.to_datetime(df[column_name], errors='coerce').dt.date
    return df

def convert_to_time(df, column_name, new_column_name=None, time_format='%I:%M:%S %p'):
    if column_name in df.columns:
        if new_column_name:
            df[new_column_name] = pd.to_datetime(df[column_name], format=time_format, errors='coerce').dt.time
        else:
            df[column_name] = pd.to_datetime(df[column_name], format=time_format, errors='coerce').dt.time
    return df

def split_activity_column(df, column_name):
    """
    Splits the specified column into 'ActivityDate' and 'ActivityTime'.
    Converts the new columns to proper date and time formats.
    """
    if column_name in df.columns:
        df[['ActivityDate', 'ActivityTime']] = df[column_name].str.split(' ', n=1, expand=True)
        df = convert_to_date(df, 'ActivityDate')
        df = convert_to_time(df, 'ActivityTime')
    else:
        print(f"Column '{column_name}' not found in DataFrame.")
    return df

def round_numeric_values(df):
    for column in ['VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance', 'SedentaryActiveDistance', 
                   'TotalDistance', 'TrackerDistance', 'AverageIntensity', 'Calories']:
        if column in df.columns:
            df[column] = df[column].round(2)
    return df

# Define a mapping of datasets to their specific column names
dataset_column_mapping = {
    'hourlyCalories_merged.csv': 'ActivityHour',
    'hourlyIntensities_merged.csv': 'ActivityHour',
    'hourlySteps_merged.csv': 'ActivityHour',
    'minuteCaloriesNarrow_merged.csv': 'ActivityMinute',
    'minuteIntensitiesNarrow_merged.csv': 'ActivityMinute',
    'minuteMETsNarrow_merged.csv': 'ActivityMinute',
    'minuteStepsNarrow_merged.csv': 'ActivityMinute',
    # Add other datasets and their column names here
}

def process_datasets(input_dir, output_dir, dataset_column_mapping):
    """
    Process and clean datasets based on the specified mapping of file names and column names.

    Args:
        input_dir (str): Directory containing input CSV files.
        output_dir (str): Directory to save cleaned CSV files.
        dataset_column_mapping (dict): Mapping of dataset file names to their specific activity columns.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name, column_name in dataset_column_mapping.items():
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, f'cleaned_{file_name}')
        
        try:
            # Load dataset
            print(f"Processing {file_name}...")
            df = pd.read_csv(input_path)
            
            # Apply cleaning steps
            df = remove_duplicates(df)
            check_missing_values(df)
            df = standardize_column_names(df)
            df = split_activity_column(df, column_name)
            df = round_numeric_values(df)

            # Save cleaned dataset
            df.to_csv(output_path, index=False)
            print(f"Cleaned file saved to: {output_path}\n")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    input_dir = '/path/to/input/directory'  # Replace with the actual path to your datasets
    output_dir = '/path/to/output/directory'  # Replace with the actual path to save cleaned datasets
    process_datasets(input_dir, output_dir, dataset_column_mapping)
