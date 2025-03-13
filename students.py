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

# students.py

# List containing student dictionaries
students = [
    {
        'first_name': 'Jack',
        'last_name': 'Williams',
        'index_number': '55001',
        'nationality': 'American',
        'starting_date': '3/10/2025',
        'courses': ['Computer Science', 'Mathematics']
    },
    {
        'first_name': 'Elena',
        'last_name': 'Petrova',
        'index_number': '55002',
        'nationality': 'Russian',
        'starting_date': '3/12/2025',
        'courses': ['Physics', 'Chemistry']
    },
    {
        'first_name': 'Alessandro',
        'last_name': 'Bianchi',
        'index_number': '55003',
        'nationality': 'Italian',
        'starting_date': '3/15/2025',
        'courses': ['History', 'Philosophy']
    }
]

# students.py

# Existing students
students = [
    {
        'first_name': 'Jack',
        'last_name': 'Williams',
        'index_number': '55001',
        'nationality': 'American',
        'starting_date': '3/10/2025',
        'courses': ['Computer Science', 'Mathematics']
    },
    {
        'first_name': 'Elena',
        'last_name': 'Petrova',
        'index_number': '55002',
        'nationality': 'Russian',
        'starting_date': '3/12/2025',
        'courses': ['Physics', 'Chemistry']
    },
    {
        'first_name': 'Alessandro',
        'last_name': 'Bianchi',
        'index_number': '55003',
        'nationality': 'Italian',
        'starting_date': '3/15/2025',
        'courses': ['History', 'Philosophy']
    }
]

# Function to add a new student
def add_student(first_name, last_name, index_number, nationality, starting_date, courses):
    new_student = {
        'first_name': first_name,
        'last_name': last_name,
        'index_number': index_number,
        'nationality': nationality,
        'starting_date': starting_date,
        'courses': courses
    }
    students.append(new_student)

# Adding new students for testing
add_student('Sophia', 'Müller', '55004', 'German', '3/18/2025', ['Software Engineering', 'AI'])
add_student('Carlos', 'Gomez', '55005', 'Spanish', '3/20/2025', ['Data Science', 'Machine Learning'])

# Print all students
for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index Number: {student['index_number']}")
