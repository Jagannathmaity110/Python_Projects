import requests

def get_exchange_rate(from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()  # Ensure you call json() with parentheses
        if to_currency in data['rates']:
            return data['rates'][to_currency]
        else:
            raise ValueError(f"Currency code {to_currency} is not available.")
    else:
        raise Exception(f"Error fetching exchange rates: {response.status_code}")

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate

def main():
    try:
        from_currency = input("From Currency (e.g: USD): ").upper()  # Convert to uppercase
        to_currency = input("To Currency (e.g: EUR): ").upper()  # Convert to uppercase
        amount = float(input("Enter your amount: "))

        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
       