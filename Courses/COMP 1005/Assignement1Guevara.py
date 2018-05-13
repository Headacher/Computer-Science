#Assignment 1

def human_years():
    if dogorcat=="dog":
        print("Your pet is " + str(pet_age*7)  +" in human years!")
    else:
        print("Your pet is " + str(pet_age*5) + " in human years!")
    
def pet_life_stage():
    if dogorcat=="dog":
        if pet_age<=2:
            print("That means they're a puppy!")
        elif pet_age<=5:
            print("That means they're an adolescent.")
        elif(pet_age<=10):
            print("That means they're an adult.")
        else:
            print("That means they're a senior citizen!")
    else:
        if pet_age<=1:
            print("That means they're a kitty!")
        elif pet_age<=7:
            print("That means they're an adolescent.")
        elif pet_age<=12:
            print("That means they're an adult.")
        else:
            print("That means they're a senior citizen!")

def kilograms_to_pounds():
    print(pet_name + " is " + str(pet_weight/2.204) + " kilograms heavy!")
    
def inches_to_centimeters():
    print(pet_name + " is " + str(pet_height/0.393) + " centimeters tall!")

def km_to_miles():
    print(pet_name + " can run " + str(pet_speed/0.621) + " kilometers an hour!")

dogorcat = input("Hello! Is your pet a cat or a dog?")

if dogorcat == "cat" or  dogorcat == "dog":
    
    pet_name = input("What's their name?")
    
    print("Welcome " + dogorcat + " owner! I'm going to ask you some quetions about " + pet_name)
    
    pet_age = int(input("How old is your pet in years?"))
    pet_weight = int(input("What is its weight in pounds?"))
    pet_height = int(input("What is its height in inches?"))
    pet_speed = int(input("How many miles can it run in an hour?"))
    
    human_years()
    pet_life_stage()
    kilograms_to_pounds()
    inches_to_centimeters()
    km_to_miles()
    
            
    
    
    print("That's all I can say about " + pet_name + " the " + dogorcat + ".")
    
else:
    print("Sorry, I can only tell you about cats or dogs.")
    