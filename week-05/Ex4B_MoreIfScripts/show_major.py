"""Display a student's major and department office."""

student_name = "Patrick"
student_major = "CSCI"

if student_major == "BIOL":
    major_name = "Biology"
    office_location = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    office_location = "Sheppard Hall, Room 314"
elif student_major == "ENGL":
    major_name = "English"
    office_location = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    office_location = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    office_location = "Westly Hall, Room 310"
else:
    major_name = "<unknown>"
    office_location = ""

print("Student Major Lookup")
print("--------------------")
print(f"Student Name: {student_name}")
print(f"Major Code: {student_major}")
print(f"Major Name: {major_name}")
print(f"Office Location: {office_location}")