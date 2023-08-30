import requests
import time

def get_random_recipe():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        
        if data.get("meals"):
            return data["meals"][0]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except ValueError as ve:
        print(f"Error decoding JSON: {ve}")
        return None
    
def display_recipe(recipe):
    if recipe:
        print(f"Recipe: {recipe['strMeal']}")
        print(f"Category: {recipe['strCategory']}")
        print("\nIngredients:")
        for i in range(1, 16):  # Maximum number of ingredients (can be edited)
            ingredient = recipe.get(f"strIngredient{i}")
            measurement = recipe.get(f"strMeasure{i}")
            if ingredient and measurement:
                print(f"{measurement.strip()} {ingredient.strip()}")
            else:
                break
        time.sleep(1.5)
        print("\nInstructions:")
        print("\n")
        instructions = recipe.get('strInstructions')
        if instructions:
            print(instructions.strip())
        else:
            print("Instructions unavailable.")
    else:
        print("No recipes found.")
        
def main():
    try:
        num_recipes = int(input("How many recipes would you like? "))
        time.sleep(1.5)
        if num_recipes <= 0:
            print("Please enter a positive integer.")
            return

        for _ in range(num_recipes):
            print("\nGenerating recipe...\n")
            time.sleep(2)
            random_recipe = get_random_recipe()
            display_recipe(random_recipe)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
