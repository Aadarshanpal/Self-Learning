import json



def main():
    while True:
        choice = int(input("1. Add expense\n2. View expenses\n3. Search expenses\n4. Show statistics\n5. Delete expense\n6. Save & exit"))
        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            search()

if __name__ == "__main__":
    main()
