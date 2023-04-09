import oracledb
import getpass
from faker import Faker
from faker_vehicle import VehicleProvider
import uuid
from pesel import generuj_pesel
from datetime import datetime, timedelta
import random
from rand_vin import generate_vin


userpwd = getpass.getpass("Podaj hasło: ")
conn = oracledb.connect(user='s100747', password=userpwd, 
                        host='217.173.198.135', port=1521, service_name='tpdb')

fake = Faker(['pl_PL'])
fake.add_provider(VehicleProvider)

def wpisz_klient():

    params = {
        'imie_klienta': fake.first_name(),
        'nazwisko_klienta': fake.last_name(),
        'ulica_klienta': fake.street_address(),
        'kod_pocztowy_klienta': int(fake.zipcode().replace('-', '')),
        'miasto_klienta': fake.city(),
        'nr_telefonu_klienta': int(fake.phone_number().replace(' ', '')),
        'pesel_klienta': generuj_pesel(),
        'numer_karty_kredytowej': fake.credit_card_number(),
        'data_ważności_karty': datetime.strptime(fake.credit_card_expire(), '%m/%y').strftime('%d-%m-%Y'),
        'cvv_karty_kredytowej': fake.credit_card_security_code()
    }

    cur = conn.cursor()
    cur.execute('INSERT INTO klient (IMIE, NAZWISKO, ULICA_I_NUMER, KOD_POCZTOWY, MIASTO, NR_TEL, PESEL, NUMER_KARTY_KREDYTOWEJ, DATA_WAŻNOŚCI_KARTY, CVV_KARTY_KREDYTOWEJ) VALUES (:imie_klienta, :nazwisko_klienta, :ulica_klienta, :kod_pocztowy_klienta, :miasto_klienta, :nr_telefonu_klienta, :pesel_klienta, :numer_karty_kredytowej, TO_DATE(:data_ważności_karty, \'DD-MM-YYYY\'), :cvv_karty_kredytowej)',
                params)
    conn.commit()
    cur.close()

    print(f'Wpisano klienta: {params["imie_klienta"]} {params["nazwisko_klienta"]}; pesel: {params["pesel_klienta"]}; ulica: {params["ulica_klienta"]}; kod i miasto: {params["kod_pocztowy_klienta"]} {params["miasto_klienta"]}; nr_tel {params["nr_telefonu_klienta"]}')

def wpisz_pracownika():
    
    params = {
        'imie_pracownika': fake.first_name(),
        'nazwisko_pracownika': fake.last_name(),
        'email_pracownika': fake.email(),
        'nr_telefonu_pracownika': int(fake.phone_number().replace(' ', ''))
    }

    cur = conn.cursor()
    cur.execute('INSERT INTO pracownik (imie, nazwisko, mail, telefon) VALUES (:imie_pracownika, :nazwisko_pracownika, :email_pracownika, :nr_telefonu_pracownika)',
                params)
    conn.commit()
    cur.close()

    print(f'Wpisano pracownika: {params["imie_pracownika"]} {params["nazwisko_pracownika"]}; email: {params["email_pracownika"]}; nr_tel: {params["nr_telefonu_pracownika"]}')

def wpisz_samochod():

    engine = ['benzyna', 'diesel', 'hybryda', 'elektryczny']
    drive_type = ['FWD', 'RWD', 'AWD']

    params = {
        'marka_samochodu' : fake.vehicle_make(),
        'model_samochodu' : fake.vehicle_model(),
        'silnik_samochodu' : random.choice(engine),
        'naped_samochodu' : random.choice(drive_type),
        'moce_samochodu' : random.randint(150, 2000),
        'VIN' : generate_vin(),
        'tablica_rejestracyjna' : fake.license_plate(),
    }

def wpisz_rezerwacja():

    dzis = datetime.now()
    dni_w_przod = random.randint(1, 365)
    data_do_kiedy = dzis + timedelta(days=dni_w_przod)

    params = {
        'id_klienta':  random.randint(1, 100),
        'id_samochodu': random.randint(1, 100),
        'data_do_kiedy': data_do_kiedy.strftime('%d-%m-%Y')
    }

for _ in range(100):
    wpisz_klient()
    wpisz_pracownika()

conn.close()


