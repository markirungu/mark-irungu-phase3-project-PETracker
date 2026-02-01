from models import session
from models.pet import Pet
from models.task import Task

def exit_program():
    print("Goodbye!")
    exit()

#pet helpers, get all pets data and manage it
def list_pets():
    pets = session.query(Pet).all()
    if pets:
        for pet in pets:
            print(f"{pet.id}. {pet.name} the {pet.species}")
    else:
        print("No pets found.")

def find_pet_by_id():
    id_ = input("Enter the pet's ID: ")
    pet = session.query(Pet).filter(Pet.id == id_).first()
    if pet:
        print(f"Found: {pet.name} the {pet.species}")
        return pet
    else:
        print(f"Pet {id_} not found.")
        return None

def create_pet():
    name = input("Enter the pet's name: ")
    species = input("Enter the pet's species (e.g., Dog, Cat): ")
    if name and species:
        pet = Pet(name=name, species=species)
        session.add(pet)
        session.commit()
        print(f"Successfully created {name}!")
    else:
        print("Creation failed. Need both name and species.")

def delete_pet():
    id_ = input("Enter the pet's ID to delete: ")
    pet = session.query(Pet).filter(Pet.id == id_).first()
    if pet:
        confirmation = input(f"Delete {pet.name}? (y/n): ").lower()
        if confirmation == 'y':
            session.delete(pet)
            session.commit()
            print(f"Deleted {pet.name}.")
    else:
        print(f"Pet {id_} not found.")

def view_pet_tasks():
    pet = find_pet_by_id()
    if pet:
        if pet.tasks:
            for task in pet.tasks:
                status = "✓" if task.completed else " "
                print(f"  [{status}] {task.id}. {task.description}")
        else:
            print(f"  No tasks for {pet.name}.")

# task ghelpers
def list_tasks():
    tasks = session.query(Task).all()
    if tasks:
        for task in tasks:
            status = "Done" if task.completed else "Pending"
            print(f"{task.id}. {task.description} (Pet ID: {task.pet_id}) [{status}]")
    else:
        print("No tasks found.")

def find_task_by_id():
    id_ = input("Enter the task's ID: ")
    task = session.query(Task).filter(Task.id == id_).first()
    if task:
        print(f"Found: {task.description}")
        return task
    else:
        print(f"Task {id_} not found.")
        return None

def create_task():
    print("Let's create a new task.")
    pet = find_pet_by_id()
    if pet:
        description = input("Enter the task description: ")
        if description:
            task = Task(description=description, pet_id=pet.id)
            session.add(task)
            session.commit()
            print(f"Task '{description}' added for {pet.name}!")
    else:
        print("Cannot create task without a valid pet.")

def delete_task():
    task = find_task_by_id()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.description}' deleted.")

def mark_task_complete():
    task = find_task_by_id()
    if task:
        task.completed = True
        session.commit()
        print(f"Marked '{task.description}' as complete!")

# demo data structures as required
def demo_data_structures():
    """Demonstrating use of lists, dicts, and tuples."""
    #common pets for ease of use
    common_species = ["Dog", "Lizard", "Fish", "My cat", "Lion"]
    print("Common pet species (List):", common_species)

    # A DICT mapping species to example names
    species_names = {
        "Dog": ["Buddy", "Max"],
        "Cat": ["Whiskers", "Luna"],
        "Fish": ["Goldie"]
    }
    print("\nExample names per species (Dict):", species_names)

    # A TUPLE for a fixed pet record namely:(ID, Name, Species)
    pet_record = (1, "gitau", "Dragon")
    print(f"\nA single pet record (Tuple): ID={pet_record[0]}, Name={pet_record[1]}")