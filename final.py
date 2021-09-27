import csv 

data1 = []
data2 = []

with open("dataset_1.csv" ,"r") as f :
    csv_reader = csv.reader(f)
    for row in csv_reader :
        data1.append(row)
headers1 = data1[0]
planet_data_1  = data1[1:]   

with open("sorted_data2.csv","r") as f :
    csv2_reader = csv .reader(f)
    for row in csv2_reader :
        data2.append(row)
headers2 = data2[0]
planet_data_2 = data2[1:]        

planet_data  = []
headers = headers1 +  headers2 

for index,row in enumerate(planet_data_1) :
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open('final.csv' , "a+") as f :
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)