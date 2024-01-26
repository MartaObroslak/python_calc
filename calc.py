# Prosty kalkulator w Pythonie

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd: Nie można dzielić przez zero!"

print("Witaj w prostym kalkulatorze!")

while True:
    print("Wybierz działanie:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Zakończ")

    wybor = input("Wybierz opcję (1/2/3/4/5): ")

    if wybor == '5':
        break

    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        print("Wynik dodawania:", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print("Wynik odejmowania:", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print("Wynik mnożenia:", mnozenie(liczba1, liczba2))
    elif wybor == '4':
        print("Wynik dzielenia:", dzielenie(liczba1, liczba2))
    else:
        print("Niepoprawny wybór. Wybierz opcję od 1 do 5.")
