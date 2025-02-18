import csv

def read_file(file_path, print_data=False):
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        data = []
        for row in csv_reader:
            data.append(row)
            if print_data:
                print(row)
        return data

def write_file(file_path, data): # data is a list of list
    with open(file_path, mode='w', encoding='utf-8-sig', newline='') as file: # newline='' to avoid empty row between each row
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

def add_grade_T4_column(file_path, new_file_path):
    data = read_file(file_path)
    if len(data) == 0:
        print('Data is empty')
        return
    if data[0][-1] == 'Điểm T4':
        return
    data[0].append('Điểm T4')
    for i in range(1, len(data)):
        if float(data[i][-1]) >= 8.5:
            data[i].append('A')
        elif float(data[i][-1]) >= 7.0:
            data[i].append('B')
        elif float(data[i][-1]) >= 5.5:
            data[i].append('C')
        elif float(data[i][-1]) >= 4.0:
            data[i].append('D')
        else:
            data[i].append('F')
    write_file(new_file_path, data)

def count_grade(file_path):
    data = read_file(file_path)
    grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for i in range(1, len(data)):
        grade_count[data[i][-1]] += 1
    return grade_count

def top_n_student(file_path, n):
    data = read_file(file_path)
    if len(data) == 0:
        print('Data is empty')
        return
    data_sorted = sorted(data[1:], key=lambda x: float(x[-2]), reverse=True)
    data_sorted = [data[0]] + data_sorted
    return data_sorted[:n]

def filter_student(file_path, a, b):
    data = read_file(file_path)
    if len(data) == 0:
        print('Data is empty')
        return
    data_filtered = [data[0]]
    for row in data[1:]:
        if a <= float(row[-2]) <= b:
            data_filtered.append(row)
    return data_filtered

def describe_grade(file_path):
    data = read_file(file_path)
    if len(data) == 0:
        print('Data is empty')
        return
    grade = [float(row[-2]) for row in data[1:]]
    mean = sum(grade) / len(grade)
    std = (sum([(x - mean) ** 2 for x in grade]) / len(grade)) ** 0.5
    grade_sorted = sorted(grade)
    n = len(grade_sorted)
    median = grade_sorted[n // 2] if n % 2 == 1 else (grade_sorted[n // 2 - 1] + grade_sorted[n // 2]) / 2
    q1 = grade_sorted[n // 4]
    q2 = grade_sorted[n // 2]
    q3 = grade_sorted[3 * n // 4]
    return mean, std, median, q1, q2, q3

def add_grade_Q_column(file_path, new_file_path):
    data = read_file(file_path)
    if len(data) == 0:
        print('Data is empty')
        return
    if data[0][-1] == 'Điểm thang Q':
        return
    data[0].append('Điểm thang Q')
    for i in range(1, len(data)):
        if str(data[i][-1]) == 'A':
            data[i].append(4)
        elif str(data[i][-1]) == 'B':
            data[i].append(3)
        elif str(data[i][-1]) == 'C':
            data[i].append(2)
        # elif str(data[i][-1]) == 'D':
        #     data[i].append(1)
        else:
            data[i].append(1)
    write_file(new_file_path, data)

# file_path = 'DSSV_CSV.csv'
file_path = 'Diem_XLTHS_CSV.csv'
data = read_file(file_path, print_data=False)

# new_file_path = 'DSSV_CSV_new.csv'
new_file_path = file_path.split('.')[0] + '_new.csv'
add_grade_T4_column(file_path, new_file_path)
print('Data after adding grade column:')
data = read_file(new_file_path, print_data=False)

grade_count = count_grade(new_file_path)
print('Grade count:', grade_count)

top_10_data = top_n_student(new_file_path, 10)
print('Top', 10, 'student:')
for row in top_10_data:
    print(row)

print('Filter student with grade in [a,b]')
a = input('Enter a: ')
b = input('Enter b: ')
data_filtered = filter_student(new_file_path, float(a), float(b))
print('Data filtered:')
for row in data_filtered:
    print(row)

mean, std, median, q1, q2, q3 = describe_grade(new_file_path)
print('Mean:', mean)
print('Std:', std)
print('Median:', median)
print('Q1:', q1)
print('Q2:', q2)
print('Q3:', q3)

new_file_path_Q = new_file_path.split('.')[0] + '_Q.csv'
add_grade_Q_column(new_file_path, new_file_path_Q)
print('Data after adding grade Q column:')
data = read_file(new_file_path_Q, print_data=False)