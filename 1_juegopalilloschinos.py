
import os 
import random
import time

def presentacion():

	print(" "*10,"*"*10,"Juegos de los palillos Chinos","*"*10," "*10)
	print()
	print()
	print(" "*19,"Gana quien coje el ultimo palillo"," "*20)
	print()
	print()
	print(" "*25,"1-Facil / 2-Dificil"," "*25)
	print()
	print()
	print("*"*75)
	print()
	
	nivel=input("Elige un nivel (1/2): --> ")

	while nivel !="1" and nivel !="2":
		nivel=input("Elige un nivel (1/2): --> ")
	return nivel 
	print()


def presentacion_1(palillos_en_juego):
	print(" "*10,"*"*10,"Juegos de los palillos Chinos","*"*10," "*10)
	print()
	print()
	print(" "*23,"Habra ",palillos_en_juego," palillos en total"," "*20)
	print()
	print()
	print(" "*18,"Se pueden quitar entre 1 y 3 palillos"," "*25)
	print()
	print()
	print("*"*75)
	print()
	empezar=input("Presiona enter para empezar ...")
	print()

def mostrar_palillos(palillos):
	print(" "*10,"*"*10,"Juegos de los palillos Chinos","*"*10," "*10)
	print()
	for i in range(4):
		for j in range(1,palillos+1):
			print("|",end=" ")
			if j%4==0:
				print(" ",end=" ")
		print("")


def jugador(palillos_en_juego):
	
    while True:
        palillos_retirar_usuario=input("Introduce la cantidad de palillos a retirar - entre 1 y 3: ----> ")
        if palillos_retirar_usuario not in ("1","2","3"):
            continue
        else:
            if int(palillos_retirar_usuario) > palillos_en_juego:
                print("introduce una cantidad menor o igual a palillos en el juego")
                continue
            else:
                palillos_en_juego=palillos_en_juego - int(palillos_retirar_usuario)
                return palillos_en_juego


def maquina_facil(palillos_en_juego):
	print("Turno de la maquina (O_O)** ......Espera")
	time.sleep(2)
	os.system("cls")
	turno=True
	while turno:	
		palillos_retirar_maquina=random.randint(1,3)
		print("La maquina a retirado",palillos_retirar_maquina)
		time.sleep(2)
		if palillos_retirar_maquina <= palillos_en_juego :
			palillos_en_juego=palillos_en_juego - palillos_retirar_maquina
			turno=False
		elif palillos_retirar_maquina > palillos_en_juego:
			print(" La maquina lo esta pensando mejor ")
			continue
	return palillos_en_juego

def maquina_dificil(palillos_en_juego):
	print("Turno de la maquina dificil (¨_¨)** ......")
	time.sleep(2)
	os.system("cls")
	
	if palillos_en_juego % 4 == 3:
		palillos_en_juego=palillos_en_juego-3
	elif palillos_en_juego % 4 == 2:
		palillos_en_juego=palillos_en_juego-2
	elif palillos_en_juego % 4 == 1:
		palillos_en_juego=palillos_en_juego-1
	elif palillos_en_juego % 4 == 0:
		palillos_en_juego=palillos_en_juego-4

	return palillos_en_juego

def evaluar():
    repetir=None
    while repetir != "SI" and repetir !="NO":
        repetir=input("Deseas volver a jugar 'SI' o 'NO'")
        if repetir=="Si" or repetir=="sI":
            repetir="SI"
        if repetir=="No" or repetir=="nO":
            repetir="NO"
    return repetir

def juego():
	
	opcion=presentacion()

	os.system("cls")
	
	palillos_en_juego=random.randint(5,15)

	presentacion_1(palillos_en_juego)

	mostrar_palillos(palillos_en_juego)

	print("")
	print("Elige opcion 1 (inicia:Jugador) o Elige opcion --> 'cualquier tecla' (inicia:Maquina)")
	print()
	inicio_partida=input("Quien inicia primero?: ")
	print("")

	turno_jugador=None        # aca se podria modificar si no , cualquier otro numero distinto a 1 dara turno a la maquina
	if inicio_partida=="1":
		turno_jugador=True
	else:
		turno_jugador=False

	if opcion=="1": 									# 	"1" nivel facil - "2" nivel dificil
		while palillos_en_juego>=1:
			if turno_jugador==True:
				palillos_en_juego=jugador(palillos_en_juego)
				print()
				if palillos_en_juego==0:
					print("Has ganado")
					print()
					print()
					time.sleep(3)
					break
				mostrar_palillos(palillos_en_juego)
				time.sleep(3)
				os.system("cls")
				turno_jugador=False
			else:
				print(" Turno de la maquina......")
				time.sleep(2)
				os.system("cls")
				palillos_en_juego=maquina_facil(palillos_en_juego)
				print()
				if palillos_en_juego==0:
					print("La maquina ha ganado")
					print()
					time.sleep(3)
					break
				mostrar_palillos(palillos_en_juego)
				time.sleep(3)
				turno_jugador=True

	if opcion=="2":
		while palillos_en_juego>=1:
			if turno_jugador==True:
				palillos_en_juego=jugador(palillos_en_juego)
				print()
				if palillos_en_juego==0:
					print("Has ganado")
					print()
					print()
					time.sleep(3)
					break
				mostrar_palillos(palillos_en_juego)
				time.sleep(3)
				os.system("cls")
				turno_jugador=False	
			else:
				print(" Turno de la maquina......")
				time.sleep(2)
				os.system("cls")
				palillos_en_juego=maquina_dificil(palillos_en_juego)
				print()
				if palillos_en_juego==0:
					print("La maquina ha ganado")
					print()
					time.sleep(3)
					break
				mostrar_palillos(palillos_en_juego)
				time.sleep(3)
				turno_jugador=True
				print()
		print()

	repetir=evaluar()

	print()

	if repetir=="SI":
		juego()
	elif repetir=="NO":
		print("Gracias por jugar")
		time.sleep(3)
		os.system("cls")
		



juego()

