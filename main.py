holidays = [
            {
                'id': 1,
                "country":"Lithuania",
                "city":"Palanga",
                "price":20.0,
                "accomodation":"hotel"
            },
            {
                'id': 2,
                "country":"Turkija",
                "city":"Alanya",
                "price":60.0,
                "accomodation":"hostel"
            },
            {
                'id': 3,
                "country":"Cyprus",
                "city":"Larnaka",
                "price":70.0,
                "accomodation":"apartaments"
            }
        ]
id_counter = 3
while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    ivestis = input()
    match ivestis:
        case "1":
            for hol in holidays:
                print(f'{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} '
                      f'parai {hol['price']} eurų.')
        case "2":
            print('atostogu itraukimas:')
            print("iveskite sali")
            country = input()
            print("iveskite miesta")
            city = input()
            print('iveskite apgyveninimo tipa')
            accom = input()
            print('iveskite kaina')
            price = float(input())
            id_counter += 1
            hol = {
                'id':id_counter,
                'country': country,
                'city': city,
                'accomodation': accom,
                'price': price
            }
            holidays.append(hol)
        case "3":
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
        case "4":
            print('atostogu salinimas')
            print("iveskite id atostogu kurias norite pasalinti")
            del_id = input()
            for hol in holidays:
                if del_id == str(hol['id']):
                    print(f'{hol['id']}. Šalinama: Atostogos {hol['country']} {hol['city']}. Kaina gy'
                           f'venant {hol['accomodation']} parai {hol['price']} eurų.')
                    holidays.remove(hol)
                    # alternatyva salinimui
                    # hol_pos_in_list = holidays.index(hol)
                    # del holidays[hol_pos_in_list]
        case "5":
            print('iseiti is programos')
            break

#apgyvendinimo tipu priverstinis pasirinkimas is menu optionu
# opts = ['hotel','hostel','camping']
# for i, val in enumerate(opts):
#     print(f'{i+1}. {val}')
# inp = int(input())
# print(opts[inp-1])