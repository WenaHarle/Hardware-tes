import csv

def calculate_volume(row):
    width = int(row['width'])
    height = int(row['height'])
    tall = int(row['tall'])
    grade = (row['grade'])
    volume = (4/3) * 3.14 * (width) * (height) * (tall) 
    result = int(volume)
    return result

input_filename = 'new_data.csv'
output_filename = 'volume.csv'

# Read the input CSV file and create a new output CSV file with an additional 'volume' column
with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
    csv_reader = csv.DictReader(input_file)
    fieldnames = csv_reader.fieldnames + ['volume']
    
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for row in csv_reader:
        volume = calculate_volume(row)
        row_with_volume = {**row, 'volume': volume}  # Create a new dictionary with the volume column
        csv_writer.writerow(row_with_volume)

print("Volume calculation and CSV write complete.")
