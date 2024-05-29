spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
def get_names(spicy_foods):
    # Initialize an empty list to store the names of spicy foods
    food_names = []
    
    # Iterate through each food dictionary in the spicy_foods list
    for food in spicy_foods:
        # Append the name of the food to the food_names list
        food_names.append(food.get('name'))
    
    # Return the list of food names
    return food_names

def get_spiciest_foods(spicy_foods):
    # Initialize an empty list to store the spiciest foods
    spiciest_foods = []
    
    # Iterate through each food dictionary in the spicy_foods list
    for food in spicy_foods:
        # Check if the heat level of the food is greater than 5
        if food.get('heat_level', 0) > 5:
            # If it is, append the food dictionary to the spiciest_foods list
            spiciest_foods.append(food)
    
    # Return the list of spiciest foods
    return spiciest_foods

              

def print_spicy_foods(spicy_foods):
              for food in spicy_foods:
                    # Iterate through each food item in the spicy_foods list
                        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
                        # Print the name and cuisine of the food, along with a representation of its heat level using chili pepper emojis



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
        # Iterate through each food item in the list of spicy_foods
        if food.get('cuisine') == cuisine:
            # Check if the cuisine of the current food matches the given cuisine
            return food
            # If a match is found, return the current food dictionary

def print_spiciest_foods(spicy_foods):
     # Get only the spiciest foods with a heat level greater than 5
    spiciest_foods = get_spiciest_foods(spicy_foods)

    # Iterate through each spiciest food and print its name and heat level
    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    
    # Initialize total heat level
    total_heat_level = 0

    # Iterate through each spicy food in the list
    for food in spicy_foods:
        # Add the heat level of the current food to the total
        total_heat_level += food['heat_level']

    # Calculate the average heat level by dividing the total by the number of spicy foods
    average_heat = total_heat_level / len(spicy_foods)

    # Return the average heat level as an integer
    return int(average_heat)

def create_spicy_food(spicy_foods, new_spicy_food):
    # Append the new spicy food to the list of spicy foods
    spicy_foods.append(new_spicy_food)

    # Return the updated list of spicy foods
    return spicy_foods