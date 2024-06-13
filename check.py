import os
import pandas as pd

file_path = r"C:\Users\preet\OneDrive\Desktop\Preethi's Dashboard\employee_time_cards.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    print(f"File not found: {file_path}")
