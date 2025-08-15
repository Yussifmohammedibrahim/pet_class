class car:
    def __init__(self, name, model , horsepower, engine_type):
        self.name = name
        self.model = model
        self.horsepower = horsepower
        self.engine = engine_type

    def display_info(self):
        print(f" -------car information--------- ")
        print(f'name : {self.name}')
        print(f"model : {self.model}")
        print(f'horsepower : {self.horsepower}')
        print(f'engine_type: {self.engine}')

        return f"car name : {self.name} , model : {self.model} , horsepower : {self.horsepower} , engine_type : {self.engine}"
     
    def update_horsepower(self, new_horsepower):
        if isinstance(new_horsepower, int) and new_horsepower > 0:
            self.horsepower = new_horsepower
            print(f"{self.name}'s horsepower updated to {new_horsepower}")
        else:
            print("Invalid horsepower! Horsepower must be a positive integer.")

truck = car("lambogirni" , "2025 model" , 457 , "6gen") 
print(truck.display_info())

truck.update_horsepower(500)
print(truck.display_info())    