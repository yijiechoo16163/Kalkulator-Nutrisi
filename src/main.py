"""
This script calculates the total calories based on the user's input of carbohydrate, protein, and fat content.
It prompts the user to enter the values for each macronutrient and validates the input.
After calculating the total calories, it asks the user if they want to continue or exit.
"""

is_continue = True
print("\n    NutCalc v1.0")
print("    Kalkulator Nutrisi oleh Bernard Koo, Zin Him dan Yi Jie\n")

# Main loop to continue or exit the program
while is_continue:
    # Variable to check if user input is valid
    # Before any user input, consider all inputs as invalid
    carbohydrate_input = False
    protein_input = False
    fat_input = False
    is_continue_input = False

    # Get user input for carbohydrate, protein and fat content

    # Ask user to input carbohydrate content in grams
    while not carbohydrate_input:
        carbohydrate = input("\nSila masukkan kandungan karbohidrat dalam gram: ")

        # Try to convert user input to float
        try:
            carbohydrate = float(carbohydrate)
            carbohydrate_input = True

        # If user input cannot be converted to float, print error message
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")

    # Ask user to input protein content in grams
    while not protein_input:
        protein = input("\nSila masukkan kandungan protein dalam gram: ")

        # Try to convert user input to float
        try:
            protein = float(protein)
            protein_input = True

        # If user input cannot be converted to float, print error message
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")

    # Ask user to input fat content in grams
    while not fat_input:
        fat = input("\nSila masukkan kandungan lemak dalam gram: ")

        # Try to convert user input to float
        try:
            fat = float(fat)
            fat_input = True

        # If user input cannot be converted to float, print error message
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang sah.")

    # Calculate total calories based on user input
    total_calories = (carbohydrate * 4) + (protein * 4) + (fat * 9)

    # Print total calories to user
    print(f"\nJumlah kalori untuk kandungan makronutrien yang diberikan ialah: {round(total_calories, 2)} kalori.")

    # Ask user if they want to continue
    while not is_continue_input:
        is_continue_input = input("\nAdakah anda mahu meneruskan? (y/N):")

        # If user input is 'y', continue the loop
        if is_continue_input.lower() == "y":
            is_continue = True
            is_continue_input = True

        # If user input is 'n' or empty, exit the loop
        elif is_continue_input.lower() == "n" or is_continue_input == "":
            is_continue = False
            is_continue_input = True

        # If user input is neither 'y' nor 'n', print error message
        else:
            print("Input tidak sah. Sila masukkan 'y' untuk meneruskan atau 'n' untuk keluar.")
            is_continue_input = False

# Print goodbye message
print("\nTerima kasih kerana menggunakan NutCalc v1.0. selamat tinggal!")
# Wait for user to press Enter to exit
input("\nTekan Enter untuk meneruskan...")
