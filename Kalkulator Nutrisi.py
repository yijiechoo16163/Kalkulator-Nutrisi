import pymysql

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
            print("Data dimasukkan dengan berjaya!")
    except pymysql.Error as e:
        print(f"Ralat memasukkan data: {e}")

def calculate_total_calories(carbohydrate, protein, fat):
    try:
        total_calories = (carbohydrate * 4) + (protein * 4) + (fat * 9)
        return total_calories
    except ZeroDivisionError:
        print("Ralat: Kandungan Makronutrien tidak boleh sifar.")
        return None

is_continue = True
print("\n    NutCalc v1.0")
print("    Kalkulator Nutrisi Python oleh Bernard Koo, Zin Him, dan Yi Jie\n")

while is_continue:
    food_name = input("\nMasukkan nama makanan: ")

    carbohydrate_input = False
    protein_input = False
    fat_input = False

    while not carbohydrate_input:
        carbohydrate = input("Sila masukkan kandungan karbohidrat dalam gram: ")
        try:
            carbohydrate = float(carbohydrate)
            carbohydrate_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")

    while not protein_input:
        protein = input("Sila masukkan kandungan protein dalam gram: ")
        try:
            protein = float(protein)
            protein_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")
    
    while not fat_input:
        fat = input("Sila masukkan kandungan lemak dalam gram: ")
        try:
            fat = float(fat)
            fat_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")
    
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
        print(f"\nJumlah kalori untuk {food_name} adalah: {round(total_calories, 2)} kalori.")

    is_continue_input = input("\nAdakah anda mahu teruskan? (y/T): ")
    if is_continue_input.lower() != "y":
        is_continue = False

print("\nTerima kasih kerana menggunakan NutCalc v1.0. Selamat tinggal!")
input("\nTekan Enter untuk teruskan...")
