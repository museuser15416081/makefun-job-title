import os

output_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
entry_path = os.path.join(output_dir, "entry.txt")

title = "Senior Vice President of Apologizing to the Printer"
with open(entry_path, "w", encoding="utf-8") as f:
    f.write(title)

print("Job title written to entry.txt")
