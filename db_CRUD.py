# pip install mysql-connector-python
# pip install pymysql (alternatyva jei anas  neveikia)
# jei atidarius workbencha nerodo duomenu baziu, o tik no connection established raudonai, darom taip:
# start ->command prompt. paleidziam kaip ADMINISTRATORIUS. atidaro terminala. jame rasome: net start (jusu servo
# pavadinimas, mysqld80 ar kazkas panasaus)
# pvz: net start new_one
import mysql.connector

DB_CONFIG = {
    'host':'localhost', #127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3312,
    'user':'root',
    'password':"root",
    'database':'holidays'
}
headers = ['id','country','city','accomodation','price']
def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_holidays():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from holidays')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    # print(rows)  # viskas kas zemiau funkcijoje yra tam, kad rezulata paverstu listu su dictionariais. veikia ir be to
    holidays_list = []
    for row in rows:
        single_holiday = {}
        for col_num in range(len(headers)):
            single_holiday[headers[col_num]] = str(row[col_num])
        holidays_list.append(single_holiday)
    return holidays_list

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")

def print_holidays(holidays):
    holidays = load_holidays()
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
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO holidays(country, city, accomodation, price) VALUES(%s,%s,%s,%s)", (country,city,accom,price))
    conn.commit()
    cur.close()
    conn.close()
    return id_counter

def edit_holiday(holidays):
    print('atostogu redagavimas')
    print("iveskite id atostogu kurias norite redaguoti")
    edit_id = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from holidays where id = %s",(edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        print(f'{row[0]}. Atostogos {row[1]} {row[2]}. Kaina gyvenant {row[3]} '
              f'parai {row[4]} eurų.')
        country = input()
        print("iveskite miesta")
        city = input()
        print('iveskite apgyveninimo tipa')
        accomodation = input()
        print('iveskite kaina')
        price = float(input())
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            'UPDATE `holidays` SET `country` = %s,`city` = %s,`accomodation` =%s,`price` =%s WHERE `id` =%s;',
            (country,city,accomodation,price,edit_id)
        )
        conn.commit()
        cur.close()
        conn.close()
    else:
        print('Įrašo su tokiu id nėra.')

def remove_holiday(holidays):
    print('atostogu salinimas')
    print("iveskite id atostogu kurias norite pasalinti")
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("select * from holidays where id = %s", (del_id,))
    row = cur.fetchone()
    if row:
        print(f'{row[0]}. Atostogos {row[1]} {row[2]}. Kaina gyvenant {row[3]} '
              f'parai {row[4]} eurų.')

        cur.execute('DELETE FROM `holidays`WHERE id = %s;',(del_id,))
        conn.commit()
    else:
        print('Įrašo su tokiu id nėra.')
    cur.close()
    conn.close()