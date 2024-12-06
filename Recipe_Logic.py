import sqlite3 as lite
import csv

class Recipe:
    def __init__(self, name, ingredients, instructions, meal_type, veg_status, prep_time):
        self.name = name
        self.ingredients = ingredients  # list of ingredients in the recipe
        self.instructions = instructions  # list of instructions
        self.meal_type = meal_type  # string telling you what type of meal this is
        self.veg_status = veg_status  # bool flag showing whether recipe is vegan or not
        self.prep_time = prep_time  # int telling you how long the recipe will take to make in minutes
def match_ingredients(ingredients, recipes):
    ingredients_list = ingredients.split(',')

recipesDatabase = lite.connect('foodDatabase.db')
repCur = recipesDatabase.cursor()

def get_recipes():
    recipe_sql = """" 
                    SELECT 
                        r.recipe_name,
                        r.instructions,
                        r.ingredients,
                        r.meal_type,
                        r.veg_status,
                        r.prep_time AS duration
                    FROM 
                        Recipes AS r
                    JOIN 
                        Recipe_Ingredients AS ri ON r.recipe_id = ri.recipe_id
                    JOIN
                        Ingerdients AS i ON ri.ingredient_id = i.ingredient_id
                    GROUP BY 
                        r.recipe_name,r.instructions,r.ingredients,r.meal_type,r.veg_status,r.prep_time
                """""
    repCur.execute(recipe_sql)
    recipes = repCur.fetchall()
    return recipes

def extract_ingredients():
    ingredients = []
    with open('ENTER_CSV_FILE.csv',mode = 'r') as file: # don't have the csv file yet
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            ingredients.extend(row)
    return ingredients # returns a list of all ingredients


