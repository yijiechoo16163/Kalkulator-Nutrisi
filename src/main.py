is_continue = True
print("\n    NutriCalc v1.0")
print("    Python Nutrition Calculator by Bernard Koo, Zin Him and Yi Jie\n")


while is_continue:
    carbohydrate_input = False
    protein_input = False
    fat_input = False
    is_continue_input = False

    while not carbohydrate_input:
        carbohydrate = input("\nPlease enter the carbohydrate content in grams: ")
        try:
            carbohydrate = float(carbohydrate)
            carbohydrate_input = True
        except ValueError:
            print("Input invalid. Please enter a valid number.")

    while not protein_input:
        protein = input("\nPlease enter the protein content in grams: ")
        try:
            protein = float(protein)
            protein_input = True
        except ValueError:
            print("Input invalid. Please enter a valid number.")
    
    while not fat_input:
        fat = input("\nPlease enter the fat content in grams: ")
        try:
            fat = float(fat)
            fat_input = True
        except ValueError:
            print("Input invalid. Please enter a valid number.")
    
    total_calories = (carbohydrate * 4) + (protein * 4) + (fat * 9)
    print(f"\nThe total calories for the given macronutrient content is: {round(total_calories, 2)} calories.")

    while not is_continue_input:
        is_continue_input = input("\nDo you want to continue? (y/N): ")
        if is_continue_input.lower() == "y":
            is_continue = True
            is_continue_input = True
        elif is_continue_input.lower() == "n" or is_continue_input == "":
            is_continue = False
            is_continue_input = True
        else:
            print("Invalid input. Please enter 'y' to continue or 'n' to exit.")
            is_continue_input = False

print("\nThank you for using NutriCalc v1.0. Goodbye!")
input("\nPress Enter to continue...")