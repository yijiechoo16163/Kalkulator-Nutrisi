import pymysql

# Replace with your database credentials
host = 'sql6.freesqldatabase.com'
user = 'sql6695141'
password = 'XPi3U647s7'
database = 'sql6695141'

def insert_calories_to_db(conn, Makanan, Kebesaran_makanan, Kalori_makanan, Jumlah_calories):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Kalori_Makanan (Makanan, Kebesaran_makanan, Kalori_makanan, Jumlah_calories) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (Makanan, Kebesaran_makanan, Kalori_makanan, Jumlah_calories))
            conn.commit()
            print("Data inserted successfully!")
    except pymysql.Error as e:
        print(f"Error inserting data: {e}")

def calculate_calories(Makanan, Kebesaran_makanan, Kalori_makanan):
    try:
        Jumlah_calories = (Kebesaran_makanan / 100) * Kalori_makanan
        return Jumlah_calories
    except ZeroDivisionError:
        print("Error: Portion size cannot be zero.")
        return None

# Example usage:
Makanan = input("Enter the name of the food: ")
Kebesaran_makanan = float(input("Enter the portion size (in grams): "))
Kalori_makanan = float(input("Enter the calories per serving: "))

Jumlah_calories = calculate_calories(Makanan, Kebesaran_makanan, Kalori_makanan)
if Jumlah_calories is not None:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=database,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    insert_calories_to_db(conn, Makanan, Kebesaran_makanan, Kalori_makanan, Jumlah_calories)
    conn.close()
    print(f"{Makanan} ({Kebesaran_makanan} grams) contains approximately {Jumlah_calories:.2f} calories and has been added to the database.")
