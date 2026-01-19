from file_CRUD import *


holidays = load_holidays()
id_counter = 3

while True:
    print_info()
    ivestis = input()
    match ivestis:
        case "1":
           print_holidays(holidays)
        case "2":
           id_counter = create_holiday(holidays,id_counter)
        case "3":
           edit_holiday(holidays)
        case "4":
          remove_holiday(holidays)
        case "5":
            print('iseiti is programos')
            break