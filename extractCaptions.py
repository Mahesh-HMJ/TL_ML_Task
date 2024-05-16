import csv

def extract_column_to_text(csv_file, text_file, column_index):
    """
    Extracts a specific column from a CSV file and writes it to a text file.

    Parameters:
    - csv_file: Path to the CSV file to read.
    - text_file: Path to the text file to write.
    - column_index: Index of the column to extract.
    """
    # Open the CSV file for reading
    with open(csv_file, 'r', newline='', encoding='utf-8') as csv_f:
        reader = csv.reader(csv_f)
        
        # Open the text file for writing
        with open(text_file, 'w', encoding='utf-8') as txt_f:
            # Iterate over each row in the CSV file
            for row in reader:
                # Extract the element at the specified column index
                column_value = row[column_index]
                
                # Write the extracted element to the text file
                txt_f.write(column_value + '\n')

# Usage example:
# Path to the CSV file
csv_file_path = 'captions.csv'

# Path to the output text file
text_file_path = 'extractedCaptions.txt'

# Index of the column to extract (e.g., 0 for the first column)
column_index = 1

# Call the function to extract the column and write it to the text file
extract_column_to_text(csv_file_path, text_file_path, column_index)
