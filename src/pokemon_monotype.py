import numpy as np

TYPE = ["Fire", "Water", "Grass"]


PAYOFF_MATRIX = [   # vs Fire,  vs Water,   vs Grass
                    [1,         0,          2], # Fire
                    [2,         1,          0], # Water
                    [0,         2,          1]  # Grass
] # Winner takes all payoff matrix

class Pokemon_monotype:
    def __init__(self, type):
        self.type = type
        self.age = 0
        self.berries = 0

    def __str__(self):
        return self.type

    def __eq__(self, other):
        return self.type == other.type
    
    def battle(self, other):
        if self.age == 0:
            self.berries = PAYOFF_MATRIX[TYPE.index(self.type)][TYPE.index(other.type)]
            self.age += 1
            print(f"{self} won {self.berries} berries")
            other.battle(self)

    def get_berries(self):
        return self.berries
    
    def set_berries(self, berries):
        self.berries = berries


class Pokemon_monotype_population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.steps = 0
        for i in range(0,size):
            self.population.append(Pokemon_monotype(TYPE[i % 3]))
        np.random.shuffle(self.population)

    def __str__(self):
        return str([str(pokemon) for pokemon in self.population])

    def __eq__(self, other):
        return self.population == other.population

    def battle(self):
        print(self)
        for i in range(0,len(self.population)-1,2):
            self.population[i].battle(self.population[i+1]) 
        if len(self.population) % 2 != 0:
            self.population[-1].set_berries(2)    
    
    def reproduce(self):
        new_population = []
        for type in TYPE:
            for _ in range(0, int(self.berries_per_type(type))):
                new_population.append(Pokemon_monotype(type))
        self.population = new_population
        np.random.shuffle(self.population)
                    
    def berries_per_type(self,type):
        berries = 0
        for pokemon in self.population:
            if pokemon.type == type:
                berries += pokemon.get_berries()
        print(f"{type} has {berries} berries")
        return berries
    
    def step(self):
        self.battle()
        self.reproduce()
        print(self.get_population_size())
        self.steps += 1

    def run(self, steps):
        for _ in range(0,steps):
            self.step()
    
    def get_population(self):
        return self.population
    
    def get_population_size(self):
        return len(self.population)
    
    def get_population_per_type_size(self, type):
        return len([pokemon for pokemon in self.population if pokemon.type == type])

    def get_steps(self):
        return self.steps
    
population = Pokemon_monotype_population(10)
print(population)
population.step()
print(population)
print("Fire", population.get_population_per_type_size("Fire"))
print("Water", population.get_population_per_type_size("Water"))
print("Grass", population.get_population_per_type_size("Grass"))