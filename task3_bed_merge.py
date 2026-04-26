import pandas as pd

file = "input.bed"
output_file = "output.bed"

cols = ["chr", "start", "end"]

df = pd.read_table(file, sep="\t", header=None, names=cols)
df = df.sort_values(by=["chr", "start", "end"]).reset_index(drop=True)

merged = []

current_row_chr = df.iloc[0]["chr"]
current_row_start = df.iloc[0]["start"]
current_row_end = df.iloc[0]["end"]

for i in range(1, len(df)):
    next_row = df.iloc[i]

    if next_row["chr"] == current_row_chr and next_row["start"] <= current_row_end:
        current_row_end = max(current_row_end, next_row["end"])
    else:
        merged.append([current_row_chr, current_row_start, current_row_end])

        current_row_chr = next_row["chr"]
        current_row_start = next_row["start"]
        current_row_end = next_row["end"]

merged.append([current_row_chr, current_row_start, current_row_end])

df_merged = pd.DataFrame(merged, columns=cols)
df_merged.to_csv(output_file, sep="\t", index=False, header=False)

