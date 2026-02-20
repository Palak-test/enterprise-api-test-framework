"""
CSV data loader for enterprise-api-test-framework
"""
import csv
import os

def load_csv_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
