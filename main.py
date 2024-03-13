from datetime import datetime

def calculate_age(birth_year):
    actual_year = datetime.now().year
    return actual_year - birth_year

def generate_card(recipient, birth_year, message, sender):
    age = calculate_age(birth_year)
    birthday_card = f"{recipient}, wszystkiego naj, naj z okazji {age} urodzin!!!\n\n{message}\n\n{sender}"
    return birthday_card

def main():
    print("Wygenerujmy kartkę urodzinową.")
    recipient = input("Podaj imię odbiorcy: ")
    birth_year = int(input("Podaj rok urodzenia odbiorcy: "))
    message = input("Wpisz Twoją wiadomość dla odbiorcy: ")
    sender = input("Podaj swoje imię: ")
    birthday_card = generate_card(recipient, birth_year, message, sender)
    print("Oto Twoja kartka urodzinowa:\n")
    print(birthday_card)

if __name__ == "__main__":
    main()
