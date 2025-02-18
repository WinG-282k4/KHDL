class student:
    def __init__(self, stt, MSSV, Name, SDT):
        self.stt = stt
        self.MSSV = MSSV
        self.Name = Name
        self.SDT = SDT

    def display(self):
        print("STT: ", self.stt)
        print("MSSV: ", self.MSSV)
        print("Name: ", self.Name)
        print("SDT: ", self.SDT)
        print("\n")

S = []
sl = int(input("Nhập số lượng sinh viên: "))
for i in range(sl):
    stt = int(input("Nhập STT: "))  # Convert input to integer
    MSSV = input("Nhập MSSV: ")
    Name = input("Nhập Name: ")
    SDT = input("Nhập SDT: ")
    print("\n")
    student1 = student(stt, MSSV, Name, SDT)
    S.append(student1)

#sort S
S.sort(key=lambda x: x.stt)

# Display all students
# print("Danh sách sinh viên: ")
# for student in S:
#     student.display()

# export to file csv
import csv
with open('student.csv', mode='w', newline='', encoding = 'utf_8') as file:
    writer = csv.writer(file)
    writer.writerow(["STT", "MSSV", "Name", "SDT"])
    for student in S:
        writer.writerow([student.stt, student.MSSV, student.Name, student.SDT])

#import file csv
with open('student.csv', mode='r', encoding = 'utf_8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)