import csv

lunch = {
    '고갯마루': '02-123-4567',
    '세븐브릭스': '02-456-7890',
    '아랑졸돈까스': '02-534-3466'
}

# 1 . String formatting
# with open('lunch.csv','w', encoding='utf-8') as f:
#     for item in lunch.items():
#         f.write(f'{item[0]},{item[1]}\n')

# 2. join
# with open('lunch.csv','w',encoding='utf-8') as f:
#     for item in lunch.items():
#         f.write(','.join(item) + '\n')

# 3. csv.write
with open('lunch.csv','w',encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)