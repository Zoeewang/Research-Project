import csv
import json

with open('FOMC_token_separated_col.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('speaker_raw.json', 'w') as f:
    json.dump(rows, f)