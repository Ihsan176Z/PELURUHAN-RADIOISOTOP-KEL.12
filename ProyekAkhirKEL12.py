'''
Kelompok : 12-Prak.KN-2024
Topik    : Peluruhan Radioaktif
Anggota  :
> Sena Patriarka Cinan (140310230015)
> M. Ihsan Putra P. M. (140310230024)
> Falesya Luneta A.    (140310230059)
'''
## LIBRARY
import numpy as np
import matplotlib.pyplot as plt

## UNSUR TABEL PERIODIK
Unsur = [
    {"Nomor Atom" : 1, "Simbol" : "H", "Nama" : "Hidrogen"},
    {"Nomor Atom" : 2, "Simbol" : "He", "Nama" : "Helium"},
    {"Nomor Atom" : 3, "Simbol" : "Li", "Nama" : "Litium"},
    {"Nomor Atom" : 4, "Simbol" : "Be", "Nama" : "Berilium"},
    {"Nomor Atom" : 5, "Simbol" : "B", "Nama" : "Boron"},
    {"Nomor Atom" : 6, "Simbol" : "C", "Nama" : "Karbon"},
    {"Nomor Atom" : 7, "Simbol" : "N", "Nama" : "Nitrogen"},
    {"Nomor Atom" : 8, "Simbol" : "O", "Nama" : "Oksigen"},
    {"Nomor Atom" : 9, "Simbol" : "F", "Nama" : "Fluorin"},
    {"Nomor Atom" : 10, "Simbol" : "Ne", "Nama" : "Neon"},
    {"Nomor Atom" : 11, "Simbol" : "Na", "Nama" : "Natrium"},
    {"Nomor Atom" : 12, "Simbol" : "Mg", "Nama" : "Magnesium"},
    {"Nomor Atom" : 13, "Simbol" : "Al", "Nama" : "Aluminium"},
    {"Nomor Atom": 14, "Simbol": "Si", "Nama": "Silikon"},
    {"Nomor Atom": 15, "Simbol": "P", "Nama": "Fosfor"},
    {"Nomor Atom": 16, "Simbol": "S", "Nama": "Belerang"},
    {"Nomor Atom": 17, "Simbol": "Cl", "Nama": "Klorin"},
    {"Nomor Atom": 18, "Simbol": "Ar", "Nama": "Argon"},
    {"Nomor Atom": 19, "Simbol": "K", "Nama": "Kalium"},
    {"Nomor Atom": 20, "Simbol": "Ca", "Nama": "Kalsium"},
    {"Nomor Atom": 21, "Simbol": "Sc", "Nama": "Skandium"},
    {"Nomor Atom": 22, "Simbol": "Ti", "Nama": "Titanium"},
    {"Nomor Atom": 23, "Simbol": "V", "Nama": "Vanadium"},
    {"Nomor Atom": 24, "Simbol": "Cr", "Nama": "Kromium"},
    {"Nomor Atom": 25, "Simbol": "Mn", "Nama": "Mangan"},
    {"Nomor Atom": 26, "Simbol": "Fe", "Nama": "Besi"},
    {"Nomor Atom": 27, "Simbol": "Co", "Nama": "Kobalt"},
    {"Nomor Atom": 28, "Simbol": "Ni", "Nama": "Nikel"},
    {"Nomor Atom": 29, "Simbol": "Cu", "Nama": "Tembaga"},
    {"Nomor Atom": 30, "Simbol": "Zn", "Nama": "Seng"},
    {"Nomor Atom": 31, "Simbol": "Ga", "Nama": "Galium"},
    {"Nomor Atom": 32, "Simbol": "Ge", "Nama": "Germanium"},
    {"Nomor Atom": 33, "Simbol": "As", "Nama": "Arsen"},
    {"Nomor Atom": 34, "Simbol": "Se", "Nama": "Selenium"},
    {"Nomor Atom": 35, "Simbol": "Br", "Nama": "Bromin"},
    {"Nomor Atom": 36, "Simbol": "Kr", "Nama": "Kripton"},
    {"Nomor Atom": 37, "Simbol": "Rb", "Nama": "Rubidium"},
    {"Nomor Atom": 38, "Simbol": "Sr", "Nama": "Stronsium"},
    {"Nomor Atom": 39, "Simbol": "Y", "Nama": "Itrium"},
    {"Nomor Atom": 40, "Simbol": "Zr", "Nama": "Zirkonium"},
    {"Nomor Atom": 41, "Simbol": "Nb", "Nama": "Niobium"},
    {"Nomor Atom": 42, "Simbol": "Mo", "Nama": "Molibdenum"},
    {"Nomor Atom": 43, "Simbol": "Tc", "Nama": "Teknesium"},
    {"Nomor Atom": 44, "Simbol": "Ru", "Nama": "Rutenium"},
    {"Nomor Atom": 45, "Simbol": "Rh", "Nama": "Rodium"},
    {"Nomor Atom": 46, "Simbol": "Pd", "Nama": "Paladium"},
    {"Nomor Atom": 47, "Simbol": "Ag", "Nama": "Perak"},
    {"Nomor Atom": 48, "Simbol": "Cd", "Nama": "Kadmium"},
    {"Nomor Atom": 49, "Simbol": "In", "Nama": "Indium"},
    {"Nomor Atom": 50, "Simbol": "Sn", "Nama": "Timah"},
    {"Nomor Atom": 51, "Simbol": "Sb", "Nama": "Antimon"},
    {"Nomor Atom": 52, "Simbol": "Te", "Nama": "Telurium"},
    {"Nomor Atom": 53, "Simbol": "I", "Nama": "Iodin"},
    {"Nomor Atom": 54, "Simbol": "Xe", "Nama": "Xenon"},
    {"Nomor Atom": 55, "Simbol": "Cs", "Nama": "Sesium"},
    {"Nomor Atom": 56, "Simbol": "Ba", "Nama": "Barium"},
    {"Nomor Atom": 57, "Simbol": "La", "Nama": "Lantanum"},
    {"Nomor Atom": 58, "Simbol": "Ce", "Nama": "Serium"},
    {"Nomor Atom": 59, "Simbol": "Pr", "Nama": "Praseodimium"},
    {"Nomor Atom": 60, "Simbol": "Nd", "Nama": "Neodimium"},
    {"Nomor Atom": 61, "Simbol": "Pm", "Nama": "Promethium"},
    {"Nomor Atom": 62, "Simbol": "Sm", "Nama": "Samarium"},
    {"Nomor Atom": 63, "Simbol": "Eu", "Nama": "Europium"},
    {"Nomor Atom": 64, "Simbol": "Gd", "Nama": "Gadolinium"},
    {"Nomor Atom": 65, "Simbol": "Tb", "Nama": "Terbium"},
    {"Nomor Atom": 66, "Simbol": "Dy", "Nama": "Disprosium"},
    {"Nomor Atom": 67, "Simbol": "Ho", "Nama": "Holmium"},
    {"Nomor Atom": 68, "Simbol": "Er", "Nama": "Erbium"},
    {"Nomor Atom": 69, "Simbol": "Tm", "Nama": "Tulium"},
    {"Nomor Atom": 70, "Simbol": "Yb", "Nama": "Iterbium"},
    {"Nomor Atom": 71, "Simbol": "Lu", "Nama": "Lutetium"},
    {"Nomor Atom": 72, "Simbol": "Hf", "Nama": "Hafnium"},
    {"Nomor Atom": 73, "Simbol": "Ta", "Nama": "Tantalum"},
    {"Nomor Atom": 74, "Simbol": "W", "Nama": "Tungsten"},
    {"Nomor Atom": 75, "Simbol": "Re", "Nama": "Rhenium"},
    {"Nomor Atom": 76, "Simbol": "Os", "Nama": "Osmium"},
    {"Nomor Atom": 77, "Simbol": "Ir", "Nama": "Iridium"},
    {"Nomor Atom": 78, "Simbol": "Pt", "Nama": "Platinum"},
    {"Nomor Atom": 79, "Simbol": "Au", "Nama": "Emas"},
    {"Nomor Atom": 80, "Simbol": "Hg", "Nama": "Raksa"},
    {"Nomor Atom": 81, "Simbol": "Tl", "Nama": "Talium"},
    {"Nomor Atom": 82, "Simbol": "Pb", "Nama": "Timbal"},
    {"Nomor Atom": 83, "Simbol": "Bi", "Nama": "Bismut"},
    {"Nomor Atom": 84, "Simbol": "Po", "Nama": "Polonium"},
    {"Nomor Atom": 85, "Simbol": "At", "Nama": "Astatin"},
    {"Nomor Atom": 86, "Simbol": "Rn", "Nama": "Radon"},
    {"Nomor Atom": 87, "Simbol": "Fr", "Nama": "Fransium"},
    {"Nomor Atom": 88, "Simbol": "Ra", "Nama": "Radium"},
    {"Nomor Atom": 89, "Simbol": "Ac", "Nama": "Aktinium"},
    {"Nomor Atom": 90, "Simbol": "Th", "Nama": "Torium"},
    {"Nomor Atom": 91, "Simbol": "Pa", "Nama": "Protaktinium"},
    {"Nomor Atom": 92, "Simbol": "U", "Nama": "Uranium"},
    {"Nomor Atom": 93, "Simbol": "Np", "Nama": "Neptunium"},
    {"Nomor Atom": 94, "Simbol": "Pu", "Nama": "Plutonium"},
    {"Nomor Atom": 95, "Simbol": "Am", "Nama": "Americium"},
    {"Nomor Atom": 96, "Simbol": "Cm", "Nama": "Kurium"},
    {"Nomor Atom": 97, "Simbol": "Bk", "Nama": "Berkelium"},
    {"Nomor Atom": 98, "Simbol": "Cf", "Nama": "Kalifornium"},
    {"Nomor Atom": 99, "Simbol": "Es", "Nama": "Einsteinium"},
    {"Nomor Atom": 100, "Simbol": "Fm", "Nama": "Fermium"},
    {"Nomor Atom": 101, "Simbol": "Md", "Nama": "Mendelevium"},
    {"Nomor Atom": 102, "Simbol": "No", "Nama": "Nobelium"},
    {"Nomor Atom": 103, "Simbol": "Lr", "Nama": "Lawrensium"},
    {"Nomor Atom": 104, "Simbol": "Rf", "Nama": "Rutherfordium"},
    {"Nomor Atom": 105, "Simbol": "Db", "Nama": "Dubnium"},
    {"Nomor Atom": 106, "Simbol": "Sg", "Nama": "Seaborgium"},
    {"Nomor Atom": 107, "Simbol": "Bh", "Nama": "Bohrium"},
    {"Nomor Atom": 108, "Simbol": "Hs", "Nama": "Hasium"},
    {"Nomor Atom": 109, "Simbol": "Mt", "Nama": "Meitnerium"},
    {"Nomor Atom": 110, "Simbol": "Ds", "Nama": "Darmstadtium"},
    {"Nomor Atom": 111, "Simbol": "Rg", "Nama": "Roentgenium"},
    {"Nomor Atom": 112, "Simbol": "Cn", "Nama": "Kopernicium"},
    {"Nomor Atom": 113, "Simbol": "Nh", "Nama": "Nihonium"},
    {"Nomor Atom": 114, "Simbol": "Fl", "Nama": "Flerovium"},
    {"Nomor Atom": 115, "Simbol": "Mc", "Nama": "Moskovium"},
    {"Nomor Atom": 116, "Simbol": "Lv", "Nama": "Livermorium"},
    {"Nomor Atom": 117, "Simbol": "Ts", "Nama": "Tenesin"},
    {"Nomor Atom": 118, "Simbol": "Og", "Nama": "Oganeson"}
]

