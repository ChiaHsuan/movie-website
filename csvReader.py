import csv

with open('myMovies.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Title'], row['Image'])