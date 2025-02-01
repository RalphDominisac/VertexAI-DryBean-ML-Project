from pathlib import Path
import pandas as pd

# Set the correct file path
data_path = Path(r"D:\Desktop\dry-bean-dataset\DryBeanDataset\Dry_Bean_Dataset.xlsx")

# Read the Excel file
beans = pd.read_excel(data_path)

# Display dataset shape
print(beans.shape)  # Should output: (13611, 17)

# Save as CSV in the converted-dataset folder
csv_path = data_path.parent / "converted-dataset" / "dry_bean.csv"
beans.to_csv(csv_path, index=False)

print(f"CSV file saved at: {csv_path}")
