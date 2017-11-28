#Programa sencillo que codifica y decodifica una cadena

import random

def main():
    list = []
    temp = []
    ram = []
    text = input("Introduzca el texto: ")
    for i in text:
       list.append((ord(i)))

    for i in list:
        a = random.randint(32,126)
        ram.append(a)
        flag = i + a
        temp.append(flag)

    list = []
    for i in temp:
        list.append(chr(i))
    print("Texto codificado....")
    print(" ".join(list))

#Seccion para decodificar o salir del programa

    while True:
        opc = input("Desea decodificar?(Si o No): ")
        if opc == 'no' or opc == 'NO':
            print("Adios...")
            break

        else:
            temp = []
            for i in list:
                temp.append(ord(i))
            i = 0
            list = []
            flag = 0
            for i in range(len(temp)):
                flag = temp[i] - ram[i]
                list.append(flag)
            temp=[]
            for i in list:
                temp.append(chr(i))
            print("texto decodificado....")
            print("".join(temp))
            break


main()

