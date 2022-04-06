def remove(pantry, bad_food):
    pass

def display(pantry):
    for i in pantry:
        print(i)

def main():
    pantry = ['Bread', 'Eggs', 'Potatoes', 'Canned Green Beans']

    print("\nHello we are in need of some assistance with our pantry.")
    print("The canned green beans have gone bad and need to be removed.")

    bad_food = 'Canned Green Beans'

    remove(pantry, bad_food)
    print("\nUpdated pantry:")
    display(pantry)

if __name__ == "__main__":
    main()