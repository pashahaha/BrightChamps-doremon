"""with open('file_handling/IPL_2018.csv') as f:
    data = f.read()
print(data)
"""

"""import csv
with open('file_handling/IPL_2018.csv') as f:
    data = csv.reader(f, delimiter = ",")
    for row in data:
        print(row)
"""

import csv
with open('file_handling\IPL_2018.csv') as f:
    data = csv.reader(f)

    data_list = list(data)

match_runs = []
for row in data_list[1:]:
    print("total runs of", row[0], "is", row[5])
    match_runs.append(int(row[5]))

print("total runs of all matches is", sum(match_runs))