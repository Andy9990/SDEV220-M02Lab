#Andrew Gottschalk
#Lab-M02
#Program that tells if your GPA is high enough to be on the dean's list or the Honor Roll

while True:
    last_name = input('Enter the student\'s last name: ')
    if last_name == 'ZZZ':
        break
    first_name = input('Enter the student\'s first name: ')
    gpa = float(input('Enter the student\'s GPA: '))
    if gpa >= 3.5:
        print(f'{first_name} {last_name} has made the Dean\'s List.')
    elif gpa >= 3.25:
        print(f'{first_name} {last_name} has made the Honor Roll.')
