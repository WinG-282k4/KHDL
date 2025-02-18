import csv

def convert_to_t4(diem_t10):
    if diem_t10 >= 8.5:
        return 'A'
    elif diem_t10 >= 7.0:
        return 'B'
    elif diem_t10 >= 5.5:
        return 'C'
    elif diem_t10 >= 4.0:
        return 'D'
    else:
        return 'F'
        

class Student:
    def __init__(self, mssv, Hoten, diem10):
        self.mssv = mssv
        self.Hoten = Hoten
        self.diem10 = diem10
        self.diem4 = convert_to_t4(diem10)
    
    def __str__(self):
        return f'{self.mssv} - {self.Hoten} - {self.diem10} - {self.diem4}'
    
# Read students from file
def read_students(filename):
    students = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            students.append(Student(row[0], row[1], float(row[2])))
    return students

# Write students to file
def write_students(students, filename):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([ 'MSSV', 'Họ tên', 'Điểm 10', 'Điểm 4'])
        for student in students:
            writer.writerow([ student.mssv, student.Hoten, student.diem10, student.diem4])

# Thong ke so luong sinh vien theo diem 4
def count_grades(students):
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for student in students:
        counts[student.diem4] += 1
    return counts

# Get top n Students
def get_top_students(students, n):
    students.sort(key=lambda x: x.diem10, reverse=True)
    return students[:n]

#Get among [a,b] diem 10
def get_students_in_range(students, a, b):
    Students_rs = []
    for student in students:
        if student.diem10 >= a and student.diem10 <= b:
            Students_rs.append(student)
    return Students_rs

# Get average grade
def avg_grade(students):
    sum = 0
    for student in students:
        sum += student.diem10
    return sum/len(students)

# Get standard deviation
def stan_deviation(students):
    avg = avg_grade(students)
    sum = 0
    for student in students:
        sum += (student.diem10 - avg)**2
    return (sum/len(students))**0.5

# Get median grade
def median_grade(students):
    students.sort(key=lambda x: x.diem10)
    n = len(students)
    if n % 2 == 0:
        return (students[n//2-1].diem10 + students[n//2].diem10)/2
    else:
        return students[n//2].diem10

# calculate_statistics
def calculate_statistics(students):
    mean = avg_grade(students)
    std = stan_deviation(students)
    median = median_grade(students)

    Students.sort(key=lambda x: x.diem10, reverse = True)
    n = len(students)

    Q1 = students[n//4].diem10 if n % 4 == 0 else (students[n//4-1].diem10 + students[n//4].diem10)/2
    Q2 = median
    Q3 = students[3*n//4].diem10 if n % 4 == 0 else (students[(3*n//4)-1].diem10 + students[3*n//4].diem10)/2
    return {'mean': mean, 'std': std, 'median': median, 'Q1': Q1, 'Q2':Q2, 'Q3': Q3}

#Get quantile
def get_quantile(students, q):
    statistics = calculate_statistics(students)
    if q > statistics['Q1']:
        return 'Q1'
    elif q > statistics['Q2']:
        return 'Q2'
    elif q > statistics['Q3']:
        return 'Q3'
    else:
        return 'Q4'
    
# Write students with quantile to file
def write_students_with_quantile(students, filename):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([ 'MSSV', 'Họ tên', 'Điểm 10', 'Điểm 4', 'Phân vị'])
        for student in students:
            quantile = get_quantile(students, student.diem10)
            writer.writerow([student.mssv, student.Hoten, student.diem10, student.diem4, quantile])
        
#Read_write file csv
Students = read_students('Diem_XLTHS_CSV.csv')
# write_students(Students, 'Bt2/So_diem4.csv')

# Thong ke so luong sinh vien theo diem 4
print('\nThong ke so luong sinh vien theo diem 4')
Counts = count_grades(Students)
print(Counts)

# Get top 5 Students
print('\nTop 5 Students')
top_students = get_top_students(Students, 10)
for student in top_students:
    print(student)

# # Get students in range [5.5, 8.0]
# print('\nStudents in range [5.5, 8.0]')
# Students = read_students('Diem_XLTHS_CSV.csv')
# students_in_range = get_students_in_range(Students, 5.5, 8.0)
# for student in students_in_range:
#     print(student)

# Caculate
print('\nCaculate_Statistics')
Students = read_students('Diem_XLTHS_CSV.csv')
Caculate_Student = calculate_statistics(Students)
print(Caculate_Student)

# #print quantile to csv
# Students = read_students('Diem_XLTHS_CSV.csv')
# write_students_with_quantile(Students, 'So_diem_phan_vi.csv')
