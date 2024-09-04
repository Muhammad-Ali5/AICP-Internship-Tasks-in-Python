# Task 1: Input and store the weights and names for pupils
def input_pupil_data(num_pupils=3):
    names = []
    weight_first_day = []
    
    for i in range(num_pupils):
        name = input(f"Enter the name of pupil {i+1}: ")
        while True:
            try:
                weight = float(input(f"Enter the weight of {name} on the first day of term (in kg): "))
                if weight <= 0 or weight >= 80:
                    print("Invalid weight. You are not eligible!")
                else:
                    break
            except ValueError:
                print("Invalid input... Please enter a number...")
        
        names.append(name)
        weight_first_day.append(weight)
    return names, weight_first_day

# Task 2: Calculate weight differences
def calculate_weight_differences(names, weight_first_day):
    weight_last_day = []
    weight_difference = []
    for i, name in enumerate(names):
        while True:
            try:
                weight = float(input(f"Enter the weight of {name} on the last day of term (in kg): "))
                if weight <= 0 or weight >= 80:
                    print("Invalid weight. You are not eligible!")
                else:
                    break
            except ValueError:
                print("Invalid input... Please enter a number...")
        weight_last_day.append(weight)
        weight_difference.append(weight - weight_first_day[i])
    
    return weight_difference

# Task 3: Output pupils with a difference in weight greater than 2.5 kg
def output_significant_changes(names, weight_differences):
    for i, difference in enumerate(weight_differences):
        if abs(difference) > 2.5:
            if difference > 0:
                print(f"{names[i]} gained {difference:.2f} kg.")
            else:
                print(f"{names[i]} lost {abs(difference):.2f} kg.")

# Main function to run all tasks
def main():
    names, weight_first_day = input_pupil_data()
    weight_differences = calculate_weight_differences(names, weight_first_day)
    output_significant_changes(names, weight_differences)

if __name__ == "__main__":
    main()
