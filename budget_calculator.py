# budget_calculator.py

def main():
    print("--- Monthly Budget Calculator ---")
    
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        # Ask for multiple expenses
        expenses = []
        print("Enter your expenses one by one. Type 'done' to finish.")
        while True:
            entry = input("Enter expense (or 'done'): ").strip().lower()
            if entry == 'done':
                break
            try:
                expense = float(entry)
                expenses.append(expense)
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
        
        # Calculate total expenses and remaining balance
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses
        
        # Display results
        print("\n--- Summary ---")
        print(f"Total Budget:     {total_budget:.2f} LKR")
        print(f"Total Expenses:   {total_expenses:.2f} LKR")
        print(f"Remaining Balance: {remaining_balance:.2f} LKR")
        
        if remaining_balance < 0:
            print("Warning: You are over budget!")
        elif remaining_balance < 500:
            print("Warning: Low Funds")
        else:
            print("You are within your budget.")

    except ValueError:
        print("Error: Please enter valid numerical values for budget and expenses.")

if __name__ == "__main__":
    main()
