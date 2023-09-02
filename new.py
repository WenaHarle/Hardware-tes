import csv

# Baca data dari file CSV
data = []
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)  # Baca header
    for row in csv_reader:
        data.append(row)

# Lakukan perhitungan dan simpan dalam list baru
new_data = []
for row in data:
    width = int(row[0])
    height = int(row[1])
    tall = int(row[2])
    grade = row[3]
    
    new_width = int (width / 2)
    new_height = int (height / 2)
    new_tall = int ((tall*1.6) /2 )   
    new_row = [new_width, new_height, new_tall, grade]
    new_data.append(new_row)

# Simpan hasil dalam file CSV baru
new_headers = ["new_width", "new_height", "tall", "grade"]
with open('new_data.csv', 'w', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)
    csv_writer.writerow(new_headers)
    csv_writer.writerows(new_data)

print("File baru 'new_data.csv' telah berhasil dibuat.")
