import re
from typing import List

def find_all_dates(text: str) -> List[str]:
    """
    This function takes a string as input and returns a list of valid dates
    in 'dd-mm-yyyy', 'mm/dd/yyyy', or 'yyyy.mm.dd' format found in the string.
    
    Parameters:
    text (str): A string containing the dates in various formats.

    Returns:
    List[str]: A list of valid dates in the formats specified.
    """
    # Regular expression patterns for the specified date formats
    patterns = [
        r'\b(\d{2})-(\d{2})-(\d{4})\b',  # dd-mm-yyyy
        r'\b(\d{2})/(\d{2})/(\d{4})\b',  # mm/dd/yyyy
        r'\b(\d{4})\.(\d{2})\.(\d{2})\b'   # yyyy.mm.dd
    ]
    
    # Combine all patterns into a single regex pattern
    combined_pattern = '|'.join(patterns)
    
    # Find all matches in the text
    matches = re.findall(combined_pattern, text)
    
    # Flatten the matches and construct the correct date strings
    valid_dates = []
    for match in matches:
        # Each match is a tuple with groups, determine which format was matched
        if match[0]:  # dd-mm-yyyy
            valid_dates.append(f"{match[0]}-{match[1]}-{match[2]}")
        elif match[3]:  # mm/dd/yyyy
            valid_dates.append(f"{match[3]}/{match[4]}/{match[5]}")
        elif match[6]:  # yyyy.mm.dd
            valid_dates.append(f"{match[6]}.{match[7]}.{match[8]}")
    
    return valid_dates

# Example usage
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
result = find_all_dates(text)
print(result)
