# animals.py

# List to store animal details
animals = [
    {
        'name': 'Cat',
        'group': 'Mammals',
        'number_of_legs': 4,
        'skills': ['climbing', 'jumping', 'hunting']
    },
    {
        'name': 'Eagle',
        'group': 'Birds',
        'number_of_legs': 2,
        'skills': ['flying', 'hunting', 'sharp vision']
    },
    {
        'name': 'Fish',
        'group': 'Fish',
        'number_of_legs': 0,
        'skills': ['swimming', 'breathing underwater']
    },
    {
        'name': 'Snake',
        'group': 'Reptiles',
        'number_of_legs': 0,
        'skills': ['slithering', 'hunting', 'camouflage']
    },
    {
        'name': 'Dog',
        'group': 'Mammals',
        'number_of_legs': 4,
        'skills': ['running', 'fetching', 'guarding']
    }
]

# Print information about each animal
for animal in animals:
    print(f"Animal: {animal['name']}")
    print(f"Group: {animal['group']}")
    print(f"Legs: {animal['number_of_legs']}")
    print(f"Skills: {', '.join(animal['skills'])}")
    print("\n")
