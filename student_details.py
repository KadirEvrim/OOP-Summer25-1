first_name = "Kadir" 
last_name = "Evrim"
index_number "35096"
nationality = "Turkish" 
starting_date = "3/13/2025" 
courses = ["Computer science"]


print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Index Number: {index_number}")
print(f"Nationality: {nationality}")
print(f"Starting Date: {starting_date}")
print(f"Courses: {', '.join(courses)}")




students = [
    {
        'first_name': 'Kadir',
        'last_name': 'Evrim',
        'index_number': '35096',
        'nationality': 'Turkish',
        'starting_date': '3/13/2025',
        'courses': ['Computer Science']
    },
    {
        'first_name': 'Alice',
        'last_name': 'Johnson',
        'index_number': '35123',
        'nationality': 'American',
        'starting_date': '3/15/2025',
        'courses': ['Mathematics', 'Physics']
    },
    {
        'first_name': 'Tom',
        'last_name': 'Smith',
        'index_number': '35245',
        'nationality': 'British',
        'starting_date': '3/20/2025',
        'courses': ['History', 'Philosophy']
    }
]

for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index Number: {student['index_number']}")
