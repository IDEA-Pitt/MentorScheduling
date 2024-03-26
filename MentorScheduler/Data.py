import Mentor
import csv #i'm just downloading the csv of the response once it's done

with open('data.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
    