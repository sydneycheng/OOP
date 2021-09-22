import StudentClass as sc

studentid = 1001
name = 'John'
dob = '1/1/2000'
classification = 'junior'

#This is a class definition
john = sc.Student(studentid, name, dob, classification)

#doesn't need any parameters bcs all it needs is dob, which is already included
john.calc_age()

john.register()

print("Student age is:", john.get_age())

print("Student can register between:",john.get_registration())