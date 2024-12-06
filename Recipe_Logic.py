import sqlite3 as lite
import csv

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


