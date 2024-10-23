import pandas as pd
import os

def time_check(file_path: str) -> pd.Series:
    try:
        # Try reading the CSV file
        df = pd.read_csv(file_path)
        print("File read successfully!")
        
        # Ensure 'startDay', 'startTime', 'endDay', 'endTime' columns exist
        if not {'startDay', 'startTime', 'endDay', 'endTime'}.issubset(df.columns):
            raise ValueError("The CSV file does not contain the required columns.")

        # Create a multi-index on (id, id_2) for the boolean series
        df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
        df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
        
        # Define the full range of 7 days and 24 hours
        full_week_days = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        full_day_time_range = pd.date_range('00:00:00', '23:59:59', freq='S').time
        
        def check_coverage(group):
            # Extract days of the week and the time ranges from the group
            covered_days = set(group['start_timestamp'].dt.day_name())
            
            # Check if all 7 days are covered
            if covered_days != full_week_days:
                return False
            
            # For time range check: Create a full coverage time set
            full_coverage = set()
            for _, row in group.iterrows():
                time_range = pd.date_range(row['start_timestamp'], row['end_timestamp'], freq='S').time
                full_coverage.update(time_range)
            
            # Check if 24-hour period is fully covered
            if set(full_day_time_range) != full_coverage:
                return False
            
            return True

        # Group the data by (id, id_2) and apply the check
        results = df.groupby(['id', 'id_2']).apply(check_coverage)
        
        # Invert the result because we want to know if the timestamps are incorrect (False means incorrect)
        return ~results

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the path and try again.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = "C:/path/to/your/dataset-1.csv"  # Replace with the actual path
incorrect_timestamps = time_check(file_path)
if incorrect_timestamps is not None:
    print(incorrect_timestamps)
