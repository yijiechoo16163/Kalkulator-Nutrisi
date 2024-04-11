# Atur cara bagi program kalkulator nutrisi

is_continue = True  # Flag untuk mengawal sama ada program meneruskan berjalan atau tidak
print("\n    NutCalc v1.0")  # Cetak tajuk program
print("    Kalkulator Nutrisi oleh Bernard Koo, Zin Him, Yi Jie dan Matthew\n")  # Cetak penulis program


while is_continue:  # Permulaan paksi utama
    carbohydrate_input = False  # Flag untuk mengawal pengesahan input karbohidrat
    protein_input = False  # Flag untuk mengawal pengesahan input protein
    fat_input = False  # Flag untuk mengawal pengesahan input lemak
    is_continue_input = False  # Flag untuk mengawal pengesahan input teruskan

    # Loop pengesahan input karbohidrat
    while not carbohydrate_input:
        carbohydrate = input("\nSila masukkan kandungan karbohidrat dalam gram: ")
        try:
            carbohydrate = float(carbohydrate)
            carbohydrate_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")

    # Loop pengesahan input protein
    while not protein_input:
        protein = input("\nSila masukkan kandungan protein dalam gram: ")
        try:
            protein = float(protein)
            protein_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")
    
    # Loop pengesahan input lemak
    while not fat_input:
        fat = input("\nSila masukkan kandungan lemak dalam gram: ")
        try:
            fat = float(fat)
            fat_input = True
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")
    
    # Kiraan jumlah kalori
    total_calories = (carbohydrate * 4) + (protein * 4) + (fat * 9)
    print(f"\nJumlah kalori untuk kandungan makronutrien yang diberi adalah: {round(total_calories, 2)} kalori.")

    # Loop pengesahan input teruskan
    while not is_continue_input:
        is_continue_input = input("\nAdakah anda mahu teruskan? (y/T): ")
        if is_continue_input.lower() == "y":
            is_continue = True
            is_continue_input = True
        elif is_continue_input.lower() == "t" or is_continue_input == "":
            is_continue = False
            is_continue_input = True
        else:
            print("Input tidak sah. Sila masukkan 'y' untuk teruskan atau 't' untuk keluar.")
            is_continue_input = False

print("\nTerima kasih kerana menggunakan NutCalc v1.0. Selamat tinggal!")  # Cetak mesej keluar
input("\nTekan Enter untuk teruskan...")  # Tunggu input pengguna sebelum keluar
