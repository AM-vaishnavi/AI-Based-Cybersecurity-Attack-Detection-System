# Convert All Parquet Files to CSV

import pandas as pd
import glob
import os

print("=" * 60)
print("AI-Based Network Intrusion Detection System")
print("Parquet to CSV Converter")
print("=" * 60)

# Find All Parquet Files

parquet_files = glob.glob("datasets/*.parquet")

if len(parquet_files) == 0:
    print("\nNo Parquet files found in the 'datasets' folder.")
    exit()

print(f"\nFound {len(parquet_files)} Parquet files.\n")

# Convert Each File

for i, file in enumerate(parquet_files, start=1):

    print(f"[{i}/{len(parquet_files)}] Processing...")

    print("Reading :", os.path.basename(file))

    # Read parquet
    df = pd.read_parquet(file)

    # Create CSV filename
    csv_file = os.path.splitext(file)[0] + ".csv"

    # Save CSV
    df.to_csv(csv_file, index=False)

    print("Saved   :", os.path.basename(csv_file))
    print("-" * 60)

print("\nAll Parquet files converted successfully!")