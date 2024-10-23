import pandas as pd
import numpy as np  # Importing NumPy

def unroll_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame): Distance matrix DataFrame

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Create an empty list to collect the unrolled data
    unrolled_data = []

    # Get the index (IDs) of the DataFrame
    ids = df.index.tolist()
    
    # Iterate over the distance matrix
    for i in ids:
        for j in ids:
            if i != j:  # Skip same id_start and id_end
                distance = df.at[i, j]
                if pd.notna(distance):  # Only include valid distances
                    unrolled_data.append({'id_start': i, 'id_end': j, 'distance': distance})

    # Create a DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data)
    
    return unrolled_df

# Example usage
# Sample distance matrix DataFrame
distance_matrix = pd.DataFrame({
    'A': [0, 5, 15, np.nan],
    'B': [5, 0, 10, 25],
    'C': [15, 10, 0, 20],
    'D': [np.nan, 25, 20, 0]
}, index=['A', 'B', 'C', 'D'])

# Unroll the distance matrix
unrolled_df = unroll_distance_matrix(distance_matrix)
print(unrolled_df)