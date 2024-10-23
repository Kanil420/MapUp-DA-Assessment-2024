import pandas as pd

def calculate_toll_rate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame with columns ['id_start', 'id_end', 'distance']

    Returns:
        pandas.DataFrame: Updated DataFrame with toll rates for different vehicle types.
    """
    # Define rate coefficients for each vehicle type
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    # Calculate toll rates by multiplying distances with the rate coefficients
    for vehicle, rate in rate_coefficients.items():
        df[vehicle] = df['distance'] * rate

    return df

# Example usage
# Sample unrolled DataFrame
data = {
    'id_start': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
    'id_end': ['B', 'C', 'A', 'C', 'A', 'D', 'B', 'C'],
    'distance': [5, 15, 5, 10, 15, 20, 25, 20]
}
unrolled_df = pd.DataFrame(data)

# Calculate toll rates
toll_rates_df = calculate_toll_rate(unrolled_df)
print(toll_rates_df)
