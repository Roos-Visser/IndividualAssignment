import json

# Open json file with data
with open('Bosnia1993Data.json', encoding='utf-16') as file:
    data = json.load(file)

event = data[0]

# Convert json file to a csv file with header and only useful columns
with open('Bosnia1993Data.csv', 'w', encoding='utf8') as file:
    file.write(f"best_estimate, highest_reliable_estimate, lowest_reliable_estimate\n")
    for event in data:
        file.write(f"{event['best']}, {event['high']}, {event['low']}\n")
    