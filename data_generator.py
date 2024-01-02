import random

def generate_array(elements:int=10) -> list:
    # Generate numbers from 1 to 1000
    return [random.randrange(1, 1000, 1) for i in range(elements)]

if __name__ == "__main__":
    print("Do not run this file!")