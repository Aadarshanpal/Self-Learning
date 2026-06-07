def get_input():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
            break
        except ValueError as e:
            print(f"Error: {e}")