## ISOTOP SETIAP UNSUR
Isotopes = [
    # Unsur 1 Hidrogen
    [
        {"Massa Atom" : 1, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 2, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 3, "Waktu Paruh" : 12.32, "Satuan Paruh" : "tahun", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 4, "Waktu Paruh" : 10**(-10), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 5, "Waktu Paruh" : 8*10**(-11), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [2]},
        {"Massa Atom" : 6, "Waktu Paruh" : 2.9*10**(-10), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 7, "Waktu Paruh" : 2.3*10**(-11), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [2]}
    ],
    # Unsur 2 Helium
    [
        {"Massa Atom" : 3, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 4, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 5, "Waktu Paruh" : 7.6*10**(-10), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 6, "Waktu Paruh" : 806.7, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 7, "Waktu Paruh" : 3.04*10**(-9), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 8, "Waktu Paruh" : 119, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 9, "Waktu Paruh" : 7*10**(-9), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 10, "Waktu Paruh" : 1.52**(-9), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [2]}
    ],
    # Unsur 3 Litium
    [
        {"Massa Atom": 3, "Waktu Paruh": 0.0123, "Satuan Paruh": "detik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 4, "Waktu Paruh" : 7.57*10**(-11), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 5, "Waktu Paruh" : 3.04*10**(-10), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 6, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 7, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 8, "Waktu Paruh" : 839.9, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Alpha"], "Orde" : [1, 1]},
        {"Massa Atom" : 9, "Waktu Paruh" : 178.3, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 10, "Waktu Paruh" : 2*10**(-9), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 11, "Waktu Paruh" : 8.59, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 12, "Waktu Paruh" : 10, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]}
    ],
    # Unsur 4 Berilium
    [
        {"Massa Atom": 5, "Waktu Paruh": None, "Satuan Paruh": None, "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 6, "Waktu Paruh" : 5, "Satuan Paruh" : "zeptodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 7, "Waktu Paruh" : 53.22, "Satuan Paruh" : "hari", "Peluruhan" : ["Emisi Elektron"], "Orde" : [1]},
        {"Massa Atom" : 8, "Waktu Paruh" : 8.2*10**(-8), "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom" : 9, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 10, "Waktu Paruh" : 1.513, "Satuan Paruh" : "tahun", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 11, "Waktu Paruh" : 13.81, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 12, "Waktu Paruh" : 21.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 13, "Waktu Paruh" : 2.7*10**(-12), "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 14, "Waktu Paruh" : 4.35, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom": 15, "Waktu Paruh": 200, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 16, "Waktu Paruh" : 200, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [2]}
    ],
    # Unsur 5 Boron
    [
        {"Massa Atom": 6, "Waktu Paruh": None, "Satuan Paruh": None, "Peluruhan" : ["Emisi Proton"], "Orde" : [2]},
        {"Massa Atom" : 7, "Waktu Paruh" : 3.26*10**(-13), "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 8, "Waktu Paruh" : 3.04*10**(-10), "Satuan Paruh" : "pikodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 9, "Waktu Paruh" : 770, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Plus", "Alpha"], "Orde" : [1, 1]},
        {"Massa Atom" : 10, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 11, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 12, "Waktu Paruh" : 20.2, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 13, "Waktu Paruh" : 17.33, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 14, "Waktu Paruh" : 12.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 15, "Waktu Paruh" : 9.93, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom": 16, "Waktu Paruh": 0.19, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 17, "Waktu Paruh" : 5.08, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 18, "Waktu Paruh" : 26, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 19, "Waktu Paruh" : 2.92, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]}
    ],
    # Unsur 6 Karbon
    [
        {"Massa Atom": 8, "Waktu Paruh": 2*10**(-12), "Satuan Paruh": "nanodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [2]},
        {"Massa Atom" : 9, "Waktu Paruh" : 126.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 10, "Waktu Paruh" : 19.29, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 11, "Waktu Paruh" : 20.334, "Satuan Paruh" : "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 12, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 13, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 14, "Waktu Paruh" : 5707.76, "Satuan Paruh" : "tahun", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 15, "Waktu Paruh" : 2.449, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 16, "Waktu Paruh" : 747, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 17, "Waktu Paruh" : 193, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 18, "Waktu Paruh": 91, "Satuan Paruh": "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 19, "Waktu Paruh" : 49, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 20, "Waktu Paruh" : 14, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 21, "Waktu Paruh" : 30, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom": 22, "Waktu Paruh": 6.2, "Satuan Paruh": "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]}
    ],
    # Unsur 7 Nitrogen
    [
        {"Massa Atom" : 10, "Waktu Paruh" : 19.29, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 11, "Waktu Paruh" : 20.334, "Satuan Paruh" : "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 12, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 13, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 14, "Waktu Paruh" : 5707.76, "Satuan Paruh" : "tahun", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 15, "Waktu Paruh" : 2.449, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 16, "Waktu Paruh" : 747, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 17, "Waktu Paruh" : 193, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 18, "Waktu Paruh": 91, "Satuan Paruh": "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 19, "Waktu Paruh" : 49, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 20, "Waktu Paruh" : 14, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 21, "Waktu Paruh" : 30, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom": 22, "Waktu Paruh": 6.2, "Satuan Paruh": "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 23, "Waktu Paruh" : 14, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]},
        {"Massa Atom" : 24, "Waktu Paruh" : 30, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom": 25, "Waktu Paruh": 6.2, "Satuan Paruh": "milidetik", "Peluruhan" : ["Beta Minus", "Emisi Neutron"], "Orde" : [1, 1]}
    ],
    # Unsur 8 Oksigen
    [
        {"Massa Atom" : 12, "Waktu Paruh" : 1.1405*10**(-12), "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [2]},
        {"Massa Atom" : 13, "Waktu Paruh" : 8.59, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 14, "Waktu Paruh" : 1.176766, "Satuan Paruh" : "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 15, "Waktu Paruh" : 2.03733, "Satuan Paruh" : "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 16, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : [None], "Orde" : [None]},
        {"Massa Atom" : 17, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : [None], "Orde" : [None]},
        {"Massa Atom" : 18, "Waktu Paruh" :  None, "Satuan Paruh" : None, "Peluruhan" : [None], "Orde" : [None]},
        {"Massa Atom" : 19, "Waktu Paruh" : 26.88, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 20, "Waktu Paruh" : 13.51, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 21, "Waktu Paruh" : 3.42, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 22, "Waktu Paruh" : 2.25, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 23, "Waktu Paruh" : 82, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 24, "Waktu Paruh" : 65, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 25, "Waktu Paruh" : 49.99, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 26, "Waktu Paruh" : 39.99, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 27, "Waktu Paruh" : 260, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutorn"], "Orde" : [1]},
        {"Massa Atom" : 28, "Waktu Paruh" : 100, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 9 Fluorin
    [
        {"Massa Atom" : 14, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Emisi Proton"], "Orde" : [2]},
        {"Massa Atom" : 15, "Waktu Paruh" : 4.562*10**(-13), "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 16, "Waktu Paruh" : 1.1405*10**(-11), "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 17, "Waktu Paruh" : 1.0733, "Satuan Paruh" : "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 18, "Waktu Paruh" : 1.829516, "Satuan Paruh" : None, "Peluruhan" : [None], "Orde" : [None]},
        {"Massa Atom" : 19, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : [None], "Orde" : [None]},
        {"Massa Atom" : 20, "Waktu Paruh" :  11.07, "Satuan Paruh" : "detik", "Peluruhan" : [None], "Orde" : [None]},
        {"Massa Atom" : 21, "Waktu Paruh" : 4.158, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 22, "Waktu Paruh" : 4.23, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 23, "Waktu Paruh" : 2.23, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 24, "Waktu Paruh" : 390, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 25, "Waktu Paruh" : 50, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 26, "Waktu Paruh" : 9.6, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 27, "Waktu Paruh" : 5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 28, "Waktu Paruh" : 39.99, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 29, "Waktu Paruh" : 2.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Emisi Neutorn"], "Orde" : [1]},
        {"Massa Atom" : 30, "Waktu Paruh" : 260, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 31, "Waktu Paruh" : 250, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [3]}
    ],
    # Unsur 10 Neon
    [
        {"Massa Atom" : 16, "Waktu Paruh" : 3.73934426*10**(-12), "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [2]},
        {"Massa Atom" : 17, "Waktu Paruh" : 109.2, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 18, "Waktu Paruh" : 1.672, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 19, "Waktu Paruh" : 17.22, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 20, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [1]},
        {"Massa Atom" : 21, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [1]},
        {"Massa Atom" : 22, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["STabil"], "Orde" : [1]},
        {"Massa Atom" : 23, "Waktu Paruh" : 37.42, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 24, "Waktu Paruh" : 3.383333, "Satuan Paruh" : "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 25, "Waktu Paruh" : 602, "Satuan Paruh" : "miliodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 26, "Waktu Paruh" : 192, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 27, "Waktu Paruh" : 32, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 28, "Waktu Paruh" : 18.9, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 29, "Waktu Paruh" : 14.8, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 30, "Waktu Paruh" : 7.3, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 31, "Waktu Paruh" : 3.4, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [2]},
        {"Massa Atom" : 32, "Waktu Paruh" : 3.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 33, "Waktu Paruh" : 180, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [3]},
        {"Massa Atom" : 34, "Waktu Paruh" :60, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [2]}
    ],
    # Unsur 11 Natrium
    [
        {"Massa Atom" : 18, "Waktu Paruh" : 1.3*10**(-12), "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 19, "Waktu Paruh" :39.99, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Proton"], "Orde" : [1]},
        {"Massa Atom" : 20, "Waktu Paruh" : 447.9, "Satuan Paruh" :"milidetik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 21, "Waktu Paruh" : 22.49, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 22, "Waktu Paruh" : 2.6027, "Satuan Paruh" : "tahun", "Peluruhan" : ["Stabil"], "Orde" : [1]},
        {"Massa Atom" : 23, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 24, "Waktu Paruh" : 14.997, "Satuan Paruh" : "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 25, "Waktu Paruh" : 59.1, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 26, "Waktu Paruh" : 1.077, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 27, "Waktu Paruh" : 301, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 28, "Waktu Paruh" : 30.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 29, "Waktu Paruh" : 44.9, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 30, "Waktu Paruh" : 48.4, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 31, "Waktu Paruh" : 17, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [3]},
        {"Massa Atom" : 32, "Waktu Paruh" : 13.2, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [2]},
        {"Massa Atom" : 33, "Waktu Paruh" : 8, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [2]},
        {"Massa Atom" : 34, "Waktu Paruh" : 5.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [2]},
        {"Massa Atom" : 35, "Waktu Paruh" : 1.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 36, "Waktu Paruh" : 180, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 37, "Waktu Paruh" : 60.00, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 12 Magnesium
    [
        {"Massa Atom" : 19, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Emisi Proton"], "Orde" : [2]},
        {"Massa Atom" : 20, "Waktu Paruh" : 90, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta PLus"], "Orde" : [1]},
        {"Massa Atom" : 21, "Waktu Paruh" : 122, "Satuan Paruh" :"milidetik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 22, "Waktu Paruh" : 3.8755, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 23, "Waktu Paruh" : 11.317, "Satuan Paruh" : "detik", "Peluruhan" : ["BEta Plus"], "Orde" : [1]},
        {"Massa Atom" : 24, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 25, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 26, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 27, "Waktu Paruh" : 9.45833, "Satuan Paruh" : "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 28, "Waktu Paruh" : 20.915, "Satuan Paruh" : "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 29, "Waktu Paruh" : 1.3, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 30, "Waktu Paruh" : 335, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 31, "Waktu Paruh" : 232, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 32, "Waktu Paruh" : 85, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [3]},
        {"Massa Atom" : 33, "Waktu Paruh" : 90.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [2]},
        {"Massa Atom" : 34, "Waktu Paruh" : 20.197, "Satuan Paruh" : "milidetik", "Peluruhan" : ["BEta Minus"], "Orde" : [2]},
        {"Massa Atom" : 35, "Waktu Paruh" : 70.69, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [2]},
        {"Massa Atom" : 36, "Waktu Paruh" :3.9, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 37, "Waktu Paruh" : 260, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 38, "Waktu Paruh" : 260, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 39, "Waktu Paruh" : 180, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 40, "Waktu Paruh" : 170, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 13 Aluminium
    [
        {"Massa Atom" : 21, "Waktu Paruh" : 35, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Stabil"], "Orde" : [1]},
        {"Massa Atom" : 22, "Waktu Paruh" : 3.8755, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom" : 23, "Waktu Paruh" : 11.317, "Satuan Paruh" : "detik", "Peluruhan" : ["BEta Plus"], "Orde" : [1]},
        {"Massa Atom" : 24, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 25, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 26, "Waktu Paruh" : None, "Satuan Paruh" : None, "Peluruhan" : ["Stabil"], "Orde" : [None]},
        {"Massa Atom" : 27, "Waktu Paruh" : 9.45833, "Satuan Paruh" : "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 28, "Waktu Paruh" : 20.915, "Satuan Paruh" : "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 29, "Waktu Paruh" : 1.3, "Satuan Paruh" : "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 30, "Waktu Paruh" : 335, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 31, "Waktu Paruh" : 232, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 32, "Waktu Paruh" : 85, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [3]},
        {"Massa Atom" : 33, "Waktu Paruh" : 90.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [2]},
        {"Massa Atom" : 34, "Waktu Paruh" : 20.197, "Satuan Paruh" : "milidetik", "Peluruhan" : ["BEta Minus"], "Orde" : [2]},
        {"Massa Atom" : 35, "Waktu Paruh" : 70.69, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [2]},
        {"Massa Atom" : 36, "Waktu Paruh" :3.9, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 37, "Waktu Paruh" : 260, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 38, "Waktu Paruh" : 260, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 39, "Waktu Paruh" : 180, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Emisi Neutron"], "Orde" : [1]},
        {"Massa Atom" : 40, "Waktu Paruh" : 170, "Satuan Paruh" : "nanodetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 41, "Waktu Paruh" : 1.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom" : 42, "Waktu Paruh" : 1.5, "Satuan Paruh" : "milidetik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 14 Silikon
    [
        None
    ],
    # Unsur 15 Fosfor
    [
        None
    ],
    # Unsur 16 Belerang
    [
        None
    ],
    # Unsur 17 Klorin
    [
        None
    ],
    # Unsur 18 Argon
    [
        None
    ],
    # Unsur 19 Kalium
    [
        None
    ],
    # Unsur 20 Kalsium
    [
        None
    ],
    # Unsur 21 Skandium
    [
        None
    ],
    # Unsur 22 Titanium
    [
        None
    ],
    # Unsur 23 Vanadium
    [
        None
    ],
    # Unsur 24 Kromium
    [
        None
    ],
    # Unsur 25 Mangan
    [
        None
    ],
    # Unsur 26 Besi
    [
        None
    ],
    # Unsur 27 Kobalt
    [
        None
    ],
    # Unsur 28 Nikel
    [
        None
    ],
    # Unsur 29 Tembaga
    [
        None
    ],
    # Unsur 30 Seng
    [
        None
    ],
    # Unsur 31 Galium
    [
        None
    ],
    # Unsur 32 Germanium
    [
        None
    ],
    # Unsur 33 Arsen
    [
        None
    ],
    # Unsur 34 Selenium
    [
        None
    ],
    # Unsur 35 Bromin
    [
        None
    ],
    # Unsur 36 Kripton
    [
        None
    ],
    # Unsur 37 Rubidium
    [
        None
    ],
    # Unsur 38 Stronsium
    [
        None
    ],
    # Unsur 39 Itrium
    [
        None
    ],
    # Unsur 40 Zirkonium
    [
        None
    ],
    # Unsur 41 Niobium
    [
        None
    ],
    # Unsur 42 Molibdenum
    [
        None
    ],
    # Unsur 43 Teknesium
    [
        None
    ],
    # Unsur 44 Rutenium
    [
        None
    ],
    # Unsur 45 Rodium
    [
        None
    ],
    # Unsur 46 Paladium
    [
        None
    ],
    # Unsur 47 Perak
    [
        None
    ],
    # Unsur 48 Kadmium
    [
        None
    ],
    # Unsur 49 Indium
    [
        None
    ],
    # Unsur 50 Timah
    [
        None
    ],
    # Unsur 51 Antimon
    [
        None
    ],
    # Unsur 52 Telurium
    [
        None
    ],
    # Unsur 53 Iodin
    [
        None
    ],
    # Unsur 54 Xenon
    [
        None
    ],
    # Unsur 55 Sesium
    [
        None
    ],
    # Unsur 56 Barium
    [
        None
    ],
    # Unsur 57 Lantanum
    [
        None
    ],
    # Unsur 58 Serium
    [
        None
    ],
    # Unsur 59 Praseodimium
    [
        None
    ],
    # Unsur 60 Neodimium
    [
        None
    ],
    # Unsur 61 Promethium
    [
        None
    ],
    # Unsur 62 Samarium
    [
        None
    ],
    # Unsur 63 Europium
    [
        None
    ],
    # Unsur 64 Gadolinium
    [
        None
    ],
    # Unsur 65 Terbium
    [
        None
    ],
    # Unsur 66 Disprosium
    [
        None
    ],
    # Unsur 67 Holmium
    [
        None
    ],
    # Unsur 68 Erbium
    [
        None
    ],
    # Unsur 69 Tulium
    [
        None
    ],
    # Unsur 70 Iterbium
    [
        None
    ],
    # Unsur 71 Lutetium
    [
        None
    ],
    # Unsur 72 Hafnium
    [
        None
    ],
    # Unsur 73 Tantalum
    [
        None
    ],
    # Unsur 74 Tungsten
    [
        None
    ],
    # Unsur 75 Rhenium
    [
        None
    ],
    # Unsur 76 Osmium
    [
        None
    ],
    # Unsur 77 Iridium
    [
        None
    ],
    # Unsur 78 Platinum
    [
        None
    ],
    # Unsur 79 Emas
    [
        None
    ],
    # Unsur 80 Raksa
    [
        None
    ],
    # Unsur 81 Talium
    [
        None
    ],
    # Unsur 82 Timbal
    [
        None
    ],
    # Unsur 83 Bismut
    [
        None
    ],
    # Unsur 84 Polonium
    [
        None
    ],
    # Unsur 85 Astatin
    [
        None
    ],
    # Unsur 86 Radon
    [
        None
    ],
    # Unsur 87 Fransium
    [
        None
    ],
    # Unsur 88 Radium
    [
        {"Massa Atom": 202, "Waktu Paruh": 16, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 203, "Waktu Paruh": 31, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 204, "Waktu Paruh": 60, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 205, "Waktu Paruh": 210, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 206, "Waktu Paruh": 240, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 207, "Waktu Paruh": 1.3, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 208, "Waktu Paruh": 1.3, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 209, "Waktu Paruh": 4.616, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 210, "Waktu Paruh": 3.7, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 211, "Waktu Paruh": 13, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 212, "Waktu Paruh": 13, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 213, "Waktu Paruh": 2.73, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 214, "Waktu Paruh": 2.46, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 215, "Waktu Paruh": 1.55, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 216, "Waktu Paruh": 182, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 217, "Waktu Paruh": 1.6, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 218, "Waktu Paruh": 1.08, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 219, "Waktu Paruh": 25.2, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 220, "Waktu Paruh": 10.09, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 221, "Waktu Paruh": 28, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 222, "Waktu Paruh": 38, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 223, "Waktu Paruh": 11.43, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 224, "Waktu Paruh": 3.63, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 225, "Waktu Paruh": 14.93, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 226, "Waktu Paruh": 1585.489, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 227, "Waktu Paruh": 42.16, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 228, "Waktu Paruh": 5.739, "Satuan Paruh": "tahun", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 229, "Waktu Paruh": 4, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 230, "Waktu Paruh": 1.5, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 231, "Waktu Paruh": 1.716, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 232, "Waktu Paruh": 4.16, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 233, "Waktu Paruh": 30, "Satuan Paruh": "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 30, "Satuan Paruh": "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 89 Aktinium
    [
        {"Massa Atom": 206, "Waktu Paruh": 22, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 207, "Waktu Paruh": 27, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 208, "Waktu Paruh": 95, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 209, "Waktu Paruh": 100, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 210, "Waktu Paruh": 350, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 211, "Waktu Paruh": 210, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 212, "Waktu Paruh": 930, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 213, "Waktu Paruh": 738, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 214, "Waktu Paruh": 8.2, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 215, "Waktu Paruh": 170, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 216, "Waktu Paruh": 440, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 217, "Waktu Paruh": 69, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 218, "Waktu Paruh": 1.08, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 219, "Waktu Paruh": 11.8, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 220, "Waktu Paruh": 26.36, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 221, "Waktu Paruh": 52, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 222, "Waktu Paruh": 5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 223, "Waktu Paruh": 2.1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 224, "Waktu Paruh": 2.7, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 225, "Waktu Paruh": 9.953, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 226, "Waktu Paruh": 1.223, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 227, "Waktu Paruh": 21.772, "Satuan Paruh": "tahun", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 228, "Waktu Paruh": 6.138, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 229, "Waktu Paruh": 1.04, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 230, "Waktu Paruh": 2.03, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 231, "Waktu Paruh": 7.5, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 232, "Waktu Paruh": 1.983, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 233, "Waktu Paruh": 2.416, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 44, "Satuan Paruh": "detik", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 235, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 1.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 90 Torium
    [
        {"Massa Atom": 209, "Waktu Paruh": 3.8, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 210, "Waktu Paruh": 9, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 211, "Waktu Paruh": 40, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 212, "Waktu Paruh": 30, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 213, "Waktu Paruh": 144, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 214, "Waktu Paruh": 100, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 215, "Waktu Paruh": 1.2, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 216, "Waktu Paruh": 26, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 217, "Waktu Paruh": 241, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 218, "Waktu Paruh": 117, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 219, "Waktu Paruh": 1.05, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 220, "Waktu Paruh": 9.7, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 221, "Waktu Paruh": 1.68, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 222, "Waktu Paruh": 2.237, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 223, "Waktu Paruh": 600, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 224, "Waktu Paruh": 810, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 225, "Waktu Paruh": 8.716, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 226, "Waktu Paruh": 30.56, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 227, "Waktu Paruh": 18.6, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 228, "Waktu Paruh": 1.9116, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 229, "Waktu Paruh": 7880, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 230, "Waktu Paruh": 75437.59, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 231, "Waktu Paruh": 1.06, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 232, "Waktu Paruh": 1.4*10**(10), "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 233, "Waktu Paruh": 21.83, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 24.074, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 235, "Waktu Paruh": 7.16, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 37.3, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 237, "Waktu Paruh": 4.7, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 9.3, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 91 Protakinium
    [
        {"Massa Atom": 212, "Waktu Paruh": 5.1, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 213, "Waktu Paruh": 5.3, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 214, "Waktu Paruh": 17, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 215, "Waktu Paruh": 14, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 216, "Waktu Paruh": 150, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 217, "Waktu Paruh": 3.6, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 218, "Waktu Paruh": 113, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 219, "Waktu Paruh": 53, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 220, "Waktu Paruh": 780, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 221, "Waktu Paruh": 5.9, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 222, "Waktu Paruh": 3.3, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 223, "Waktu Paruh": 5.1, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 224, "Waktu Paruh": 850, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 225, "Waktu Paruh": 1.7, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 226, "Waktu Paruh": 1.8, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 227, "Waktu Paruh": 38.3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 228, "Waktu Paruh": 21.94, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 229, "Waktu Paruh": 1.5, "Satuan Paruh": "hari", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 230, "Waktu Paruh": 17.361, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 231, "Waktu Paruh": 32760, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 232, "Waktu Paruh": 1.32, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 233, "Waktu Paruh": 26.975, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 6.6, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 235, "Waktu Paruh": 24.43, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 9.16, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 237, "Waktu Paruh": 8.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 2.26, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 239, "Waktu Paruh": 1.8, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 240, "Waktu Paruh": 1.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 92 Uranium
    [
        {"Massa Atom": 217, "Waktu Paruh": 16, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 218, "Waktu Paruh": 510, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 219, "Waktu Paruh": 42, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 220, "Waktu Paruh": 60, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 221, "Waktu Paruh": 700, "Satuan Paruh": "nanodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 222, "Waktu Paruh": 1, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 223, "Waktu Paruh": 18, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 224, "Waktu Paruh": 900, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 225, "Waktu Paruh": 84, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 226, "Waktu Paruh": 350, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 227, "Waktu Paruh": 1.1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 228, "Waktu Paruh": 9.16, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 229, "Waktu Paruh": 58.3, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 230, "Waktu Paruh": 20.83, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 231, "Waktu Paruh": 4.16, "Satuan Paruh": "hari", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 232, "Waktu Paruh": 68.81, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 233, "Waktu Paruh": 159200, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 245500, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 235, "Waktu Paruh": 7.039, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 2.342*10**(7), "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 237, "Waktu Paruh": 6.747, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 4.47, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 239, "Waktu Paruh": 23.45, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 240, "Waktu Paruh": 14.1, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 241, "Waktu Paruh": 5, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 242, "Waktu Paruh": 16.83, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 93 Neptunium
    [
        {"Massa Atom": 225, "Waktu Paruh": 2, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 226, "Waktu Paruh": 35, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 227, "Waktu Paruh": 510, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 228, "Waktu Paruh": 1.023, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 229, "Waktu Paruh": 4, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 230, "Waktu Paruh": 4.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 231, "Waktu Paruh": 48.83, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 232, "Waktu Paruh": 14.7, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 233, "Waktu Paruh": 36.16, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 4.39, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 235, "Waktu Paruh": 1.08, "Satuan Paruh": "tahun", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 153000, "Satuan Paruh": "tahun", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 237, "Waktu Paruh": 2.144*10**(6), "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 87.8, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 239, "Waktu Paruh": 2.116, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 240, "Waktu Paruh": 1.03, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 241, "Waktu Paruh": 13.9, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 242, "Waktu Paruh": 2.16, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 243, "Waktu Paruh": 1.85, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 244, "Waktu Paruh": 2.29, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 94 Plutonium
    [
        {"Massa Atom": 228, "Waktu Paruh": 1.1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 229, "Waktu Paruh": 1.5, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 230, "Waktu Paruh": 1.7, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 231, "Waktu Paruh": 8.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 232, "Waktu Paruh": 33.8, "Satuan Paruh": "menit", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 233, "Waktu Paruh": 20.9, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 8.8, "Satuan Paruh": "jam", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 235, "Waktu Paruh": 25.3, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 2.858, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 237, "Waktu Paruh": 45.25, "Satuan Paruh": "hari", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 87.8, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 239, "Waktu Paruh": 24110, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 240, "Waktu Paruh": 6561, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 241, "Waktu Paruh": 14.29, "Satuan Paruh": "tahun", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 242, "Waktu Paruh": 374175.5, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 243, "Waktu Paruh": 4.95, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 244, "Waktu Paruh": 7.9, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 245, "Waktu Paruh": 10.5, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 246, "Waktu Paruh": 10.8, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 247, "Waktu Paruh": 2.26, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 95 Americium
    [
        {"Massa Atom": 231, "Waktu Paruh": 30, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 232, "Waktu Paruh": 1.31, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 233, "Waktu Paruh": 3.16, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 2.316, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 235, "Waktu Paruh": 9.83, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 3.6, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 237, "Waktu Paruh": 1.2, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 1.638, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 239, "Waktu Paruh": 11.8, "Satuan Paruh": "jam", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 240, "Waktu Paruh": 2.118, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 241, "Waktu Paruh": 432.52, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 242, "Waktu Paruh": 16.019, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 243, "Waktu Paruh": 7388.38, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 244, "Waktu Paruh": 10.1, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 245, "Waktu Paruh": 2.05, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 246, "Waktu Paruh": 38.3, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 247, "Waktu Paruh": 23.3, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 248, "Waktu Paruh": 10, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 249, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 96 Kurium
    [
        {"Massa Atom": 233, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 234, "Waktu Paruh": 51, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 235, "Waktu Paruh":5, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 10, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 237, "Waktu Paruh": 20, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 2.38, "Satuan Paruh": "jam", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 239, "Waktu Paruh": 2.9, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 240, "Waktu Paruh": 26.62, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 241, "Waktu Paruh": 32.7, "Satuan Paruh": "hari", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 242, "Waktu Paruh": 162.8472, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 243, "Waktu Paruh": 29.1, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 244, "Waktu Paruh": 18.1, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 245, "Waktu Paruh": 8561.6, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 246, "Waktu Paruh": 4756.468, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 247, "Waktu Paruh": 1.56, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 248, "Waktu Paruh": 348807.7, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 249, "Waktu Paruh": 1.069, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 250, "Waktu Paruh": 8304.79, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 251, "Waktu Paruh": 16.83, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 252, "Waktu Paruh": 2, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 97 Berkelium
    [
        {"Massa Atom": 235, "Waktu Paruh": 20, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 236, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 237, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 2.4, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 239, "Waktu Paruh": 3.3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 240, "Waktu Paruh": 4.83, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 241, "Waktu Paruh": 4.6, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 242, "Waktu Paruh": 7, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 243, "Waktu Paruh": 4.4, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 244, "Waktu Paruh": 4.35, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 245, "Waktu Paruh": 4.942, "Satuan Paruh": "hari", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 246, "Waktu Paruh": 1.851, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 247, "Waktu Paruh": 1379.3759, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 248, "Waktu Paruh": 9.512, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 249, "Waktu Paruh": 329.861, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 250, "Waktu Paruh": 3.21, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 251, "Waktu Paruh": 55.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 252, "Waktu Paruh": 1.83, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 253, "Waktu Paruh": 10, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 254, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 98 Kalifornium
    [
        {"Massa Atom": 237, "Waktu Paruh": 2.1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 238, "Waktu Paruh": 21.1, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 239, "Waktu Paruh": 39, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 240, "Waktu Paruh": 57.6, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 241, "Waktu Paruh": 3.78, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 242, "Waktu Paruh": 3.7, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 243, "Waktu Paruh": 10.7, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 244, "Waktu Paruh": 19.4, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 245, "Waktu Paruh": 45, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 246, "Waktu Paruh": 1.4875, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 247, "Waktu Paruh": 3.1, "Satuan Paruh": "jam", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 248, "Waktu Paruh": 333.5, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 249, "Waktu Paruh": 351, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 250, "Waktu Paruh": 13.08, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 251, "Waktu Paruh": 898, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 252, "Waktu Paruh": 2.645, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 253, "Waktu Paruh": 17.8125, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 254, "Waktu Paruh": 60.532, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 255, "Waktu Paruh": 1.416, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 12.3, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]}
    ],
    # Unsur 99 Einsteinium
    [
        {"Massa Atom": 240, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 241, "Waktu Paruh": 8, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 242, "Waktu Paruh": 13.5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 243, "Waktu Paruh": 21, "Satuan Paruh": "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 244, "Waktu Paruh": 37, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 245, "Waktu Paruh": 1.1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 246, "Waktu Paruh": 7.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 247, "Waktu Paruh": 4.55, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 248, "Waktu Paruh": 26.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 249, "Waktu Paruh": 1.703, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 250, "Waktu Paruh": 8.61, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 251, "Waktu Paruh": 1.38, "Satuan Paruh": "hari", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 252, "Waktu Paruh": 1.292, "Satuan Paruh": "tahun", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 253, "Waktu Paruh": 20.474, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 254, "Waktu Paruh": 275.694, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 255, "Waktu Paruh": 39.81, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 25.4, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 257, "Waktu Paruh": 7.754, "Satuan Paruh": "hari", "Peluruhan" : ["Beta Minus"], "Orde" : [1]},
        {"Massa Atom": 258, "Waktu Paruh": 3.3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 100 Fermium
    [
        {"Massa Atom": 242, "Waktu Paruh": 800, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 243, "Waktu Paruh": 180, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 244, "Waktu Paruh": 3.3, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 245, "Waktu Paruh": 4.3, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 246, "Waktu Paruh": 1.1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 247, "Waktu Paruh": 29, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 248, "Waktu Paruh": 36, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 249, "Waktu Paruh": 2.596, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 250, "Waktu Paruh": 30, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 251, "Waktu Paruh": 5.27, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 252, "Waktu Paruh": 1.057, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 253, "Waktu Paruh": 3.009, "Satuan Paruh": "hari", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 254, "Waktu Paruh": 3.24, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 255, "Waktu Paruh": 20.06, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 2.626, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 257, "Waktu Paruh": 100.497, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 258, "Waktu Paruh": 370, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 259, "Waktu Paruh": 1.5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 260, "Waktu Paruh": 4, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 101 Mendelevium
    [
        {"Massa Atom": 255, "Waktu Paruh": 900, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 257, "Waktu Paruh": 1.12, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 248, "Waktu Paruh": 7, "Satuan Paruh": "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 249, "Waktu Paruh": 24, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 250, "Waktu Paruh": 52, "Satuan Paruh": "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 251, "Waktu Paruh": 4, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 252, "Waktu Paruh": 2.33, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 253, "Waktu Paruh": 6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 254, "Waktu Paruh": 10, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 255, "Waktu Paruh": 26.6, "Satuan Paruh": "menit", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 1.27, "Satuan Paruh": "jam", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 257, "Waktu Paruh": 5.527, "Satuan Paruh": "jam", "Peluruhan" : ["Epsilon"], "Orde" : [1]},
        {"Massa Atom": 258, "Waktu Paruh": 51.5, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 259, "Waktu Paruh": 1.61, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 260, "Waktu Paruh": 31.8, "Satuan Paruh": "hari", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 261, "Waktu Paruh": 40, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 262, "Waktu Paruh": 3.33, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 102 Nobelium
    [
        {"Massa Atom": 248, "Waktu Paruh": 2, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 249, "Waktu Paruh": 57, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 250, "Waktu Paruh": 4.2, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 251, "Waktu Paruh": 800, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 252, "Waktu Paruh": 2.44, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 253, "Waktu Paruh": 1.62, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 254, "Waktu Paruh": 51, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 255, "Waktu Paruh": 3.1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 2.91, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 257, "Waktu Paruh": 25, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 258, "Waktu Paruh": 1.2, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 259, "Waktu Paruh": 58.3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 260, "Waktu Paruh": 106, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 261, "Waktu Paruh": 2.7, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 262, "Waktu Paruh": 5, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 263, "Waktu Paruh": 20, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 264, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 103 Lawrensium
    [
        {"Massa Atom": 251, "Waktu Paruh": 150, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 252, "Waktu Paruh": 360, "Satuan Paruh": "milidetik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 253, "Waktu Paruh": 570, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 254, "Waktu Paruh": 13, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 255, "Waktu Paruh": 22, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 27, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 257, "Waktu Paruh": 646, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 258, "Waktu Paruh": 4.1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 259, "Waktu Paruh": 6.2, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 260, "Waktu Paruh": 3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 261, "Waktu Paruh": 38.3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 262, "Waktu Paruh": 4, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 263, "Waktu Paruh": 5.5, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 264, "Waktu Paruh": 10, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 265, "Waktu Paruh": 10, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 266, "Waktu Paruh": 1.1, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 104 Rutherfordium
    [
        {"Massa Atom": 253, "Waktu Paruh": 13, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 254, "Waktu Paruh": 23, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 255, "Waktu Paruh": 1.68, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 6.45, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 257, "Waktu Paruh": 4.7, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 258, "Waktu Paruh": 12, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 259, "Waktu Paruh": 3.2, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 260, "Waktu Paruh": 21, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 261, "Waktu Paruh": 1.083, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 262, "Waktu Paruh": 2.3, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 263, "Waktu Paruh": 10, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 264, "Waktu Paruh": 1.1, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 265, "Waktu Paruh": 13.05, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 266, "Waktu Paruh": 10, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 267, "Waktu Paruh": 5.5, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 268, "Waktu Paruh": 1.1, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 105 Dubnium
    [
        {"Massa Atom": 255, "Waktu Paruh": 1.586, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 256, "Waktu Paruh": 1.586, "Satuan Paruh": "detik", "Peluruhan" : ["Beta Plus"], "Orde" : [1]},
        {"Massa Atom": 257, "Waktu Paruh": 1.5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 258, "Waktu Paruh": 4, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 259, "Waktu Paruh": 510, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 260, "Waktu Paruh": 1.52, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 261, "Waktu Paruh": 1.8, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 262, "Waktu Paruh": 35, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 263, "Waktu Paruh": 27, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 264, "Waktu Paruh": 3.3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 265, "Waktu Paruh": 15, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 266, "Waktu Paruh": 20, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 267, "Waktu Paruh": 1.94, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 268, "Waktu Paruh": 5.5, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 269, "Waktu Paruh": 2.7, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 270, "Waktu Paruh": 1.1, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 106 Seaborgium
    [
        {"Massa Atom": 258, "Waktu Paruh": 2.9, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 259, "Waktu Paruh": 480, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 260, "Waktu Paruh": 3.6, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 261, "Waktu Paruh": 230, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 262, "Waktu Paruh": 6.9, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 263, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 264, "Waktu Paruh": 37, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 265, "Waktu Paruh": 8, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 266, "Waktu Paruh": 21, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 267, "Waktu Paruh": 19, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 268, "Waktu Paruh": 30, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 269, "Waktu Paruh": 35, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 270, "Waktu Paruh": 10, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 271, "Waktu Paruh": 1.94, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 272, "Waktu Paruh": 1.1, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 273, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
    ],
    # Unsur 107 Bohrium
    [
        {"Massa Atom": 260, "Waktu Paruh": 300, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 261, "Waktu Paruh": 12, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 262, "Waktu Paruh": 290, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 263, "Waktu Paruh": 200, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 264, "Waktu Paruh": 440, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 265, "Waktu Paruh": 900, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 266, "Waktu Paruh": 5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 267, "Waktu Paruh": 22, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 268, "Waktu Paruh": 25, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 269, "Waktu Paruh": 25, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 270, "Waktu Paruh": 30, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 271, "Waktu Paruh": 40, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 272, "Waktu Paruh": 1.6, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 273, "Waktu Paruh": 1.5, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 274, "Waktu Paruh": 1.5, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 275, "Waktu Paruh": 40, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 108 Hasium
    [
        {"Massa Atom": 263, "Waktu Paruh": 1, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 264, "Waktu Paruh": 800, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 265, "Waktu Paruh": 2, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 266, "Waktu Paruh": 2.3, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 267, "Waktu Paruh": 52, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 268, "Waktu Paruh": 2, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 269, "Waktu Paruh": 27, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 270, "Waktu Paruh": 3.6, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 271, "Waktu Paruh": 40, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 272, "Waktu Paruh": 40, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 273, "Waktu Paruh": 50, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 274, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 275, "Waktu Paruh": 30, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 276, "Waktu Paruh": 1.1, "Satuan Paruh": "jam", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 277, "Waktu Paruh": 40, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 109 Meitnerium
    [
        {"Massa Atom": 265, "Waktu Paruh": 2, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 266, "Waktu Paruh": 1.2, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 267, "Waktu Paruh": 9.9, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 268, "Waktu Paruh": 53, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 269, "Waktu Paruh": 200, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 270, "Waktu Paruh": 2, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 271, "Waktu Paruh": 5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 272, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 273, "Waktu Paruh": 20, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 274, "Waktu Paruh": 20, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 275, "Waktu Paruh": 30, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 276, "Waktu Paruh": 40, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 277, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 278, "Waktu Paruh": 30, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 279, "Waktu Paruh": 6.6, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 110 Darmstadtium
    [
        {"Massa Atom": 267, "Waktu Paruh": 10, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 268, "Waktu Paruh": 100, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 269, "Waktu Paruh": 230, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 270, "Waktu Paruh": 100, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 271, "Waktu Paruh": 1.63, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 272, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 273, "Waktu Paruh": 170, "Satuan Paruh": "mikrodetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 274, "Waktu Paruh": 2, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 275, "Waktu Paruh": 2, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 276, "Waktu Paruh": 5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 277, "Waktu Paruh": 5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 278, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 279, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 280, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 281, "Waktu Paruh": 4, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 111 Roentgenium
    [
        {"Massa Atom": 272, "Waktu Paruh": 2, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 273, "Waktu Paruh": 5, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 274, "Waktu Paruh": 5, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 275, "Waktu Paruh": 9.9, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 276, "Waktu Paruh": 100, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 277, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 278, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 279, "Waktu Paruh": 3, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 280, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 281, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 282, "Waktu Paruh": 3.3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 283, "Waktu Paruh": 10, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 112 Kopernicium
    [
        {"Massa Atom": 277, "Waktu Paruh": 1.1, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 278, "Waktu Paruh": 9.9, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 279, "Waktu Paruh": 100, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 280, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 281, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 282, "Waktu Paruh": 30, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 283, "Waktu Paruh": 4.16, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 284, "Waktu Paruh": 11, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 285, "Waktu Paruh": 40, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 113 Nihonium
    [
        {"Massa Atom": 283, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 284, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 285, "Waktu Paruh": 1.6, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 286, "Waktu Paruh": 5, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 287, "Waktu Paruh": 20, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 114 Flerovium
    [
        {"Massa Atom": 285, "Waktu Paruh": 5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 286, "Waktu Paruh": 5, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 287, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 288, "Waktu Paruh": 2.8, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 289, "Waktu Paruh": 1.3, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 115 Moskovium
    [
        {"Massa Atom": 287, "Waktu Paruh": 500, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 288, "Waktu Paruh": 1, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 289, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 290, "Waktu Paruh": 9.9, "Satuan Paruh": "detik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 291, "Waktu Paruh": 1, "Satuan Paruh": "menit", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 116 Livermorium
    [
        {"Massa Atom": 289, "Waktu Paruh": 10, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 290, "Waktu Paruh": 8, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 291, "Waktu Paruh": 18, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 292, "Waktu Paruh": 53, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 293, "Waktu Paruh": 54, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 117 Tenesin
    [
        {"Massa Atom": 293, "Waktu Paruh": 20, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]},
        {"Massa Atom": 294, "Waktu Paruh": 51, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ],
    # Unsur 118 Oganeson
    [
        {"Massa Atom": 294, "Waktu Paruh": 0.69, "Satuan Paruh": "milidetik", "Peluruhan" : ["Alpha"], "Orde" : [1]}
    ]
]

## METODE NUMERIK
# PDB Numerik
def RK4_Peluruhan (N_awal : float, waktu_luruh : float, waktu_paruh : float) :
    # Inisiasi
    dt = waktu_luruh/100
    ts = int(waktu_luruh/dt)
    t = np.zeros(ts + 1)
    N = np.zeros(ts + 1)
    lmbd = 0.693/waktu_paruh

    # Data Awal
    t[0] = 0
    N[0] = N_awal

    # Runge Kutta Orde 4
    for i in range (1,ts+1) :
        k1 = -lmbd * N[i-1]
        k2 = -lmbd * (N[i-1] + 0.5 * dt * k1)
        k3 = -lmbd * (N[i-1] + 0.5 * dt * k2)
        k4 = -lmbd * (N[i-1] + dt * k3)

        N[i] = N[i-1] + dt * (k1 + 2*k2 + 2*k3 + k4) / 6.0
        t[i] = t[i-1] + dt
    return t, N

# Interpolasi Numerik
def InterpolasiLagrange (x : list, y : list) :
    n = len(x)
    xp = np.linspace(float(x[0]), float(x[-1]), 10)
    yp = []
    for data in range (len(xp)) :
        hasil = 0
        for i in range (n) :
            kali = 1
            for j in range (n) :
                if j != i :
                    if x[i] == x[j] :
                        kali *= 1
                    else :
                        kali *= (xp[data] - x[j])/(x[i] - x[j])
            
            # Untuk Plot linear
            if x[i] == xp[data] :
                if data == 1 :
                    hasil = y[0]
                    break
                elif data == (len(xp) -1)  :
                    hasil = y[-1]
                    break
                else : 
                    hasil = y[0] + ((min(y) - max(y))/10)*data
                    break
            # Untuk Plot non-linear
            else :
                hasil += y[i]*kali
        yp.append(hasil)
    return xp, yp

## INPUT BERBAGAI PARAMETER
# Input nomor atom
def NomorAtom () :
    while True :
        try :
            nomor_atom = int(input("> Masukkan nomor atom yang akan diamati : "))
            if not 1 <= nomor_atom <= len(Unsur) + 1 :
                print("ERROR...Tolong masukkan nomor atom dari 1 hingga 118!\n")
                continue
            elif Isotopes[nomor_atom - 1] == [None]:
                print("Maaf, tidak terdapat data isotop dari unsur tersebut, silahkan memilih kembail...\n")
                continue
            else :
                break
        except ValueError :
            print("ERROR...Tolong masukkan input berupa integer!\n")
            continue
    return nomor_atom

# Input Waktu Peluruhan
def WaktuPeluruhan () :
    while True :
        try :
            waktu_luruh = float(input(f'> {"Masukkan lamanya waktu peluruhan":35} : '))
            break
        except ValueError :
            print("ERROR...Tolong masukkan input berupa angka!\n")
            continue
    return waktu_luruh

# Input Jumlah
def InputJumlah () :
    while True :
        try :
            input_jumlah = float(input("> Masukkan jumlah awal yang akan diamati : "))
            break
        except ValueError :
            print("ERROR...Tolong masukkan input berupa angka!\n")
            continue
    return input_jumlah

## KONVERSI SATUAN
def KonversiSatuan (nilai:float, satuan_awal:str, satuan_akhir:str, satuan:list) :
    # Mengambil skala berdasarkan satuan waktu
    for i in range (len(satuan)) :
        if satuan_awal == satuan[i]["Satuan"] :
            skala_awal : float = satuan[i]["skala"]
        if satuan_akhir == satuan[i]["Satuan"] :
            skala_akhir : float = satuan[i]["skala"]
    # Rasio skala
    rasio = skala_awal/skala_akhir
    # Kondisi nilai berdasarkan satuan waktu
    while True :
        if satuan_awal == satuan_akhir :
            break
        else :
            nilai = nilai*rasio
            break
    return nilai

## SATUAN FISIKA
# Satuan Waktu (skala detik)
waktu = "satuan waktu"
SatuanWaktu = [
    {"Satuan" : "quectodetik", "skala" : 10**(-30)},{"Satuan" : "rontodetik", "skala" : 10**(-27)},{"Satuan" : "yoktodetik", "skala" : 10**(-24)},
    {"Satuan" : "zeptodetik", "skala" : 10**(-21)},{"Satuan" : "attodetik", "skala" : 10**(-18)},{"Satuan" : "femtodetik", "satuan" : 10**(-15)},
    {"Satuan" : "pikodetik", "skala" : 10**(-12)},{"Satuan" : "nanodetik", "skala" : 10**(-9)},{"Satuan" : "mikrodetik", "skala" : 10**(-6)},
    {"Satuan" : "milidetik", "skala" : 10**(-3)},{"Satuan" : "sentidetik", "skala" : 10**(-2)},{"Satuan" : "desidetik", "skala" : 10**(-1)},
    {"Satuan" : "detik", "skala" : 1},{"Satuan" : "dekadetik", "skala" : 10},{"Satuan" : "hektodetik", "skala" : 10**2},{"Satuan" : "kilodetik", "skala" : 10**3},
    {"Satuan" : "megadetik", "skala" : 10**6},{"Satuan" : "gigadetik", "skala" : 10**9},{"Satuan" : "teradetik", "skala" : 10**12},{"Satuan" : "petadetik", "skala" : 10**15},
    {"Satuan" : "exadetik", "skala" : 10**18},{"Satuan" : "zettadetik", "skala" : 10**21},{"Satuan" : "yottadetik", "skala" : 10**24},
    {"Satuan" : "ronnadetik", "skala" : 10**27},{"Satuan" : "quettadetik", "skala" : 10**30},{"Satuan" : "menit", "skala" : 60},{"Satuan" : "jam", "skala" : 3600},
    {"Satuan" : "hari", "skala" : 86400},{"Satuan" : "minggu", "skala" : 604800},{"Satuan" : "bulan", "skala" : 2592*10**3},{"Satuan" : "tahun", "skala" : 365*30*24*3600},
    {"Satuan" : "abad", "skala" : 100*365*30*24*3600},{"Satuan" : "milenium", "skala" : 1000*365*30*24*3600},{"Satuan" : "tahun galaksi", "skala" : 2.3*10**8*365*30*24*3600}
]

# Satuan Massa (skala gram)
massa = "satuan massa"
SatuanMassa = [
    {"Satuan" : "quectogram", "skala" : 10**(-30)},{"Satuan" : "rontogram", "skala" : 10**(-27)},{"Satuan" : "yoktogram", "skala" : 10**(-24)},
    {"Satuan" : "zeptogram", "skala" : 10**(-21)},{"Satuan" : "attogram", "skala" : 10**(-18)},{"Satuan" : "femtogram", "satuan" : 10**(-15)},
    {"Satuan" : "pikogram", "skala" : 10**(-12)},{"Satuan" : "nanogram", "skala" : 10**(-9)},{"Satuan" : "mikrogram", "skala" : 10**(-6)},
    {"Satuan" : "miligram", "skala" : 10**(-3)},{"Satuan" : "sentigram", "skala" : 10**(-2)},{"Satuan" : "desigram", "skala" : 10**(-1)},
    {"Satuan" : "gram", "skala" : 1},{"Satuan" : "dekagram", "skala" : 10},{"Satuan" : "hektogram", "skala" : 10**2},{"Satuan" : "kilogram", "skala" : 10**3},
    {"Satuan" : "kuintal", "skala" : 10**5},{"Satuan" : "megagram (ton)", "skala" : 10**6},{"Satuan" : "gigagram", "skala" : 10**9},{"Satuan" : "teragram", "skala" : 10**12},
    {"Satuan" : "petagram", "skala" : 10**15},{"Satuan" : "exagram", "skala" : 10**18},{"Satuan" : "zettagram", "skala" : 10**21},{"Satuan" : "yottagram", "skala" : 10**24},
    {"Satuan" : "ronnagram", "skala" : 10**27},{"Satuan" : "quettagram", "skala" : 10**30}
]

## PROGRAM PILIHAN MENU
# Menu Peluruhan unsur radioaktif
def peluruhan () :
    # Menginput isotop dan keadaan peluruhannya
    while True :
        # Judul dan subjudul
        print(f'\n{"="*50}\n{"||"} {"PELURUHAN RADIOISOTOP".center(44," ")} {"||"}\n{"="*50}\n')
        print("[ Memilih Isotop ]\n")
        # Input nomor atom dan nama unsur
        nomor_atom = NomorAtom()
        nama_unsur = f'{Unsur[nomor_atom - 1]["Nama"]}-'
        # Menu dan pilihan isotop
        MenuPilihan(Isotopes[nomor_atom - 1], "Massa Atom", "isotop", nama_unsur)
        while True :
            pilihan = PilihAngka(1,len(Isotopes[nomor_atom - 1]))
            # Radioisotop atau bukan
            if Isotopes[nomor_atom - 1][pilihan-1]["Peluruhan"] == ["Stabil"]:
                print("Maaf, isotop yang anda pilih tidak termasuk dalam radioisotop\nkarena merupakan isotop yang stabil, silahkan memilih kembail...\n")
                continue
            else :
                massa_atom = Isotopes[nomor_atom - 1][pilihan-1]["Massa Atom"]
                waktu_paruh = Isotopes[nomor_atom - 1][pilihan-1]["Waktu Paruh"]
                satuan_paruh = Isotopes[nomor_atom - 1][pilihan-1]["Satuan Paruh"]
                print(f'[SUKSES] Baik, radioisotop yang anda pilih adalah {nama_unsur}{massa_atom}\ndengan waktu paruh sebesar {waktu_paruh:,} {satuan_paruh}\n')
                break
        
        # Menginput jumlah awal
        print("[ Menginput Jumlah Awal ]\n")
        while True :
            pilihan = input("> Dinyatakan dalam apakah jumlah awal radioisotop tersebut ?\n  1. Partikel.\n  2. Massa.\n  Nomor Pilihan (1/2): ")
            print()
            # Partikel
            if pilihan == "1" :
                satuan_jumlah = "partikel"
                jenis = "jumlah"
                print(f'  Satuan Jumlah Awal = {satuan_jumlah}\n')
                break
            # Massa
            elif pilihan == "2" :
                MenuPilihan(SatuanMassa, "Satuan", massa, None)
                print("Pilihlah satuan massa awal partikel berdasarkan menu tersebut!")
                satuan_jumlah = SatuanMassa[PilihAngka(1,len(SatuanMassa)+1)-1]["Satuan"]
                jenis = "massa"
                print(f'  Satuan Jumlah Awal = {satuan_jumlah}\n')
                break
            # Lainnya
            else :
                print("ERROR...Tolong masukkan nomor pilihan yang sesuai1\n")
                continue
        jumlah_awal = InputJumlah()

        # Menginput waktu peluruhan
        print("\n[ Menginput Lamanya Waktu Peluruhan ]\n")
        MenuPilihan(SatuanWaktu, "Satuan", waktu, None)
        # Pengulangan apabila melebihi batas
        while True :
            print("Pilihlah satuan waktu peluruhan berdasarkan menu tersebut!")
            satuan_luruh = SatuanWaktu[PilihAngka(1,len(SatuanWaktu)+1)-1]["Satuan"]
            print(f'  Satuan Waktu Peluruhan = {satuan_luruh}\n')
            waktu_luruh = WaktuPeluruhan()

            # Skala berdasarkan satuan waktu dalam detik
            for i in range (len(SatuanWaktu)) :
                if SatuanWaktu[i]["Satuan"] == satuan_luruh :
                    skala_luruh = SatuanWaktu[i]["skala"]
                if SatuanWaktu[i]["Satuan"] == satuan_paruh :
                    skala_paruh = SatuanWaktu[i]["skala"]

            # Konversi waktu peluruhan atau waktu paruh radioisotop
            if skala_luruh > skala_paruh :
                satuan_utama = satuan_paruh
                rasio = skala_luruh/skala_paruh
                waktu_luruh = KonversiSatuan(waktu_luruh, satuan_luruh, satuan_paruh, SatuanWaktu)
            elif skala_paruh > skala_luruh :
                satuan_utama = satuan_luruh
                rasio = skala_paruh/skala_luruh
                waktu_paruh = KonversiSatuan(waktu_paruh, satuan_paruh, satuan_luruh, SatuanWaktu)

            if not 10**(-7) <= rasio <= 10**7 :
                print(f'[DITOLAK] Maaf, perbandingan antara paruh waktu radioisotop\ndengan waktu peluruhan di luar interval aman (10^(-7) hingga 10^7)\nmohon untuk menginput kembali waktu peluruhan...\n')
                continue
            else :
                break
        
        # Komputasi
        print("\n[ Komputasi Peluruhan ]\n")
        print(f'\nWaktu paruh = {float(f"{waktu_paruh:5.3e}"):,}\nWaktu Peluruhan = {float(f"{waktu_luruh:5.3e}"):,}\nSatuan Utama = {satuan_utama}\n')
        print(f'Sedang melakukan komputasi, mohon tunggu sebentar...')
        t, N = RK4_Peluruhan(jumlah_awal, waktu_luruh, waktu_paruh)
        print(f'Komputasi telah selesai, silahkan dapat menampilkan grafik...\n')

        # Plot Grafik
        plt.get_current_fig_manager().set_window_title(f"Grafik Peluruhan {nama_unsur.capitalize()}{massa_atom}")
        plt.title(f'Peluruhan {nama_unsur}{massa_atom}\nWaktu Paruh = {waktu_paruh:5.3e} {satuan_paruh.capitalize()}\n')
        plt.ticklabel_format(axis = 'both', style = 'sci', scilimits = (-3,5))
        plt.plot(t, N, label = f"Peluruhan {nama_unsur}{massa_atom}")
        plt.plot(waktu_luruh, N[-1], "or", label = f"Kondisi Akhir")
        plt.plot(t[0], N[0], "og", label = f"Kondisi Awal")
        plt.autoscale(enable=True, axis='both')
        plt.xlabel(f"Waktu ({satuan_utama})")
        plt.ylabel(f"{jenis.capitalize()} ({satuan_jumlah.capitalize()})")
        plt.grid(axis = 'both')
        plt.legend()

        # Menampilkan Grafik
        print(f"\n[ Menampilkan Grafik ]")
        print(f"Apakah anda ingin menampilkan grafik peluruhan {nama_unsur}{massa_atom} ?")
        pilihan = PilihYaTidak()
        if pilihan == "ya" :
            print(f'Baik, memuat grafik peluruhan {nama_unsur}{massa_atom}, mohon tunggu sebentar...')
            plt.show()
            print(f'Grafik Peluruhan {nama_unsur}{massa_atom} selesai ditampilkan...\n')
        
        # Menyimpan Data txt
        print(f"\n[ Menyimpan Data ]")
        print(f"Apakah anda ingin menyimpan data peluruhan {nama_unsur}{massa_atom} sebagai txt ?")
        pilihan = PilihYaTidak()
        if pilihan == "ya" :
            print(f'Baik, sedang menyimpan data, mohon tunggu sebentar...\n')
            header = [f"Waktu Peluruhan ({satuan_utama})", f"{jenis.capitalize()} ({satuan_jumlah})"]
            nama_file = f"Data Peluruhan {nama_unsur}{massa_atom}"
            data = [[i for i in t], [i for i in N]]
            SaveData(header, data, nama_file)
            print(f'Data berhasil disimpan sebagai txt dengan nama {nama_file}.txt\n')
        
        # Mengulangi Program
        print(f"\n[ Mengulangi Program ]")
        print("Apakah anda ingin mengulangi kembali program ini ?")
        pilihan = PilihYaTidak()
        if pilihan == "ya" :
            print(f'Baik, memuat ulang program...\n\n3...\n\n2...\n\n1...\n\nselesai...\n')
            continue
        else :
            print(f'Baik, kembail ke menu awal...\n\n3...\n\n2...\n\n1...\n\nselesai...\n')
            break
    return

# Menu Jalur kestabilan isotop
def kestabilan ():
    # Pemilihan Radioisotop Awal
    while True :
        # Judul
        print(f'\n{"="*50}\n{"||"} {"JALUR KESTABILAN ISOTOP".center(44," ")} {"||"}\n{"="*50}\n')
        # Menu dan pilihan
        menu_kestabilan = [
            {"Pilihan" : "Pemilihan Radioisotop"},
            {"Pilihan" : "Deret Torium"},
            {"Pilihan" : "Deret Neptunium"},
            {"Pilihan" : "Deret Uranium"},
            {"Pilihan" : "Deret Aktinium"}
        ]
        MenuPilihan(menu_kestabilan, "Pilihan", "Kestabilan Radioisotop", None)
        pilihan = PilihAngka(1,len(menu_kestabilan))
        # Menu 1 Pemilihan Radioisotop
        if pilihan == 1 :
            # Judul dan input nomor atom
            print("[ Pemilihan Radioisotop ]\n")
            # Input nomor atom, nama unsur, dan simbol unsur
            nomor_atom = NomorAtom()
            nama_unsur = f'{Unsur[nomor_atom - 1]["Nama"]}-'
            simbol_unsur = f'{Unsur[nomor_atom - 1]["Simbol"]}'
            # Menu dan pilihan isotop
            MenuPilihan(Isotopes[nomor_atom - 1], "Massa Atom", "isotop", nama_unsur)
            while True :
                pilihan = PilihAngka(1,len(Isotopes[nomor_atom - 1]))
                if Isotopes[nomor_atom - 1][pilihan-1]["Peluruhan"] == ["Stabil"]:
                    print("Maaf, isotop yang anda pilih tidak termasuk dalam radioisotop\nkarena merupakan isotop yang stabil, silahkan memilih kembail...\n")
                    continue
                else :
                    # Inisiasi
                    massa_atom : int = Isotopes[nomor_atom - 1][pilihan-1]["Massa Atom"]
                    waktu_paruh : float= Isotopes[nomor_atom - 1][pilihan-1]["Waktu Paruh"]
                    satuan_paruh : str = Isotopes[nomor_atom - 1][pilihan-1]["Satuan Paruh"]
                    tipe_peluruhan : list = Isotopes[nomor_atom - 1][pilihan-1]["Peluruhan"]
                    orde_peluruhan : list = Isotopes[nomor_atom - 1][pilihan-1]["Orde"]
                    print(f'[SUKSES] Baik, radioisotop yang anda pilih adalah {nama_unsur}{massa_atom}\ndengan waktu paruh sebesar {waktu_paruh:,} {satuan_paruh}')
                    for i in range (len(tipe_peluruhan)) :
                        teks = f'yang mengalami peluruhan '
                        if len(tipe_peluruhan) > 1 and i == 0 :
                            teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]} dan'
                        else :
                            teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]}.\n'
                    print(teks)
                    break
        
        # Menu 2 Deret Torium
        elif pilihan == 2 :
            print("[ Deret Torium ]\n")
            nomor_atom = int(90)
            nama_unsur = "Torium-"
            simbol_unsur = "Th"
            massa_atom = int(232)
            waktu_paruh = float(14.05)
            satuan_paruh = "gigatahun"
            tipe_peluruhan = ["Alpha"]
            orde_peluruhan = [1]
            print(f'[SUKSES] Baik, peluruhan dimulai dari radioisotop {nama_unsur}{massa_atom}\ndengan waktu paruh sebesar {waktu_paruh:,} {satuan_paruh}')
            for i in range (len(tipe_peluruhan)) :
                teks = f'yang mengalami peluruhan '
                if len(tipe_peluruhan) > 1 and i == 0 :
                    teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]} dan'
                else :
                    teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]}.\n'
            print(teks)
        
        # Menu 3 Deret Neptunium
        elif pilihan == 3 :
            print("[ Deret Neptunium ]\n")
            nomor_atom = int(93)
            nama_unsur = "Neptunium-"
            simbol_unsur = "Np"
            massa_atom = int(237)
            waktu_paruh = float(2.114)
            satuan_paruh = "megatahun"
            tipe_peluruhan = ["Alpha"]
            orde_peluruhan = [1]
            print(f'[SUKSES] Baik, peluruhan dimulai dari radioisotop {nama_unsur}{massa_atom}\ndengan waktu paruh sebesar {waktu_paruh:,} {satuan_paruh}')
            for i in range (len(tipe_peluruhan)) :
                teks = f'yang mengalami peluruhan '
                if len(tipe_peluruhan) > 1 and i == 0 :
                    teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]} dan'
                else :
                    teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]}.\n'
            print(teks)

        # Menu 4 Deret Uranium
        elif pilihan == 4 :
            print("[ Deret Uranium ]\n")
            nomor_atom = int(92)
            nama_unsur = "Uranium-"
            simbol_unsur = "U"
            massa_atom = int(238)
            waktu_paruh = float(4.5)
            satuan_paruh = "gigatahun"
            tipe_peluruhan = ["Alpha"]
            orde_peluruhan = [1]
            print(f'[SUKSES] Baik, peluruhan dimulai dari radioisotop {nama_unsur}{massa_atom}\ndengan waktu paruh sebesar {waktu_paruh:,} {satuan_paruh}')
            for i in range (len(tipe_peluruhan)) :
                teks = f'yang mengalami peluruhan '
                if len(tipe_peluruhan) > 1 and i == 0 :
                    teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]} dan'
                else :
                    teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]}.\n'
            print(teks)

        # Menu 5 Deret Aktinium
        else :
            print("[ Deret Aktinium ]\n")
            nomor_atom = int(92)
            nama_unsur = "Uranium"
            simbol_unsur = "U"
            massa_atom = int(235)
            waktu_paruh = float(0.704)
            satuan_paruh = "gigatahun"
            tipe_peluruhan = ["Alpha"]
            orde_peluruhan = [1]
            print(f'[SUKSES] Baik, peluruhan dimulai dari radioisotop {nama_unsur}{massa_atom}\ndengan waktu paruh sebesar {waktu_paruh:,} {satuan_paruh}')
            for i in range (len(tipe_peluruhan)) :
                teks = f'yang mengalami peluruhan '
                if len(tipe_peluruhan) > 1 and i == 0 :
                    teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]} dan'
                else :
                    teks += f'{orde_peluruhan[i]}-{tipe_peluruhan[i]}.\n'
            print(teks)

        # Komputasi dan Plot Grafik
        print("\n[ Komputasi Jalur Kestabilan ]\n")
        print(f'Sedang melakukan komputasi, mohon tunggu sebentar...')

        plt.get_current_fig_manager().set_window_title(f"Grafik Jalur Kestabilan {nama_unsur.capitalize()}{massa_atom}")
        plt.title(f'Jalur Kestabilan {nama_unsur}{massa_atom}\nWaktu Paruh = {waktu_paruh:5.3e} {satuan_paruh.capitalize()}\n')

        # Mengambil Data
        DataNomorAtom, DataMassaAtom, DataNeutron, DataNamaUnsur, DataSimbol, DataWaktuParuh, DataSatuanParuh, DataTipePeluruhan, DataOrdePeluruhan = JalurKestabilan(nomor_atom, massa_atom, nama_unsur, simbol_unsur, waktu_paruh, satuan_paruh, tipe_peluruhan, orde_peluruhan)
        
        # Garis Kestabilan beserta Keterangan Tipe Peluruhan
        for plot in range (len(DataNomorAtom)) :
            teks1 = f'{DataMassaAtom[plot]:3.0f}   '
            teks2 = f'{DataNomorAtom[plot]:3.0f}   '
            teks3 = f'   {DataSimbol[plot]}'
            plt.text(DataNomorAtom[plot], DataNeutron[plot], teks3, fontsize = 14, ha = 'center', va = 'center', bbox = dict(boxstyle = 'square', facecolor = 'white', edgecolor = 'black'))
            plt.text(DataNomorAtom[plot], DataNeutron[plot], teks1, fontsize = 6, ha = 'right', va = 'top')
            plt.text(DataNomorAtom[plot], DataNeutron[plot], teks2, fontsize = 6, ha = 'right', va = 'bottom')
            plt.scatter(DataNomorAtom[plot], DataNeutron[plot], c = 'black', label = f"Isotop")

            # Iterasi untuk menentukan simbol dan warna setiap tipe peluruhan
            simbol = " "
            
            for tipeluruh in range (len(DataTipePeluruhan[plot])) :
                if DataTipePeluruhan[plot][tipeluruh] == "Alpha" :
                    simbol += f"{DataOrdePeluruhan[plot][tipeluruh]}a "
                elif DataTipePeluruhan[plot][tipeluruh] == "Beta Minus":
                    simbol += f"{DataOrdePeluruhan[plot][tipeluruh]}B- "
                elif DataTipePeluruhan[plot][tipeluruh] == "Beta Plus" :
                    simbol += f"{DataOrdePeluruhan[plot][tipeluruh]}B+ "
                elif DataTipePeluruhan[plot][tipeluruh] == "Emisi Proton" :
                    simbol += f"{DataOrdePeluruhan[plot][tipeluruh]}p "
                elif DataTipePeluruhan[plot][tipeluruh] == "Emisi Neutron" :
                    simbol += f"{DataOrdePeluruhan[plot][tipeluruh]}n "
                else :
                    break

            if plot in range (len(DataNomorAtom)-1) :
                # Inisiasi
                panjangx = DataNomorAtom[plot + 1] + DataNomorAtom[plot]
                panjangy = DataNeutron[plot + 1] + DataNeutron[plot]
                Data_Z = [DataNomorAtom[plot]] # Nomor Atom sebelum dan sesudah
                Data_N = [DataNeutron[plot]] # Junlah Neutron sebelum dan sesudah
                # Penambahan
                Data_Z.append(DataNomorAtom[plot + 1])
                Data_N.append(DataNeutron[plot + 1])
                # Plot Interpolasi
                if len(DataTipePeluruhan[plot]) > 1 : warna = 'c'
                Z, N = InterpolasiLagrange(Data_Z,Data_N)
                plt.plot(Z, N)
                plt.text(panjangx/2, panjangy/2, f'${simbol}$', ha = 'center', va = 'center', fontsize = 10, bbox = dict(facecolor = 'white', edgecolor = 'none'))
        
        # Keterangan grafik
        plt.ticklabel_format(axis = 'both', style = 'sci', scilimits = (-3,5))
        plt.autoscale(enable=True, axis='both')
        plt.xlabel(f"{'Nomor Atom'}")
        plt.ylabel(f"{'Neutron Atom'}")
        plt.grid(axis = 'both')
        print(f'Kompuatsi telah selesai, silahkan dapat menampilkan grafik...\n')

        # Menampilkan Grafik
        print(f"\n[ Menampilkan Grafik ]")
        print(f"Apakah anda ingin menampilkan grafik dari\njalur kestabilan radioisotop {nama_unsur}{massa_atom} ?")
        pilihan = PilihYaTidak()
        if pilihan == "ya" :
            print(f'Baik, memuat grafik kestabilan {nama_unsur}{massa_atom}, mohon tunggu sebentar...')
            plt.show()
            print(f'Grafik Jalur Kestabilan {nama_unsur}{massa_atom} selesai ditampilkan...\n')

        # Menyimpan Data txt
        print(f"\n[ Menyimpan Data Jalur Kestabilan ]")
        print(f"Apakah anda ingin menyimpan data jalur kestabilan dari\nradioisotop {nama_unsur}{massa_atom} sebagai txt ?")
        pilihan = PilihYaTidak()
        if pilihan == "ya" :
            print(f'Baik, sedang menyimpan data, mohon tunggu sebentar...')
            header = ["Nomor Atom", 
                      "Nama Isotop", 
                      "Simbol Isotop", 
                      "Massa Isotop", 
                      "Waktu Paruh", 
                      "Satuan Paruh", 
                      "Tipe Peluruhan", 
                      "Orde Peluruhan"]
            nama_file = f"Data Jalur Kestabilan Radioisotop {nama_unsur}{massa_atom}"
            data = [DataNomorAtom,
                    DataNamaUnsur,
                    DataSimbol,
                    DataMassaAtom,
                    DataWaktuParuh,
                    DataSatuanParuh,
                    DataTipePeluruhan,
                    DataOrdePeluruhan]
            SaveData(header, data, nama_file)
            print(f'Data berhasil disimpan sebagai txt dengan nama {nama_file}.txt\n')

        # Mengulangi Program
        print(f"\n[ Mengulangi Program ]")
        print("Apakah anda ingin mengulangi kembali program ini ?")
        pilihan = PilihYaTidak()
        if pilihan == "ya" :
            print(f'Baik, memuat ulang program...\n\n3...\n\n2...\n\n1...\n\nselesai...\n')
            continue
        else :
            print(f'Baik, kembail ke menu awal...\n\n3...\n\n2...\n\n1...\n\nselesai...\n')
            break
    return

# Komputasi Jalur Kestabilan
def JalurKestabilan(nomor_atom : int, 
                    massa_atom : int, 
                    nama_unsur : str, 
                    simbol_unsur : str, 
                    waktu_paruh : float, 
                    satuan_paruh : str, 
                    tipe_peluruhan : list, 
                    orde_peluruhan : list) :
    # Inisiasi
    DataNomorAtom = [nomor_atom] # Z
    DataMassaAtom = [massa_atom] # A
    DataNeutron = [massa_atom-nomor_atom] # N
    DataNamaUnsur = [nama_unsur] # nama
    DataSimbol = [simbol_unsur] # simbol
    DataWaktuParuh = [waktu_paruh] # WP
    DataSatuanParuh = [satuan_paruh] # SP
    DataTipePeluruhan = [tipe_peluruhan] # TP
    DataOrdePeluruhan = [list(orde_peluruhan)] # OP

    # Fungsi Tipe Peluruhan
    # Alpha
    def Alpha(nomor_atom : int, massa_atom : int, orde_peluruhan : int) :
        massa_atom -= 4*orde_peluruhan
        nomor_atom -= 2*orde_peluruhan
        neutron_atom = massa_atom - nomor_atom
        return massa_atom, nomor_atom, neutron_atom
    
    # Beta Minus
    def BetaMinus(nomor_atom : int, massa_atom : int, orde_peluruhan : int) :
        # Massa Atom tetap
        nomor_atom += 1*orde_peluruhan
        neutron_atom = massa_atom - nomor_atom
        return massa_atom, nomor_atom, neutron_atom
    
    # Beta Plus
    def BetaPlus(nomor_atom : int, massa_atom : int, orde_peluruhan : int) :
        # Massa Atom tetap
        nomor_atom -= 1*orde_peluruhan
        neutron_atom = massa_atom - nomor_atom
        return massa_atom, nomor_atom, neutron_atom
    
    # Emisi Proton
    def EmisiProton(nomor_atom : int, massa_atom : int, orde_peluruhan : int) :
        massa_atom -= 1*orde_peluruhan
        nomor_atom -= 1*orde_peluruhan
        neutron_atom = massa_atom - nomor_atom
        return massa_atom, nomor_atom, neutron_atom
    
    # Emisi Neutron
    def EmisiNeutron(nomor_atom : int, massa_atom : int, orde_peluruhan : int) :
        massa_atom -= 1*orde_peluruhan
        # Nomor Atom tetap
        neutron_atom = massa_atom - nomor_atom
        return massa_atom, nomor_atom, neutron_atom
    
    # Komputasi dan Plot Grafik
    while True :
        # Pemberhentian jika stabil
        akhir = "tidak"
        for tipeluruh in tipe_peluruhan :
            if tipeluruh == "Stabil" :
                akhir = "ya"
                break
        if akhir == "ya":
            break

        # Kompuatsi Radioisotop
        for tipeluruh in range (len(tipe_peluruhan)) :
            # Peluruhan Alpha
            if tipe_peluruhan[tipeluruh] == "Alpha" :
                massa_atom, nomor_atom, neutron_atom = Alpha(nomor_atom, massa_atom, orde_peluruhan[tipeluruh])
                nama_unsur = Unsur[nomor_atom - 1]["Nama"]
                simbol_unsur = Unsur[nomor_atom - 1]["Simbol"]
            # Peluruhan Beta Minus
            elif tipe_peluruhan[tipeluruh] == "Beta Minus" :
                massa_atom, nomor_atom, neutron_atom = BetaMinus(nomor_atom, massa_atom, orde_peluruhan[tipeluruh])
                nama_unsur = Unsur[nomor_atom - 1]["Nama"]
                simbol_unsur = Unsur[nomor_atom - 1]["Simbol"]
            # Peluruhan Beta Plus
            elif tipe_peluruhan[tipeluruh] == "Beta Plus" :
                massa_atom, nomor_atom, neutron_atom = BetaPlus(nomor_atom, massa_atom, orde_peluruhan[tipeluruh])
                nama_unsur = Unsur[nomor_atom - 1]["Nama"]
                simbol_unsur = Unsur[nomor_atom - 1]["Simbol"]
            # Peluruhan Emisi Proton
            elif tipe_peluruhan[tipeluruh] == "Emisi Proton" :
                massa_atom, nomor_atom, neutron_atom = EmisiProton(nomor_atom, massa_atom, orde_peluruhan[tipeluruh])
                nama_unsur = Unsur[nomor_atom - 1]["Nama"]
                simbol_unsur = Unsur[nomor_atom - 1]["Simbol"]
            # Peluruhan Emisi Neutron
            elif tipe_peluruhan[tipeluruh] == "Emisi Neutron" :
                massa_atom, nomor_atom, neutron_atom = EmisiNeutron(nomor_atom, massa_atom, orde_peluruhan[tipeluruh])
                nama_unsur = Unsur[nomor_atom - 1]["Nama"]
                simbol_unsur = Unsur[nomor_atom - 1]["Simbol"]

        # Pemberhentian jika tidak terdapat data
        if Isotopes[nomor_atom - 1] == [None]:
            print("\nMaaf, jalur kestabilan tidak sepenuhnya selesai karena tidak terdapat data dari salah satu isotop\ntetapi anda masih dapat menampilkan grafik dan menyimpan datanya sebagai txt...\n")
            break

        # Penentuan Waktu Paruh dan Tipe Peluruhan
        for iso in range (len(Isotopes[nomor_atom - 1])) :
            print(Isotopes[nomor_atom - 1][iso])
            if int(Isotopes[nomor_atom - 1][iso]["Massa Atom"]) == massa_atom :
                waktu_paruh = Isotopes[nomor_atom - 1][iso]["Waktu Paruh"]
                satuan_paruh = Isotopes[nomor_atom - 1][iso]["Satuan Paruh"]
                tipe_peluruhan = Isotopes[nomor_atom - 1][iso]["Peluruhan"]
                orde_peluruhan = Isotopes[nomor_atom - 1][iso]["Orde"]
                break  
        
        # Penambahan Data
        DataNomorAtom.append(nomor_atom)
        DataMassaAtom.append(massa_atom)
        DataNeutron.append(neutron_atom)
        DataNamaUnsur.append(nama_unsur)
        DataSimbol.append(simbol_unsur)
        DataWaktuParuh.append(waktu_paruh)
        DataSatuanParuh.append(satuan_paruh)
        DataTipePeluruhan.append(tipe_peluruhan)
        DataOrdePeluruhan.append(orde_peluruhan)
        
    return DataNomorAtom, DataMassaAtom, DataNeutron, DataNamaUnsur, DataSimbol, DataWaktuParuh, DataSatuanParuh, DataTipePeluruhan, DataOrdePeluruhan
    
## MENU DAN PILIHAN
# Menu Pilihan
def MenuPilihan (isi_menu:list, parameter:str, judul_menu:str, keterangan:any) :
    # inisiasi
    n = len(isi_menu)
    banyak_baris = 6
    lebar_nomor = len(f'{n}') + 1

    hitung = []
    for i in range (n) :
        hitung.append(str(isi_menu[i][parameter]))
    lebar_teks = len(max(hitung, key = len)) + 1

    if keterangan == None :
        lebar_keterangan = 0
        keterangan = ''
    elif keterangan != None :
        lebar_keterangan = len(str(keterangan))
    
    lebar_pilihan = 3 + lebar_nomor + lebar_teks + lebar_keterangan
    lebar_menu = 6 + (int((n-2)/banyak_baris)+1)*(lebar_pilihan)
    maks_lebar_menu = 126
    
    # Pembatasan
    if n <= 8 :
        banyak_baris = n
    while True :
        if lebar_menu > maks_lebar_menu :
            banyak_baris += 1
            lebar_menu = 6 + (int(n/banyak_baris) + 1)*(lebar_pilihan)
            continue
        elif lebar_menu <= maks_lebar_menu :
            break

    # Menampilkan Menu
    print(f"[ {judul_menu.upper()} ]".center(lebar_menu, "="))
    for kolom in range (banyak_baris) :
        tabel = "|| "
        for baris in range (0, n, banyak_baris) :
            indeks = kolom + baris
            if n == banyak_baris :
                indeks = kolom 
            if indeks < len(isi_menu) :
                tabel += f'{indeks+1:{lebar_nomor}}. {keterangan:{lebar_keterangan}}{str(isi_menu[indeks][parameter]).capitalize() + ".":{lebar_teks}} '
            elif indeks >= len(isi_menu) :
                tabel += f'{" "*lebar_pilihan}'
        print(tabel + " ||")
    print(f'{"="*lebar_menu}\n')
    return

# Pilihan Berbasis Angka
def PilihAngka (pilihan_awal:int, pilihan_akhir:int):
    while True :
        try :
            pilihan = int(input("> Masukkan nomor menu yang diinginkan : "))
            if pilihan not in [i for i in range(pilihan_awal,pilihan_akhir+1)] :
                print("ERROR...Tolong masukkan nomor menu yang sesuai!\n")
                continue
            elif pilihan in [i for i in range(pilihan_awal,pilihan_akhir+1)] :
                return pilihan
        except ValueError :
            print("ERROR...Tolong masukkan input berupa integer!\n")
            continue

# Pilihan Berbasis Ya atau Tidak
def PilihYaTidak () :
    while True :
        pilihan = str(input(f"> (ya/tidak) : "))
        if pilihan.lower() == "ya" :
            pilihan = "ya"
            break
        elif pilihan.lower() == "tidak" :
            pilihan = "tidak"
            break
        else:
            print("ERROR...Tolong masukkan ya/tidak!\n")
            continue
    return pilihan

# Menyimpan Data sebagai TXT
def SaveData (header : list[str], data : list, nama_file : str) :
    # Inisiasi komponen
    n = len(header)
    BanyakListData = len(data)
    BanyakData = len(data[BanyakListData-1])
    lebar = []
    for i in range (BanyakListData) :
        for j in range (BanyakData) :
            hitung = 2
            if type(data[i][j]) is list :
                for elem in data[i][j] :
                    hitung += len(str(elem))
            else :
                hitung += len(str(data[i][j]))
            lebar.append(hitung)
    for elem in header :
        lebar.append(len(str(elem)))
    lebar = max(lebar)

    # Pembuatan file
    with open(f"{nama_file}.txt", "a") as file:
        teks = f''
        for i in header :
            teks += f'{i.capitalize():{lebar}}'.center(lebar," ")
            teks += f' | '
        file.write(teks)
        file.write(f'\n{"="*n*(lebar+3)}\n')
        for i in range (BanyakData) :
            baris = f''
            for j in range (BanyakListData) :
                mendata = str(data[j][i])
                baris += f'{mendata:{lebar}}'
                baris += f' | '
            file.write(f"{baris}\n")
        file.write(f'{"="*n*(lebar+3)}\n')
    return

## PROGRAM UTAMA
def main () :
    while True :
        menu = [
        {"Pilihan" : "Peluruhan Radioisotop"},
        {"Pilihan" : "Jalur Kestabilan Radioisotop"},
        {"Pilihan" : "Keluar"}
        ]
        MenuPilihan(menu, "Pilihan", "menu", None)

        pilihan = PilihAngka(1,3)
        if pilihan == 1 :
            peluruhan()
            continue
        elif pilihan == 2 :
            kestabilan()
            continue
        elif pilihan == 3 :
            print("\nBaik, terima kasih telah menggunakan program kami...\n")
            break
    return

if __name__ == "__main__" :
    main()