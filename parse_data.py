import csv
states = []
dates = []

raw = []

with open('../covid-19-data/us-states.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        raw.append(row)
        if row[1] in states:
            print(states.index(row[1]))
        else:
            states.append(row[1])
        if row[0] in dates:
            print(dates.index(row[0]))
        else:
            dates.append(row[0])

data = [[ 0 for a in range(len(states))]
            for b in range(len(dates))]

for i in range(len(states)):
    for j in range(len(dates)):

        if i == 0:
            data[j][i] = j


data[0][:] = states

for i in raw:
    if i[0] in dates:
        data[dates.index(i[0])][states.index(i[1])] = i[3]

for i in range(len(data[0])):
    data[0][i] = data[0][i].replace(" ","")

with open('organized_data5.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')
    for i in range(len(data)):
        output_writer.writerow(data[i])
