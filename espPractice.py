import pandas as pd
import matplotlib.pyplot as plt

fileLoop = True
while fileLoop:
    try:
        df = pd.read_csv("Task4a_RBSX_data.csv")

    except FileNotFoundError:
        print("File not found\nPlease download the file -> Task4a_RBSX_data.csv")

    else:
        fileLoop = False

def get_int_in_range(prompt, low, high):
    while True:
        raw = input(prompt)
        try:
            value = (int(raw))
        
        except ValueError:
            print("Please enter whole number")
            continue
        
            if value < low or value > high:
                print(f"Please enter a number between {low} and {high}")
                continue
        
        return value

def menu():
    flag = True
    while flag:
        print("\n------------------------------------------------------")
        print("RBSX Currency Tool - what would you like to do?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling (GBP)")
        print("3. Pound (GBP) to Australian Dollars (AUD)")
        print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("7. View trends of GBP against other currencies")
        print("8. View performance of a selected currency (graph)")
        print("9. Exit the program")
        print("------------------------------------------------------\n")
        
        menu_choice = get_int_in_range("Please enter the number of your choice (1-9): ", 1, 9)
        flag = False
    return menu_choice


def get_currency():
    currencies = {
    '1': 'GBP - EUR',
    '2': 'EUR - GBP',
    '3': 'GBP - AUD',
    '4': 'AUD - GBP',
    '5': 'GBP - JPY',
    '6': 'JPY - GBP'
    }

    currency = currencies.get(menu_choice)
    return currency


def get_conversion_rate():
    conversion_rate = round(df[currency].iloc[-1], 2)
    return conversion_rate


def get_amount_to_convert():
    print("You are converting:", currency)
    flag = True
    while flag:
        conversion_amount = input("Please enter the amount you wish to convert: ")
        try:
            value = float(conversion_amount)
        
        except ValueError:
            print("Sorry, you must enter a numerical value")
            flag = True
        
        else:
            if value < 0:
                print("Sorry, the amount cannot be a negative number")
                flag = True
            
            else:
                return conversion_amount


def perform_conversion():
    amount_received = round(conversion_amount * conversion_rate, 2)
    print("\n----------------------------------")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]))
    print('You will receive {} in {}'.format(amount_received, currency[6:9]))
    print("----------------------------------\n")


def show_gbp_trends():
    print("\n------------------------------------------------------")
    print("Trends of GBP against other currencies (last 12 weeks)")
    print("------------------------------------------------------\n")

    gbp_columns = ['GBP - EUR', 'GBP - AUD', 'GBP - JPY']

    for col in gbp_columns:
        highest = round(df[col].max(), 4)
        lowest = round(df[col].min(), 4)
        average = round(df[col].mean(), 4)
        start_rate = df[col].iloc[0]
        end_rate = df[col].iloc[-1]

    if end_rate > start_rate:
        direction = "increased"

    elif end_rate < start_rate:
        direction = "decreased"

    else:
        direction = "stayed the same"

    print(f"\n--- {col} ---")
    print(f"Highest rate: {highest}")
    print(f"Lowest rate: {lowest}")
    print(f"Average rate: {average}")
    print(f"Overall the rate has {direction} from {round(start_rate, 4)} to {round(end_rate, 4)}")
    print("------------------------------------------------------\n")


def show_performance():
    print("\n------------------------------------------------------")
    print("Which currency pair would you like to see the performance of?")
    print("1. GBP - EUR")
    print("2. GBP - AUD")
    print("3. GBP - JPY")
    print("------------------------------------------------------\n")

    choice = get_int_in_range("Please enter your choice (1-3): ", 1, 3)
    pair_options = {1: 'GBP - EUR', 2: 'GBP - AUD', 3: 'GBP - JPY'}
    pair = pair_options.get(choice)

    start_rate = df[pair].iloc[0]
    end_rate = df[pair].iloc[-1]
    change = end_rate - start_rate
    percent_change = round((change / start_rate) * 100, 2)

    print("")
    print(f"Performance for {pair}:")
    print(f"Start rate: {round(start_rate, 4)}")
    print(f"End rate: {round(end_rate, 4)}")
    print(f"Change: {round(change, 4)}")
    print(f"Percentage change: {percent_change}%")

    if percent_change > 0:
        print("This currency pair has gone UP over the period.")
    
    elif percent_change < 0:
        print("This currency pair has gone DOWN over the period.")
    
    else:
        print("This currency pair has not changed over the period.")

    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df[pair], color='blue')
    plt.title("Performance of " + pair + " over the last 12 weeks")
    plt.xlabel("Date")
    plt.ylabel("Conversion rate")
    plt.xticks(df['Date'][::7], rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("grapho")


running = True
while running:
    menu_choice = menu()

    if menu_choice in [1, 2, 3, 4, 5, 6]:
        currency = get_currency()
        conversion_rate = get_conversion_rate()
        conversion_amount = float(get_amount_to_convert())
        perform_conversion()

    elif menu_choice == 7:
        show_gbp_trends()

    elif menu_choice == 8:
        show_performance()

    elif menu_choice == 9:
        print("\n------------------------------------------------------")
        print("Thank you for using the RBSX Currency Tool")
        print("------------------------------------------------------\n")
        running = False