is_continue = True
print("\n    NutCalc v1.0")
print("    Kalkulator Nutrisi oleh Bernard Koo, Zin Him dan Yi Jie\n")


while is_continue:
    carbohydrate_input = False
    protein_input = False
    fat_input = False
    is_continue_input = False

    while not carbohydrate_input:
        carbohydrate = input("\nSila masukkan kandungan karbohidrat dalam gram: ")
        try:
            carbohydrate = float(carbohydrate)
            carbohydrate_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")

    while not protein_input:
        protein = input("\nSila masukkan kandungan protein dalam gram: ")
        try:
            protein = float(protein)
            protein_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")
    
    while not fat_input:
        fat = input("\nSila masukkan kandungan lemak dalam gram: ")
        try:
            fat = float(fat)
            fat_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")
    
    total_calories = (carbohydrate * 4) + (protein * 4) + (fat * 9)
    print(f"\nJumlah kalori untuk kandungan makronutrien yang diberi adalah: {round(total_calories, 2)} kalori.")

    while not is_continue_input:
        is_continue_input = input("\nAdakah anda mahu teruskan? (y/T): ")
        if is_continue_input.lower() == "y":
            is_continue = True
            is_continue_input = True
        elif is_continue_input.lower() == "n" or is_continue_input == "":
            is_continue = False
            is_continue_input = True
        else:
            print("Input tidak sah. Sila masukkan 'y' untuk teruskan atau 'n' untuk keluar.")
            is_continue_input = False

print("\nTerima kasih kerana menggunakan NutCalc v1.0. Selamat tinggal!")
input("\nTekan Enter untuk teruskan...")
