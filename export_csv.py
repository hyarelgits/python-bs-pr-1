import csv

with open("students.csv","w",newline="") as f:

    writer = csv.writer(f)

    writer.writerow(["Name","Marks"])

    writer.writerow(["Hyarel",90])
