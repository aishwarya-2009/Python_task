
# main.py
from shop import weight_calc

def main():
    try:
        widgets = int(input("Enter the number of widgets: "))
        gizmos = int(input("Enter the number of gizmos: "))
        total_weight = weight_calc.calculate_total_weight(widgets, gizmos)
        print(f"The total weight of the order is {total_weight} grams.")
    except ValueError:
        print("Please enter valid integers for the number of widgets and gizmos.")

if __name__ == "__main__":
    main()

