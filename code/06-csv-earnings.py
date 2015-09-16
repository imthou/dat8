import csv

EARNINGS_FILE = 'earnings.csv'

data = []

# 'UTF-8', 'latin-1', 'ascii'
with open(EARNINGS_FILE, 'r', encoding='latin-1') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        try:
            row['veteran'] = float(row['veteran'])
            data.append(row)
        except ValueError:
            pass
            #row['veteran'] = 0.0


vets_colleges = [(college['veteran'], college['INSTNM']) for college in data]

print('MAX: ', max(vets_colleges))
print('MIN: ', min(vets_colleges))
print('NUM ZERO: ', len([vc for vc in vets_colleges if vc[0] == 0.0]))


#print('AVG: ', sum(veterans)/len(veterans))
#print(data[0]['veteran'])

#fin = open(EARNINGS_FILE, 'r', encoding='UTF-8')
#lines = fin.readlines()
#fin.close()

#print(lines[0])
#print(lines[1])