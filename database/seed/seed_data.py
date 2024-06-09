import sys
import os

# Adjust the Python path to include the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Now import the Breed model
from backend.models.breed import Breed

# Define the breeds
breeds = [
    Breed(name='Chiwawa', info='작지만 사납다.'),
    Breed(name='Labrador', info='똑똑하고 온순하다.'),
    # Add more breeds as needed
]

# Save the breeds to the database
for breed in breeds:
    breed.save()
