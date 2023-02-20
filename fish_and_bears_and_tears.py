import random


class ecosystem:
    # instance attributes, input of names of ecosystem, prey and predator
    def __init__(self, ecosystem, prey, predator):
        self.ecosystem = ecosystem
        self.prey = prey
        self.predator = predator

    #  instance methods
    #  this methods sets up the ecosystem:
        #  input of size of the ecosystem
        #  input number prey animals and number predators
    def __starting__(self, size_ecosystem, num_prey, num_predator):
        #  safe ecosystem variables for unleashing-method
        global ecosystem_setup
        global ecosystem_ongoing
        #  populate list based on the numeric inputs
        #  fill up remaining spaces as "free"
        ecosystem_setup =\
            [self.predator] * num_predator\
            + [self.prey] * num_prey\
            + ["free"] * (size_ecosystem - num_predator - num_prey)
        #  put list elements in random order
        random.shuffle(ecosystem_setup)
        #  create "ongoing" variable for subsequent method
        ecosystem_ongoing = ecosystem_setup
        #  print result
        print("The initial set-up is:", ecosystem_setup)
        return ecosystem_setup

    #  this method takes the set_up ecosystem
        #  runs it over as many time periods as defined by the user
    def __unleashing__(self, rounds=1):
        ecosystem_final = []
        #  for-loop for r rounds, default set to 1
        for r in range(rounds):
            #  choose animal to move based on random index
            random_index = random.randint(0, len(ecosystem_ongoing) - 1)
            moving_animal = ecosystem_ongoing[random_index]
            #  repeat if chosen index has no animal
            while moving_animal == "free":
                random_index = random.randint(0, len(ecosystem_ongoing) - 1)
                moving_animal = ecosystem_ongoing[random_index]
            #  provide animal
            print("The animal that was selected was a", moving_animal)
            #  define movement options for selected index
            #  first  and final positions have special movement
            #  no animal can move outside the ecosystem
            if random_index == len(ecosystem_ongoing):
                move = random.choice([-1, 0])
            elif random_index == 0:
                move = random.choice([0, 1])
            else:
                move = random.choice([-1, 0, 1])
            #  define non-movement
            if move == 0:
                print("This round, the animal did not move")
            #  define movement scenarios
            else:
                #  if intended index is empty: move
                if ecosystem_ongoing[random_index+move-1] == "free":
                    ecosystem_ongoing[random_index], ecosystem_ongoing[random_index+move] = \
                        ecosystem_ongoing[random_index+move], ecosystem_setup[random_index]
                    print("The animal moved to a free spot")
                #  define cases of animal meeting animal of same species
                elif ecosystem_ongoing[random_index+move-1] == ecosystem_ongoing[random_index]:
                    #  if no free space is left, no new animal spawns
                    if "free" not in ecosystem_ongoing:
                        print("No new animal could be added")
                    else:
                        #  Pick a random index
                        random_free_index = random.randint(
                            0, len(ecosystem_ongoing) - 1)
                        #  Repeat until free space is selected
                        while ecosystem_ongoing[random_free_index] != "free":
                            random_free_index = random.randint(
                                0, len(ecosystem_ongoing) - 1)
                        #  Once free space is found, add new animal
                        if ecosystem_ongoing[random_free_index] == "free":
                            ecosystem_ongoing[random_free_index] =\
                                ecosystem_ongoing[random_index]
                            print("A new", moving_animal, "was added")
                else:
                    #  describe meeting of predator and prey
                    ecosystem_ongoing[random_index+move-1] = self.predator
                    ecosystem_ongoing[random_index] = "free"
                    #  print("A predator ate a prey!")
                    print("A", self.predator, "ate a", self.prey)
            ecosystem_final.append(ecosystem_ongoing[:])
        #  provide resulting final ecosystem
        print("Final set-up:", ecosystem_final[-1])
        return ecosystem_final[-1]


#  applying class and both methods
#  ecosystem river with prey fish and predator bear
river = ecosystem("river", "fish", "bear")

#  test set-up
print("The", river.ecosystem, "has species",
      river.prey, "and", river.predator)

#  populate ecosystem as size 10, 5 prey animals and 3 predators
river_set_up = river.__starting__(10, 5, 3)

#  run this ecosystem for 5 time units
river_element_selected = river.__unleashing__(rounds=5)
