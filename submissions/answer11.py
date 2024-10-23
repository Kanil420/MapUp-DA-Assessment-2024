import pandas as pd
import numpy as np

def find_ids_within_ten_percentage_threshold(df: pd.DataFrame, reference_id: str) -> pd.DataFrame:
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame): DataFrame with columns ['id_start', 'id_end', 'distance']
        reference_id (str): The ID for which to find nearby IDs based on distance threshold.

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Calculate average distance for the reference_id
    reference_distances = df[df['id_start'] == reference_id]['distance']
    
    if reference_distances.empty:
        return pd.DataFrame()  # Return empty DataFrame if no distances found

    average_distance = reference_distances.mean()

    # Calculate the threshold
    lower_bound = average_distance * 0.9
    upper_bound = average_distance * 1.1

    # Calculate average distances for all IDs in id_start
    average_distances = df.groupby('id_start')['distance'].mean()

    # Find IDs within the threshold
    within_threshold = average_distances[
        (average_distances >= lower_bound) & (average_distances <= upper_bound)
    ].index.tolist()

    # Convert to DataFrame and sort
    result_df = pd.DataFrame(within_threshold, columns=['id_start']).sort_values(by='id_start')
    
    return result_df

# Example usage
# Sample unrolled DataFrame
data = {
    'id_start': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
    'id_end': ['B', 'C', 'A', 'C', 'A', 'D', 'B', 'C'],
    'distance': [5, 15, 5, 10, 15, 20, 25, 20]
}
unrolled_df = pd.DataFrame(data)

# Find IDs within 10% threshold of reference ID 'A'
result_df = find_ids_within_ten_percentage_threshold(unrolled_df, 'A')
print(result_df)
