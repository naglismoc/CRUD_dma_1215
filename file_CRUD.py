import csv

headers = ['id','country','city','price','accomodation']
def load_holidays():
    with open('.accomodations.csv',mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))
def save_holidays(holidays):
    with open("accomodations.csv",mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(holidays)

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")

def print_holidays(holidays):
    for hol in holidays:
        print(f'{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} '
              f'parai {hol['price']} eurų.')


def create_holiday(holidays,id_counter):
    print('atostogu itraukimas:')
    print("iveskite sali")
    country = input()
    print("iveskite miesta")
    city = input()
    print('iveskite apgyveninimo tipa')
    accom = input()
    print('iveskite kaina')
    price = float(input())
    id_counter = int(holidays[-1]['id']) + 1 if len(holidays) > 0 else 1
    hol = {
        'id': id_counter,
        'country': country,
        'city': city,
        'accomodation': accom,
        'price': price
    }
    holidays.append(hol)
    save_holidays(holidays)
    return id_counter


def edit_holiday(holidays):
    print('atostogu redagavimas')
    print("iveskite id atostogu kurias norite redaguoti")
    edit_id = input()
    for hol in holidays:
        if edit_id == str(hol['id']):
            print(f'{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} '
                  f'parai {hol['price']} eurų.')
            print("iveskite sali")
            hol['country'] = input()
            print("iveskite miesta")
            hol['city'] = input()
            print('iveskite apgyveninimo tipa')
            hol['accomodation'] = input()
            print('iveskite kaina')
            hol['price'] = float(input())
    save_holidays(holidays)

def remove_holiday(holidays):
    print('atostogu salinimas')
    print("iveskite id atostogu kurias norite pasalinti")
    del_id = input()
    for hol in holidays:
        if del_id == str(hol['id']):
            print(f'{hol['id']}. Šalinama: Atostogos {hol['country']} {hol['city']}. Kaina gy'
                  f'venant {hol['accomodation']} parai {hol['price']} eurų.')
            holidays.remove(hol)
    save_holidays(holidays)