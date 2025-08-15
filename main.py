class Pet:
    """
    A class to represent a pet in a management system.
    
    Attributes:
        name (str): Name of the pet
        pet_type (str): Type of pet (e.g., Dog, Cat)
        age (int): Age of the pet in years
    """
    
    def __init__(self, name: str, pet_type: str, age: int):
        """
        Constructor to initialize pet attributes
        
        Args:
            name: Name of the pet
            pet_type: Type of pet
            age: Age in years
        """
        self.name = name
        self.pet_type = pet_type
        self.age = age
    
    def display_info(self) -> None:
        """Displays all information about the pet in a formatted way"""
        print("\n Pet Information:")
        print(f"Name: {self.name}")
        print(f"Type: {self.pet_type}")
        print(f"Age: {self.age} years")
    
    def update_age(self, new_age: int) -> None:
        """
        Updates the pet's age with validation
        
        Args:
            new_age: New age value (must be positive integer)
        """
        if isinstance(new_age, int) and new_age > 0:
            self.age = new_age
            print(f"{self.name}'s age updated to {new_age}")
        else:
            print("Invalid age! Age must be a positive integer.")

# Demonstration
if __name__ == "__main__":
    print(" Pet Management System ")
    print("-" * 30)
    
    # Create pet instances
    pet1 = Pet("Buddy", "Dog", 3)
    pet2 = Pet("Whiskers", "Cat", 5)
    
    # Display initial info
    pet1.display_info()
    pet2.display_info()
    
    # Update age and show changes
    print("\nUpdating Buddy's age...")
    pet1.update_age(4)
    
    print("\nAfter Update:")
    pet1.display_info()