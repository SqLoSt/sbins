import requests
from termcolor import colored
from pyfiglet import Figlet
import os

def check_bin():
    os.system('clear')
    f = Figlet(font='big')
    heart = f.renderText('S-bins')
    print(colored(heart, 'green'))
    print(colored("Coded by SqLoSt / For Quatrox",'red'))
    print(colored("github.com/SqLoSt | Discord: SqLoSt#6660",'cyan'))
    input(colored("\n--- Press 'x' (any key) to continue --- ", 'red'))

    card_number = input("Please enter credit card number: ")
    url = f'https://lookup.binlist.net/{card_number[:6]}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country = data.get("country", {}).get("name", "")
        card_type = data.get("type", "")
        card_brand = data.get("brand", "")
        bank = data.get("bank", {}).get("name", "")
        scheme = data.get("scheme", "")
        prepaid = data.get("prepaid", False)
        length = data.get("number_length", {}).get("length", "")
        luhn = data.get("luhn", False)
        print(f'{colored("Country:", "red")} {colored(country, "green")}\n{colored("Card Type:", "red")} {colored(card_type, "green")}\n{colored("Card Brand:", "red")} {colored(card_brand, "green")}\n{colored("Issuer:", "red")} {colored(bank, "green")}\n{colored("Scheme:", "red")} {colored(scheme, "green")}\n{colored("Prepaid:", "red")} {colored(str(prepaid), "green")}\n{colored("Number Length:", "red")} {colored(str(length), "green")}\n{colored("Luhn Valid:", "red")} {colored(str(luhn), "green")}')
    else:
        print(colored("Invalid card number" , 'red'))

    choice = input("Do you want to check another card number? (y/n): ")
    if choice == 'y':
        check_bin()
    else:
        print(colored("Thanks for using S-bins." , 'magenta'))


check_bin()
