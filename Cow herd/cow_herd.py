def record_yield():
    herd_size = int(input("Enter the number of cows in the herd: "))
    herd_data = {}
    
    for _ in range(herd_size):
        cow_id = input("Enter cow's 3-digit ID: ")
        if cow_id in herd_data:
            print("Cow ID already exists. Please enter a unique ID.")
            continue

        herd_data[cow_id] = []

        for day in range(7):
            for milking in range(2):
                while True:
                    try:
                        yield_value = float(input(f"Enter the yield for cow {cow_id} on day {day+1}, milking {milking+1}: "))
                        herd_data[cow_id].append(round(yield_value, 1))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

    return herd_data

def calculate_statistics(herd_data):
    total_yield = 0
    num_cows = len(herd_data)
    
    for cow_id, yields in herd_data.items():
        total_yield += sum(yields)
    
    average_yield = total_yield / num_cows
    
    print(f"Total weekly milk yield for the herd: {round(total_yield)} litres")
    print(f"Average weekly milk yield per cow: {round(average_yield)} litres")

def identify_cows(herd_data):
    max_yield = 0
    best_cow_id = None
    low_yielding_cows = []
    
    for cow_id, yields in herd_data.items():
        weekly_yield = sum(yields)
        
        # Identify the most productive cow
        if weekly_yield > max_yield:
            max_yield = weekly_yield
            best_cow_id = cow_id
        
        # Identify cows with yield < 12 litres for 4 or more days
        low_yield_days = sum(1 for yield_value in yields if yield_value < 12)
        if low_yield_days >= 4:
            low_yielding_cows.append(cow_id)
    
    print(f"Most productive cow: {best_cow_id} with a yield of {round(max_yield)} litres in the week.")
    
    if low_yielding_cows:
        print("Cows with yield less than 12 litres on four or more days:")
        for cow_id in low_yielding_cows:
            print(f"Cow ID: {cow_id}")
    else:
        print("No cows produced less than 12 litres of milk on four or more days.")

# Example of running the full program
herd_data = record_yield()
calculate_statistics(herd_data)
identify_cows(herd_data)
