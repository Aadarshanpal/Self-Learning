def get_input():
    while True:
        try:
            n = int(input("Enter Your guess: "))
            if n < 0 or n > 100:
                raise ValueError("The number is out of range 0-100")
            return n
        except ValueError as e:
            print(f"Error: {e}")