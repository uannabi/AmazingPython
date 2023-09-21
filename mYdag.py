'''
Replace 'path/to/your/first.csv' and 'path/to/your/second.csv' with the paths to the two CSV files you want to compare.

Note: This script assumes that the two CSV files are of the same length and have the same headers. If this is not the case, additional logic would be needed to handle those scenarios.

'''
def compare_csv_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        # Read header
        header1 = file1.readline().strip()
        header2 = file2.readline().strip()

        # Check if headers are the same
        if header1 != header2:
            return f"Header mismatch: {header1} != {header2}"

        # Initialize variables to keep track of line numbers and mismatches
        line_number = 1
        mismatches = []

        # Compare line by line
        while True:
            line1 = file1.readline().strip()
            line2 = file2.readline().strip()

            # Break the loop if we've reached the end of both files
            if not line1 and not line2:
                break

            # Check for mismatched lines
            if line1 != line2:
                mismatches.append(f"Line {line_number}: {line1} != {line2}")

            line_number += 1

        if not mismatches:
            return "Success"
        else:
            return "\n".join(mismatches)


# Replace with the paths to your CSV files
file1_path = 'path/to/your/first.csv'
file2_path = 'path/to/your/second.csv'

result = compare_csv_files(file1_path, file2_path)
print(result)
