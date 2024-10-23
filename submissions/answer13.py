import pandas as pd
import numpy as np
from datetime import time, timedelta

def calculate_time_based_toll_rates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame): DataFrame with toll rates calculated for different vehicles.

    Returns:
        pandas.DataFrame: Updated DataFrame with time-based toll rates.
    """
    # Define the discount factors
    weekday_discount_factors = {
        'morning': 0.8,  # 00:00:00 to 10:00:00
        'day': 1.2,      # 10:00:00 to 18:00:00
        'evening': 0.8   # 18:00:00 to 23:59:59
    }
    weekend_discount_factor = 0.7  # For Saturday and Sunday

    # Define days of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Prepare to store the new data
    expanded_data = []

    # Generate time ranges for each day
    for day in days_of_week:
        for hour in range(24):  # 0 to 23 for hours
            for minute in [0, 30]:  # 0 and 30 minutes
                current_time = time(hour, minute)

                for index, row in df.iterrows():
                    id_start = row['id_start']
                    id_end = row['id_end']
                    distance = row['distance']
                    
                    # Determine discount factor based on day and time
                    if day in ['Saturday', 'Sunday']:
                        discount_factor = weekend_discount_factor
                    else:
                        # Weekday calculations
                        if current_time < time(10, 0):  # 00:00:00 to 10:00:00
                            discount_factor = weekday_discount_factors['morning']
                        elif current_time < time(18, 0):  # 10:00:00 to 18:00:00
                            discount_factor = weekday_discount_factors['day']
                        else:  # 18:00:00 to 23:59:59
                            discount_factor = weekday_discount_factors['evening']

                    # Calculate toll rates for each vehicle type with the discount factor
                    toll_rates = {
                        'moto': row['moto'] * discount_factor,
                        'car': row['car'] * discount_factor,
                        'rv': row['rv'] * discount_factor,
                        'bus': row['bus'] * discount_factor,
                        'truck': row['truck'] * discount_factor
                    }

                    # Append data including start and end day/time
                    expanded_data.append({
                        'id_start': id_start,
                        'id_end': id_end,
                        'distance': distance,
                        'start_day': day,
                        'start_time': current_time,
                        'end_day': day,
                        'end_time': current_time,
                        **toll_rates  # Unpack toll rates
                    })

    # Create a new DataFrame from the expanded data
    result_df = pd.DataFrame(expanded_data)
    
    return result_df

# Example usage
# Sample toll rates DataFrame with previously calculated toll rates
data = {
    'id_start': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
    'id_end': ['B', 'C', 'A', 'C', 'A', 'D', 'B', 'C'],
    'distance': [5, 15, 5, 10, 15, 20, 25, 20],
    'moto': [4.0, 12.0, 4.0, 8.0, 12.0, 16.0, 20.0, 16.0],
    'car': [6.0, 18.0, 6.0, 12.0, 18.0, 24.0, 30.0, 24.0],
    'rv': [7.5, 22.5, 7.5, 15.0, 22.5, 30.0, 37.5, 30.0],
    'bus': [10.0, 33.0, 10.0, 22.0, 33.0, 44.0, 55.0, 44.0],
    'truck': [18.0, 54.0, 18.0, 36.0, 54.0, 72.0, 90.0, 72.0]
}
toll_rates_df = pd.DataFrame(data)

# Calculate time-based toll rates
time_based_toll_rates_df = calculate_time_based_toll_rates(toll_rates_df)
print(time_based_toll_rates_df)
