import pandas as pd
import numpy as np

def calculate_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame): DataFrame with columns ['From', 'To', 'Distance']

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Create a unique set of IDs
    ids = pd.unique(df[['From', 'To']].values.ravel('K'))
    
    # Initialize the distance matrix with NaN values
    distance_matrix = pd.DataFrame(np.nan, index=ids, columns=ids)
    
    # Fill the distance matrix with known distances
    for _, row in df.iterrows():
        from_id = row['From']
        to_id = row['To']
        distance = row['Distance']
        
        # Set the distance in both directions
        distance_matrix.at[from_id, to_id] = distance
        distance_matrix.at[to_id, from_id] = distance  # For symmetry

    # Fill the diagonal with zeros
    np.fill_diagonal(distance_matrix.values, 0)
    
    # Use a loop to calculate cumulative distances (Floyd-Warshall algorithm)
    for k in ids:
        for i in ids:
            for j in ids:
                if pd.notna(distance_matrix.at[i, k]) and pd.notna(distance_matrix.at[k, j]):
                    new_distance = distance_matrix.at[i, k] + distance_matrix.at[k, j]
                    if pd.isna(distance_matrix.at[i, j]) or new_distance < distance_matrix.at[i, j]:
                        distance_matrix.at[i, j] = new_distance

    return distance_matrix

# Example usage
# Create a sample DataFrame
data = {
    'From': ['A', 'B', 'A', 'C', 'B'],
    'To': ['B', 'C', 'C', 'D', 'D'],
    'Distance': [5, 10, 15, 20, 25]
}
sample_df = pd.DataFrame(data)

# Calculate the distance matrix
distance_matrix_df = calculate_distance_matrix(sample_df)
print(distance_matrix_df)
