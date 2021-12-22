import sys
import datetime
from dateutil.relativedelta import relativedelta

print("Ten program oblicza różne kadrowe rzeczy :)")
imie_nazwisko = input("Podaj imię i nazwisko : ") #Imię i nazwisko do nazwy pliku
nazwa_pliku = imie_nazwisko + ".txt" #Utworzenie .txt
stanowisko = input("Podaj stanowisko: ")
adres = input("Podaj adres: ")
kategoria = input("Podaj kategorię zaszeregowania: ")

while True: #Sprawdzenie poprawności typu danych wejściowych
    try:
        wyn_zasa = float(input("Podaj wynagrodzenie zasadnicze: "))
        break
    except ValueError:
        print("Nieprawidłowe dane wejściowe.")
        continue
while True:
    try:
        dod_staz_p = float(input("Podaj wartość dodatku stażowego w % (np. 20): ")) #Wartości dodatków w %
        break
    except ValueError:
        print("Nieprawidłowe dane wejściowe.")
        continue
while True:
    try:
        dod_funk_p = float(input("Podaj wartość dodatku funkcyjnego w % (np. 10): "))
        break
    except ValueError:
        print("Nieprawidłowe dane wejściowe.")
        continue

dod_staz_z = wyn_zasa*(dod_staz_p/100) #Wartości dodatków w złotówkach
dod_funk_z = wyn_zasa*(dod_funk_p/100)
wyn_lacz = wyn_zasa + wyn_zasa*(dod_staz_p/100) + wyn_zasa*(dod_funk_p/100) #Wynagrodzenie łącznie

data_zatrudnienia_input = input("Podaj datę zatrudnienia w formacie DD.MM.RRRR : ")
d_z, m_z, r_z = map(int, data_zatrudnienia_input.split('.')) #Dzień zatrudnienia, miesiąc zatrudnienia, rok zatrudnienia
data_zatrudnienia = datetime.date(r_z, m_z, d_z) #Właściwa zmienna - data zatrudnienia

data_kop_input = input("Podaj datę końca okresu próbnego (ostatni dzień) w formacie DD.MM.RRRR : ")
d_kop, m_kop, r_kop = map(int, data_kop_input.split('.')) #Koniec okresu próbnego
data_kop = datetime.date(r_kop, m_kop, d_kop) #Właściwa zmienna - data końca okresu próbnego

umowa_ncno = data_kop + relativedelta(months=+33, days=+1) #Data umowy na czas nieokreślony
ow_1m_start = data_zatrudnienia + relativedelta(months=+6) #Początek miesięcznego okresu wypowiedzenia
ow_3m = data_zatrudnienia + relativedelta(years=+3, days=-1) #Początek trzymiesięcznego okresu wypowiedzenia

sys.stdout = open(nazwa_pliku, "w") #Tworzenie pliku tekstowego
print("Daty w tym pliku zapisane są w formacie DD.MM.RRRR")
print("Pracownik:", imie_nazwisko)
print("Adres:", adres)
print("Stanowisko:", stanowisko)
print("Kategoria zaszeregowania:", kategoria)
print("Wynagrodzenie zasadnicze:", wyn_zasa, "zł")
print("Dodatek stażowy: ", dod_staz_z, " zł, (", dod_staz_p, " %)", sep='')
print("Dodatek funkcyjny: ", dod_funk_z, " zł, (", dod_funk_p, " %)", sep='')
print("Wynagrodzenie łącznie:", wyn_lacz, "zł")
print(data_zatrudnienia.strftime("Data zatrudnienia: %d.%m.%Y"))
print(umowa_ncno.strftime("Data podpisania umowy na czas nieokreślony: %d.%m.%Y"))
print(ow_1m_start.strftime("Początek miesięcznego okresu wypowiedzenia: %d.%m.%Y"))
print(ow_3m.strftime("Początek trzymiesięcznego okresu wypowiedzenia: %d.%m.%Y"))
sys.stdout.close()

