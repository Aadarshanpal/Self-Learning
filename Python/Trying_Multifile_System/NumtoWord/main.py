from GetInput import get_input
from MainLogic import logic
def main():
    num = get_input()
    word = logic(num)
    print(f"The word is: {word}")
    
if __name__ == "__main__" : main()
