from ast import Dict
from unittest import result
from numpy import append
from riset import riset1, riset2
import databases

databases.pizza

def addPizza(l=True):
    while(l):
        idPizza=len(databases.pizza)+0
        databases.pizza.append(dict())
        namaPizza=input("Nama: ")
        hargaPizza=int(input("Harga: "))
        try :
            databases.pizza[idPizza]['no']=idPizza
            databases.pizza[idPizza]['nama']=namaPizza
            databases.pizza[idPizza]['harga']=hargaPizza
        except IndexError:
            print(F"Belum ada inputan")
        nakon=input("Masih Mau Lanjut Mengisi Data Pizza? (y/t) = ")
        if(nakon=="y"):
            l=True
        elif(nakon=="t"):
            l=False
            MainProgram()

def viewPizza():
    i=int(input(F"Index berapa = "))
    if databases.pizza[i]==None:
        print(F"Belum ada inputan ")
    else:
        try :
            print(databases.pizza[i])
        except IndexError:
            print(F"ID Pizza tidak ditemukan")  
    nakon=input(F"Kembali ke Main Menu? (y/t): ")
    if (nakon=="y"):
        MainProgram()
    elif(nakon=="t"):
        exitApplication()

def editPizza(l=True):
    riset1(databases.pizza)  
    while(l):
        databases.pizza.append(dict())
        idPizza=int(input(F"Input ID yang mau di edit: "))
        namaPizza=input(F"Edit Nama Pizza: ")
        hargaPizza=int(input(F"Edit Harga pizza: "))
        databases.pizza[idPizza]['no']=idPizza
        databases.pizza[idPizza]['nama']=namaPizza
        databases.pizza[idPizza]['harga']=hargaPizza    
        nakon=input(F"Masih Lanjut Mengedit Data Pizza? (y/t) = ")
        if(nakon=="y"):
            l=True
        elif(nakon=="t"):
            l=False
            MainProgram()

def deletePizza(l=True):
    while(l):
        b=int(input(F"Input ID Pizza yang mau di hapus: "))
        # for i in len(pizza):
        #     if pizza <= i:
        #         pizza.pop(i)
        #     else:    
        #         print("ID Tidak ditemukan")  
        #  
        # if b in pizza:
        #     print("ID Pizza ditemukan")
        #     pizza.pop(b)
        # else:
        #     print("ID Pizza Tidak ditemukan")
        try :
            databases.pizza.pop(b)
        except IndexError:
            print(F"ID Pizza tidak ditemukan")
        # pizza.pop(b)
        # print(pizza)
        nakon=input(F"Masih Lanjut Menghapus Data Pizza? (y/t) = ")
        if(nakon=="y"):
            l=True
        elif(nakon=="t"):
            l=False
            MainProgram()

def viewallPizza(l=True):
    while(l):
        riset1(databases.pizza)
        nakon=input(F"Balik ke Main Menu? (y/t) = ")
        if(nakon=="y"):
            l=False
            MainProgram()
        elif(nakon=="t"):
            l=False
            exitApplication()

def exitApplication():
    riset2()

def switcher(pil): 
    if(pil==1):
        addPizza()
    elif(pil==2):
        viewPizza()
    elif(pil==3):
        viewallPizza()
    elif(pil==4):
        editPizza()
    elif(pil==5):
        deletePizza()
    elif(pil==0):
        exitApplication()  
    try :
        pil<=5
    except IndexError:
        print(F"Pilihan tidak ditemukan")
    return 0

def MainProgram():
    print(F" 0. Keluar\n 1. Tambah Pizza\n 2. Lihat Data Pizza dengan index tertentu\n 3. Lihat Semua data Pizza\n 4. Edit Data Pizza\n 5. Hapus Data Pizza\n")
    pil=int(input(F" Pilih Nomer: "))
    switcher(pil)

MainProgram()