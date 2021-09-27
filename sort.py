import csv 

data=[]
with open("dataset_2.csv","r")as f :
    csv_reader = csv.reader(f)
    for row in csv_reader :
        data.append(row)

headers = data[0]
planet_data = data[1:]

for i in planet_data :
    i[2]=i[2].lower()

planet_data.sort(key=lambda planet_data : planet_data[2])

with open("sorted_data2.csv" , "a+") as f :
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)


