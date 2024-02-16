
student = {'name': 'Kirk',
           'age': 20,
           'major': 'MIS',
           'hobbies': ['Lifting', 'Basketball', 'Painting'] }

#add new key value
student['State'] = 'Texas'

#update current age +1
student['age'] += 1

#iterate through dictionary
for key, value in student.items():
    print(f'{key}: {value}')
