import pandas as pd
import polyline
from geopy.distance import geodesic

def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
    # Step 1: Decode the polyline string into a list of coordinates
    coords = polyline.decode(polyline_str)
    
    # Step 2: Create a Pandas DataFrame from the list of coordinates
    df = pd.DataFrame(coords, columns=['latitude', 'longitude'])
    
    # Step 3: Calculate the distance between consecutive points using the Haversine formula
    distances = [0]  # First point has 0 distance
    for i in range(1, len(df)):
        # Calculate distance between current point and previous point
        prev_point = (df.loc[i-1, 'latitude'], df.loc[i-1, 'longitude'])
        curr_point = (df.loc[i, 'latitude'], df.loc[i, 'longitude'])
        dist = geodesic(prev_point, curr_point).meters
        distances.append(dist)
    
    # Add the distance column to the DataFrame
    df['distance'] = distances
    
    return df

# Sample polyline string (encoded latitude and longitude)
polyline_str = "_p~iF~ps|U_ulLnnqC_mqNvxq`@"

# Call the function with the sample input
output_df = polyline_to_dataframe(polyline_str)
print(output_df)
