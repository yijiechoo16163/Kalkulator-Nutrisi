import pymysql

# Replace with your database credentials
host = 'sql6.freesqldatabase.com'
user = 'sql6695141'
password = 'XPi3U647s7'
database = 'sql6695141'

def insert_nutrient_info(conn, food_name, carbohydrate, protein, fat, total_calories):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Macronutrient_Info (food_name, carbohydrate, protein, fat, total_calories) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (food_name, carbohydrate, protein, fat, total_calories))
            conn.commit()
            print("Data inserted successfully!")
    except pymysql.Error as e:
        print(f"Error inserting data: {e}")

def calculate_total_calories(carbohydrate, protein, fat):
    try:
        total_calories = (carbohydrate * 4) + (protein * 4) + (fat * 9)
        return total_calories
    except ZeroDivisionError:
        print("Error: Macronutrient content cannot be zero.")
        return None

# Example usage:
is_continue = True
print("\n    NutCalc v1.0")
print("    Python Nutrition Calculator by Bernard Koo, Zin Him and Yi Jie\n")

while is_continue:
    food_name = input("\nEnter the name of the food: ")

    carbohydrate_input = False
    protein_input = False
    fat_input = False

    while not carbohydrate_input:
        carbohydrate = input("Please enter the carbohydrate content in grams: ")
        try:
            carbohydrate = float(carbohydrate)
            carbohydrate_input = True
        except ValueError:
            print("Input invalid. Please enter a valid number.")

    while not protein_input:
        protein = input("Please enter the protein content in grams: ")
        try:
            protein = float(protein)
            protein_input = True
        except ValueError:
            print("Input invalid. Please enter a valid number.")
    
    while not fat_input:
        fat = input("Please enter the fat content in grams: ")
        try:
            fat = float(fat)
            fat_input = True
        except ValueError:
            print("Input invalid. Please enter a valid number.")
    
    total_calories = calculate_total_calories(carbohydrate, protein, fat)
    if total_calories is not None:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        insert_nutrient_info(conn, food_name, carbohydrate, protein, fat, total_calories)
        conn.close()
        print(f"\nThe total calories for {food_name} are: {round(total_calories, 2)} calories.")

    is_continue_input = input("\nDo you want to continue? (y/N): ")
    if is_continue_input.lower() != "y":
        is_continue = False

print("\nThank you for using NutCalc v1.0. Goodbye!")
input("\nPress Enter to continue...")
