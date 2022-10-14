# import re

# sabloni = {
#     "celi_brojevi": r"^\-?[0-9]+$",
#     "realni_brojevi": r"^\-?[0-9]+\.[0-9]+$",
#     "domeni": r"^[a-z][a-z0-9]+\.[a-z]{2,7}$",
#     "tablice": r"^[A-Z^WQYX]{2}\-[0-9]{3,5}\-[A-Z^WQY]{2}$"
# }

# imena_sablona = list(sabloni.keys())
# broj_sablona = len(imena_sablona)

# podaci = ""

# def unos_fajla ():
#     ime_fajla = input("Unesite ime datoteke sa podacima: ")

#     try:
#         file = open(ime_fajla)
#         podaci = file.read()

#     except FileNotFoundError:
#         print("Ta datoteka ne postoji.")
#         exit()

# def prikaz_menija (opcije):
#     kljucevi = list(opcije.keys())
#     n = len(kljucevi)
#     print("Moguci sabloni su:")
#     print("  0) Izlaz")
#     for i in range(len(kljucevi)):
#         ime_sablona = kljucevi[i]
#         print(f"  {i+1}) {ime_sablona}")
#     print(f"  {n+1}) Promena fajla")

# def unos_izbora (opcije):
#     broj_opcija = len(list(opcije.keys()))

#     izbor = 0
#     while izbor < 1 or izbor > broj_opcija + 1:
#         try:
#             izbor = int(input("Koju opciju birate? "))
#         except ValueError:
#             izbor = -1
    
#     return izbor

# while True:
#     izabrana_opcija = unos_izbora(sabloni)

#     if izabrana_opcija == 0:
#         break

#     if izabrana_opcija == broj_sablona + 1:
#         continue

#     ime_izabranog_sablona = imena_sablona[izabrana_opcija - 1]
#     izabrani_regularni_izraz = sabloni[ime_izabranog_sablona]

#     rezultati = re.findall(izabrani_regularni_izraz, podaci, flags=re.MULTILINE)

#     for red in rezultati:
#         print(red)

# print("Kraj.")

# file = open("document.txt", "w")
# file.write("Very important!")
# file.flush()
# file.close()

#########################################################

# date = input("Input date: ")
# user_text = input("Input your thoughts: ")
# pattern = f"{date}\n\n{user_text}\n\n\n\n"

# file = open("document.txt", "a")
# file.write(pattern)
# file.flush()
# file.close()

#########################################################

import re

# NNN/NN-NN-NNN
# NNN/NNN-NNNN
# NNN/NNN-NNN
# +NNNNNNNN...

# telefon = input("Unesite broj telefona: ")

# print(telefon)

# # 1) Prvo 4 provere pojedinacno:
# sablonA = r'^0[1-9][0-9]/[0-9]{2}\-[0-9]{2}\-[0-9]{3}$'
# sablonB = r'^0[1-9][0-9]/[0-9]{2}\-[0-9]{3,4}$'
# sablonC = r'^0\+[0-9]{8,24}$'

# if re.search(sablonA, telefon) or re.search(sablonB, telefon) or re.search(sablonC, telefon):
#     print(f"{telefon} je u ispravnom formatu telefona.")
# else:
#     print(f"{telefon} nije u ispravnom formatu telefona.")

# # 2) Onda sve 4 spojene u jedan izraz:
# sablon = r'^([1-9][0-9]/[0-9]{2}\-[0-9]{2}\-[0-9]{3})|(0[1-9][0-9]/[0-9]{2}\-[0-9]{3,4})|(0\+[0-9]{8,24})$'

# if re.search(sablon, telefon):
#     print(f"{telefon} je u ispravnom formatu telefona.")
# else:
#     print(f"{telefon} nije u ispravnom formatu telefona.")