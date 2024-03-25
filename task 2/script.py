from collections import defaultdict
from datetime import datetime
import os

minute_counts = defaultdict(int)

file_path = os.path.join(os.path.dirname(__file__), '..', 'Presidential_Debate.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()

        try:
            timestamp = datetime.strptime(line, '%a %b %d %H:%M:%S +0000 %Y')
            timestamp = timestamp.replace(second=0, microsecond=0)
            minute_counts[timestamp] += 1
        except ValueError:
            pass

for timestamp, count in sorted(minute_counts.items()):
    print(f"{timestamp}: {count} tweets")
