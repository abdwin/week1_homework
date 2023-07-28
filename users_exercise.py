users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# option 1 - standard drilldown - opted to setup a function although I realise not needed
def get_handle(user):
    print(users[user]["twitter"]
# get_handle("Jonathan")
# option 2 - use dictionary get method - nesting gets
print(users.get("Jonathan").get("twitter"))

# 2. Get Erik's hometown
# option 1 - standard drilldown - opted to setup a function although I realise not needed
def get_hometown(user):
    print(users[user]["home_town"])
# get_hometown("Erik")
# option 2 - use dictionary get method - nesting gets
print(users.get("Erik").get("home_town"))

# 3. Get the list of Erik's lottery numbers
# option 1 - standard drilldown - opted to setup a function although I realise not needed
def get_lottery(user):
    print(users[user]["lottery_numbers"])
# get_lottery("Erik")
# option 2 - use dictionary get method - nesting gets
print(users.get("Erik").get("lottery_numbers"))

# 4. Get the species of Avril's pet Monty
# option 1 - standard for item in list, if the right pet, print species
def get_species(user, pet_name):
    for pet in users[user]["pets"]:
      if pet["name"] == pet_name:
        print(pet["species"])
# get_species("Erik", "kevin")
# option 2 - similar but with dictionary get method to return the list, if the right pet, print species
for pet in users.get("Erik").get("pets"):
   if pet.get("name") == "kevin":
    print(pet.get("species"))
  

# 5. Get the smallest of Erik's lottery numbers
# option 1 - list sort method and then using index to pick out smallest
def get_small_number(user):
  #  users[user]["lottery_numbers"].sort()
  #  print(users[user]["lottery_numbers"][0])
# get_small_number("Erik")
# option 2 - use min() method
  print(min(users[user]["lottery_numbers"]))
  
# 6. Return an list of Avril's lottery numbers that are even
# option 1 - for loop with if conditional - using % operator to find evens, sorted it as well
def get_even(user):
  evens = []
  for number in users[user]["lottery_numbers"]:
    if number % 2 == 0:
      evens.append(number)
  evens.sort()
  print(evens)
  # get_even("Avril")
# option 2 - you can create a new list whilst running through an existing list with a condition!
evens = [num for num in users[user]["lottery_numbers"] if (num % 2) == 0]
  print(evens)
# option 3 - you can create a new list whilst running through an existing list with a condition!
# But this time using dictionary get method to return the existing list
evens = [num for num in users.get("Avril").get("lottery_numbers") if (num % 2) == 0]
print(evens)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# list append method. 
def add_lottery_number(user, number):
  users[user]["lottery_numbers"].append(number)
  print(users[user]["lottery_numbers"])
# add_lottery_number("Erik", 7)

# 8. Change Erik's hometown to Edinburgh
# standard reassign
def change_hometown(user, hometown):
    users[user]["home_town"] = hometown
    print(users[user]["home_town"])
# change_hometown("Erik", "Edinburgh")

# 9. Add a pet dog to Erik called "fluffy"
# standard append method
def add_pet(user, petname, petspecies):
  users[user]["pets"].append({"name" : petname, "species" : petspecies})
  print(users[user]["pets"])
# add_pet("Erik", "fluffy", "dog")

# 10. Add another person to the users dictionary
# standard update method
users.update(
  {"Alan": {
    "twitter": "allyballyb",
    "lottery_numbers": [5, 10, 15, 20, 25, 30],
    "home_town": "Glasgow",
    "pets": [
    {
      "name": "luna",
      "species": "cat"
    },
    {
      "name": "leia",
      "species": "cat"
    }
  ]
  }
  }
  )
# print(users)