import csv
from matplotlib import pyplot as plt

DATA_FILE = '06-drones.csv'

data = []
with open(DATA_FILE, 'r', encoding='latin-1') as fin:
	reader = csv.DictReader(fin)
	data = [row for row in reader]
	#for row in reader:
	#	data.append(row)

print(data[0])

###################
# Let's make a histogram of strike locations!
###################

locations = [strike['Location'] for strike in data]

#{'Datta Khel': 5, 'Mosaki': 2, ...}
loc_hist = {}
for location in locations:
	# Is location already a key in the dictionary?
	if location in loc_hist:
		loc_hist[location] += 1		
	else:
		loc_hist[location] = 1

print(loc_hist)
print()
print(sorted(loc_hist.values()))
print()
print(sorted(set(loc_hist.keys())))
