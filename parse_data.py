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

deaths = [[ 0 for a in range(len(states))]
            for b in range(len(dates))]

new_cases = [[ 0 for a in range(len(states))]
            for b in range(len(dates))]

new_deaths = [[ 0 for a in range(len(states))]
            for b in range(len(dates))]

smooth_new_cases = [[ 0 for a in range(len(states))]
            for b in range(len(dates))]

smooth_new_deaths = [[ 0 for a in range(len(states))]
            for b in range(len(dates))]

for i in range(len(states)):
    for j in range(len(dates)):
        if i == 0:
            data[j][i] = j
            deaths[j][i] = j
            new_cases[j][i] = j
            new_deaths[j][i] = j
            smooth_new_cases[j][i] = j
            smooth_new_deaths[j][i] = j


data[0][:] = states
deaths[0][:] = states
new_cases[0][:] = states
new_deaths[0][:] = states
smooth_new_cases[0][:] = states
smooth_new_deaths[0][:] = states

smooth_range = 5

j = 0
for i in raw:
    if j > 1:
        if i[0] in dates:
            x = dates.index(i[0])
            prev = x - 1
            y = states.index(i[1])
            data[x][y] = i[3]
            deaths[x][y] = i[4]

            new_cases[x][y] = int(i[3]) - int(data[prev][y])
            new_deaths[x][y] = int(i[4]) - int(deaths[prev][y])
            if j > (smooth_range + 1):
                smooth_new_cases[x][y] = sum([int(new_cases[k][y]) for k in range (x-smooth_range + 1,x + 1)])/smooth_range
                smooth_new_deaths[x][y] = sum([int(new_deaths[k][y]) for k in range (x-smooth_range + 1,x + 1)])/smooth_range
    else:
        if i[0] in dates:
            x = dates.index(i[0])
            prev = x
            y = states.index(i[1])
            data[x][y] = i[3]
            deaths[x][y] = i[4]
            new_cases[x][y] = i[3]
            new_deaths[x][y] = i[4]
    j = j + 1

data[0][:] = states
deaths[0][:] = states
new_cases[0][:] = states
new_deaths[0][:] = states
smooth_new_cases[0][:] = states
smooth_new_deaths[0][:] = states
data[0][0] = 'year'
deaths[0][0] = 'year'
new_cases[0][0] = 'year'
new_deaths[0][0] = 'year'
smooth_new_cases[0][0] = 'year'
smooth_new_deaths[0][0] = 'year'

for i in range(len(data[0])):
    data[0][i] = data[0][i].replace(" ","")
    deaths[0][i] = deaths[0][i].replace(" ","")
    new_cases[0][i] = new_cases[0][i].replace(" ","")
    new_deaths[0][i] = new_deaths[0][i].replace(" ","")
    smooth_new_cases[0][i] = smooth_new_cases[0][i].replace(" ","")
    smooth_new_deaths[0][i] = smooth_new_deaths[0][i].replace(" ","")


with open('organized_data6.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')
    for i in range(len(data)):
        output_writer.writerow(data[i])

with open('organized_deaths.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')
    for i in range(len(deaths)):
        output_writer.writerow(deaths[i])

with open('new_cases.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')
    for i in range(len(new_cases)):
        output_writer.writerow(new_cases[i])

with open('new_deaths.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')
    for i in range(len(new_deaths)):
        output_writer.writerow(new_deaths[i])

with open('smooth_new_cases.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')
    for i in range(len(smooth_new_cases)):
        output_writer.writerow(smooth_new_cases[i])

with open('smooth_new_deaths.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')
    for i in range(len(smooth_new_deaths)):
        output_writer.writerow(smooth_new_deaths[i])
