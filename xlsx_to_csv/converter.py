import pandas as pd
import os
excel_file = "sheet.xlsx"
excel = pd.ExcelFile(excel_file)
output_dir = "sheet"
os.makedirs(output_dir, exist_ok=True)
for sheet_name in excel.sheet_names:
    df = pd.read_excel(excel, sheet_name=sheet_name)
    csv_file = os.path.join(output_dir, f"{sheet_name}.csv")
    df.to_csv(csv_file, index=False)
    print(f'Converted sheet "{sheet_name}" to CSV: {csv_file}')
print("Conversion completed")
