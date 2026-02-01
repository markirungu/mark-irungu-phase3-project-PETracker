# Import all the helper functions for the CLI menu to use
from helpers import (
    exit_program,          
    list_pets,             
    find_pet_by_id,        
    create_pet,         
    delete_pet,    
    view_pet_tasks,        
    list_tasks,           
    find_task_by_id,    
    create_task,           
    delete_task,           
    mark_task_complete,   
    demo_data_structures   
)

def main():
    """The heart of our CLI app - keeps running until user decides to exit, """
    # NB. the loop runs forever until we call exit_program()
    while True:
        main_menu()
        choice = input("> ")
        
        #choice handling
        if choice == "0":
            exit_program()
        elif choice == "1":
            pet_menu()
        elif choice == "2":
            task_menu()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    """Display the main navigation menu with a nice header"""
    print("\n" + "="*30)
    print("       PETTRACKER CLI")
    print("="*30)
    print("0. Exit Program")
    print("1. Manage Pets")      # Everything pet-related
    print("2. Manage Tasks")     # Everything task-related
    print("="*30) #visual separator for better readability
    

def pet_menu():
    """Sub-menu for all pet-related operations"""
    # Keep showing the pet menu until user goes back to main menu
    while True:
        print("\n--- PET MANAGEMENT ---")
        print("0. Back to Main Menu")    
        print("1. List All Pets")        
        print("2. Find Pet by ID")       
        print("3. Create a New Pet")     
        print("4. Delete a Pet")         
        print("5. View Tasks for a Pet") 
        
        choice = input("> ")
        
        # pet operations
        if choice == "0":
            # going back to the main menu
            break  # This exits the while loop, returning to main menu
        elif choice == "1":
            list_pets()           
        elif choice == "2":
            find_pet_by_id()      
        elif choice == "3":
            create_pet()          
        elif choice == "4":
            delete_pet()          
        elif choice == "5":
            view_pet_tasks()      
        else:
            print("Invalid choice.")  

def task_menu():
    """Sub-menu for all task-related operations"""
    # Keep showing task menu until user goes back
    while True:
        print("\n--- TASK MANAGEMENT ---")
        print("0. Back to Main Menu")      
        print("1. List All Tasks")         
        print("2. Find Task by ID")        
        print("3. Create a New Task")      
        print("4. Delete a Task")          
        print("5. Mark Task as Complete")  
        
        choice = input("> ")
        
        #task menu operations
        if choice == "0":
            break  
        elif choice == "1":
            list_tasks()            
        elif choice == "2":
            find_task_by_id()       
        elif choice == "3":
            create_task()           
        elif choice == "4":
            delete_task()           
        elif choice == "5":
            mark_task_complete()   
        else:
            print("Invalid choice.")  

# NB. this line makes sure the app only runs when we execute this file directly
if __name__ == "__main__":
    main()  