def menu():
    print("\n""1. enter product.")
    print("2. show inventory.")
    print("3. calculate statistics.")
    print("4. leave.""\n")
    try:
        option = int (input("Enter your option: "))
        if option in (1,4):
            print(f"Select option {option}.")
        else:
            print(f"Dont exist option {option}, try again")
            menu()
    except ValueError:
        print("Error try again and select a valid option")
        menu()