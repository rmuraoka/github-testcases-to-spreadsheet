import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
import glob
import re

if 'GOOGLE_CREDENTIALS' not in os.environ:
    raise ValueError("The environment variable 'GOOGLE_CREDENTIALS' is not found.")

try:
    creds_json = json.loads(os.environ['GOOGLE_CREDENTIALS'])
except json.JSONDecodeError as e:
    raise ValueError("The environment variable 'GOOGLE_CREDENTIALS' is not in a valid JSON format.") from e

# Setting up Google Authentication Credentials
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json)
client = gspread.authorize(creds)

# Open Spreadsheet
spreadsheet = client.open_by_key(os.environ['SPREADSHEET_ID'])

# Select a Specific Worksheet
worksheet = spreadsheet.worksheet(os.environ['WORKSHEET_TITLE'])

# Load all test case files in the 'testcases' folder
testcases_folder = './testcases/'
testcase_files = glob.glob(testcases_folder + '**/*.md', recursive=True)

# Store the contents of the test cases in a list
test_cases_data = []
for file_path in testcase_files:
    path_parts = os.path.relpath(file_path, testcases_folder).split(os.sep)
    filename = path_parts[-1]
    item1 = path_parts[0] if len(path_parts) > 1 else ""
    item2 = path_parts[1] if len(path_parts) > 2 else ""

    with open(file_path, 'r') as file:
        content = file.read()
        # Extract the tags section using regular expression
        tags_match = re.search(r'(?<=\n### Tags\n).+', content, re.DOTALL)
        tags = tags_match.group(0).strip() if tags_match else ""
        content_cleaned = re.sub(r'### Tags.*', '', content, flags=re.DOTALL)
        test_cases_data.append([filename, item1, item2, content_cleaned, tags])

# Write headers to the spreadsheet
worksheet.update('A1', [['Filename', 'Item1', 'Item2', 'Content, Tags']])

# Write test case data to the spreadsheet
if test_cases_data:
    worksheet.update('A2', test_cases_data)
