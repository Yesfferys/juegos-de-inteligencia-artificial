#yesfferys
# Ejercicio Nivel 19,reto 6.TRES EN RAYA

import os
import time
import random


def mostrar_tablero(casillas):
	"""
	Vamos a mostrar el tablero con el metodo f-string
	"""
	print(f"			1       |2       |3       ")
	print(f"			    {casillas[0][0]}   |    {casillas[0][1]}   |   {casillas[0][2]}   ")
	print(f"			        |        |        ")
	print(f"			--------+--------+--------")
	print(f"			4       |5       |6       ")
	print(f"			    {casillas[1][0]}   |    {casillas[1][1]}   |   {casillas[1][2]}   ")
	print(f"			        |        |        ")
	print(f"			--------+--------+--------")
	print(f"			7       |8       |9       ")
	print(f"			    {casillas[2][0]}   |    {casillas[2][1]}   |   {casillas[2][2]}   ")
	print(f"			        |        |        ")

def presentacion():
	"""
	Nivel facil: la maquina solo intentara defenderse 
	nivel dificil: la maquina buscara la mejor opcion para ganar
	"""
	print("*"*80)
	print()
	print("*"*30," JUEGO  3 EN RAYA ","*"*30)
	print()
	print(f"				1     |2     |3     ")
	print(f"				      |      |      ")
	print(f"			 	      |      |      ")
	print(f"				------+------+------")
	print(f"				4     |5     |6     ")
	print(f"				      |      |      ")
	print(f"				      |      |      ")
	print(f"				------+------+------")
	print(f"				7     |8     |9     ")
	print(f"				      |      |      ")
	print(f"				      |      |      ")
	print()
	print("*"*23," Tenemos  2  niveles para jugar ","*"*23)
	print()

	print()
	nivel=input("Introduce   1-nivel facil  //  2-nivel dificil --> ")
	while nivel != "1" and nivel != "2":
		print("Asegurate de elegir la opcion '1' o '2'")
		time.sleep(1)
		os.system("cls")
		nivel=input("Asegurate de introducir la opcion -->   1-nivel facil  //  2-nivel dificil --> ")
	nivel=int(nivel)

	ficha=input("Por favor elige una ficha 'X' o 'O' --> ").upper()
	while ficha != "X" and ficha != "O" :
		print("Asegurate de elegir la opcion 'X' o 'O'")
		time.sleep(2)
		os.system("cls")
		ficha=input("Por favor elige una ficha nuevamente 'X' o 'O' --> ").upper()

	return nivel,ficha
	

def opciones_marcadas_lista(jugador,maquina,posiciones_jugador=[],posiciones_maquina=[]):
	"""
	Recibe 2 listas
	Devuelve las opciones marcadas en el tablero
	"""
	matriz=[[" "," "," "],[" "," "," "],[" "," "," "]]

	for posicion in posiciones_jugador:
		if posicion <=3:
			matriz[0][posicion-1]=jugador
		elif posicion >=4 and posicion <=6:
			matriz[1][posicion-4]=jugador
		elif posicion >6 and posicion <10:
			matriz[2][posicion-7]=jugador

	for posicion in posiciones_maquina:
		if posicion <=3:
			matriz[0][posicion-1]=maquina 
		elif posicion >=4 and posicion <=6:
			matriz[1][posicion-4]=maquina
		elif posicion >6 and posicion <10:
			matriz[2][posicion-7]=maquina

	return matriz



def ganador(jugador,matriz):
	"""
	Verifica si hay ganador
	jugador es el tipo de ficha en formato string
	"""
	ganador=False
	#evaluacion horizontal
	if jugador == matriz[0][0] and jugador == matriz[0][1] and jugador == matriz[0][2]:
		ganador=True
	elif jugador == matriz[1][0] and jugador == matriz[1][1] and jugador == matriz[1][2]:
		ganador=True
	elif jugador == matriz[2][0] and jugador == matriz[2][1] and jugador == matriz[2][2]:
		ganador=True

	#evaluacion vertical
	elif jugador == matriz[0][0] and jugador == matriz[1][0] and jugador == matriz[2][0]:
		ganador=True
	elif jugador == matriz[0][1] and jugador == matriz[1][1] and jugador == matriz[2][1]:
		ganador=True
	elif jugador == matriz[0][2] and jugador == matriz[1][2] and jugador == matriz[2][2]:
		ganador=True

	#evaluacion diagonal
	elif jugador == matriz[0][0] and jugador == matriz[1][1] and jugador == matriz[2][2]:
		ganador=True
	elif jugador == matriz[0][2] and jugador == matriz[1][1] and jugador == matriz[2][0]:
		ganador=True
		
	return ganador

def defensa_maquina_facil(matriz,jugador,posiciones_maquina,posiciones_jugador):
	"""
	La maquina solo se defiende
	"""
	opciones=list(range(1,10))

	jugadas_posibles=[opcion for opcion in opciones if opcion not in posiciones_jugador and opcion not in posiciones_maquina]
	maquina=random.choice(jugadas_posibles)

	# 1ra defensa horizontal
	if jugador == matriz[0][0] and jugador == matriz[0][1]:
		if 3 in jugadas_posibles:
			maquina = 3
	elif jugador == matriz[0][0] and jugador == matriz[0][2]:
		if 2 in jugadas_posibles:
			maquina = 2
	elif jugador == matriz[0][1] and jugador == matriz[0][2]:
		if 1 in jugadas_posibles:
			maquina = 1	

	elif jugador == matriz[1][0] and jugador == matriz[1][1]:
		if 6  in jugadas_posibles:
			maquina = 6
	elif jugador == matriz[1][0] and jugador == matriz[1][2]:
		if 5 in jugadas_posibles:
			maquina = 5
	elif jugador == matriz[1][1] and jugador == matriz[1][2]:
		if 4 in jugadas_posibles:		
			maquina = 4

	elif jugador == matriz[2][0] and jugador == matriz[2][1]:
		if 9 in jugadas_posibles:
			maquina = 9
	elif jugador == matriz[2][0] and jugador == matriz[2][2]:
		if 8 in jugadas_posibles:
			maquina = 8
	elif jugador == matriz[2][1] and jugador == matriz[2][2]:
		if 4 in jugadas_posibles:
			maquina = 4

	# verticales
	elif jugador == matriz[0][0] and jugador == matriz[1][0]:
		if 7 in jugadas_posibles:
			maquina = 7
	elif jugador == matriz[0][0] and jugador == matriz[2][0]:
		if 4 in jugadas_posibles:
			maquina = 4
	elif jugador == matriz[2][0] and jugador == matriz[1][0]:
		if 1 in jugadas_posibles:
			maquina = 1	

	elif jugador == matriz[0][1] and jugador == matriz[1][1]:
		if 1 in jugadas_posibles:		
			maquina = 1
	elif jugador == matriz[0][1] and jugador == matriz[2][1]:
		if 5 in jugadas_posibles:		
			maquina = 5
	elif jugador == matriz[1][1] and jugador == matriz[2][1]:
		if 2 in jugadas_posibles:		
			maquina = 2

	elif jugador == matriz[0][2] and jugador == matriz[1][2]:
		if 9 in jugadas_posibles:		
			maquina = 9
	elif jugador == matriz[1][2] and jugador == matriz[2][2]:
		if 3 in jugadas_posibles:
			maquina = 3
	elif jugador == matriz[0][2] and jugador == matriz[2][2]:
		if 6 in jugadas_posibles:
			maquina = 6	

	#diagonal
	elif jugador == matriz[0][0] and jugador == matriz[1][1]:
		if 9 in jugadas_posibles:
			maquina = 9
	elif jugador == matriz[1][1] and jugador == matriz[2][2]:
		if 1 in jugadas_posibles:		
			maquina = 1
	elif jugador == matriz[2][2] and jugador == matriz[0][0]:
		if 5 in jugadas_posibles:
			maquina = 5		
	
	#diagonal
	elif jugador == matriz[0][2] and jugador == matriz[1][1]:
		if 7 in jugadas_posibles:
			maquina = 7
	elif jugador == matriz[1][1] and jugador == matriz[2][0]:
		if 3 in jugadas_posibles:
			maquina = 3
	elif jugador == matriz[2][0] and jugador == matriz[0][2]:
		if 5 in jugadas_posibles:
			maquina = 5

	return maquina

#######################################################################################################################################
def defensa_maquina_dificil(matriz,maquina,posiciones_maquina,posiciones_jugador):
	"""
	La maquina quiere ganar
	"""
	opciones=list(range(1,10))
	jugadas_posibles=[opcion for opcion in opciones if opcion not in posiciones_jugador and opcion not in posiciones_maquina]
	opcion_ganar=False

	# 1ra linea horizontal - ganar
	if maquina == matriz[0][0] and  maquina == matriz[0][1]:
		if 3 in jugadas_posibles:
			maquina = 3
			opcion_ganar=True
	elif maquina == matriz[0][0] and  maquina == matriz[0][2]:
		if 2 in jugadas_posibles:
			maquina = 2
			opcion_ganar=True
	elif maquina == matriz[0][1] and  maquina == matriz[0][2]:
		if 1 in jugadas_posibles:
			maquina = 1
			opcion_ganar=True
	# 2da linea horizontal - ganar
	elif maquina == matriz[1][0] and  maquina == matriz[1][1]:
		if 6  in jugadas_posibles:
			maquina = 6
			opcion_ganar=True
	elif maquina == matriz[1][0] and  maquina == matriz[1][2]:
		if 5 in jugadas_posibles:
			maquina = 5
			opcion_ganar=True
	elif maquina == matriz[1][1] and  maquina == matriz[1][2]:
		if 4 in jugadas_posibles:		
			maquina = 4
			opcion_ganar=True

	elif maquina == matriz[2][0] and  maquina == matriz[2][1]:
		if 9 in jugadas_posibles:
			maquina = 9
			opcion_ganar=True
	elif maquina == matriz[2][0] and  maquina == matriz[2][2]:
		if 8 in jugadas_posibles:
			maquina = 8
			opcion_ganar=True
	elif maquina == matriz[2][1] and  maquina == matriz[2][2]:
		if 4 in jugadas_posibles:
			maquina = 4
			opcion_ganar=True

	# verticales
	elif maquina == matriz[0][0] and  maquina == matriz[1][0]:
		if 7 in jugadas_posibles:
			maquina = 7
			opcion_ganar=True
	elif maquina == matriz[0][0] and maquina == matriz[2][0]:
		if 4 in jugadas_posibles:
			maquina = 4
			opcion_ganar=True
	elif maquina == matriz[2][0] and maquina == matriz[1][0]:
		if 1 in jugadas_posibles:
			maquina = 1	
			opcion_ganar=True

	elif maquina == matriz[0][1] and maquina == matriz[1][1]:
		if 1 in jugadas_posibles:		
			maquina = 1
			opcion_ganar=True
	elif maquina == matriz[0][1] and maquina == matriz[2][1]:
		if 5 in jugadas_posibles:		
			maquina = 5
			opcion_ganar=True
	elif maquina == matriz[1][1] and maquina == matriz[2][1]:
		if 2 in jugadas_posibles:		
			maquina = 2
			opcion_ganar=True

	elif maquina == matriz[0][2] and maquina == matriz[1][2]:
		if 9 in jugadas_posibles:		
			maquina = 9
			opcion_ganar=True
	elif maquina == matriz[1][2] and maquina == matriz[2][2]:
		if 3 in jugadas_posibles:
			maquina = 3
			opcion_ganar=True
	elif maquina == matriz[0][2] and maquina == matriz[2][2]:
		if 6 in jugadas_posibles:
			maquina = 6	
			opcion_ganar=True

	#diagonal
	elif maquina == matriz[0][0] and maquina == matriz[1][1]:
		if 9 in jugadas_posibles:
			maquina = 9
			opcion_ganar=True
	elif maquina == matriz[1][1] and maquina == matriz[2][2]:
		if 1 in jugadas_posibles:		
			maquina = 1
			opcion_ganar=True
	elif maquina == matriz[2][2] and maquina == matriz[0][0]:
		if 5 in jugadas_posibles:
			maquina = 5	
			opcion_ganar=True
	
	#diagonal
	elif maquina == matriz[0][2] and maquina == matriz[1][1]:
		if 7 in jugadas_posibles:
			maquina = 7
			opcion_ganar=True
	elif maquina == matriz[1][1] and maquina == matriz[2][0]:
		if 3 in jugadas_posibles:
			maquina = 3
			opcion_ganar=True
	elif maquina == matriz[2][0] and maquina == matriz[0][2]:
		if 5 in jugadas_posibles:
			maquina = 5
			opcion_ganar=True

	return maquina,opcion_ganar

def condicion_tablero(matriz):
	"""
	evalua el estado del tablero
	"""
	estado_tablero="lleno"
	for i in matriz:
		for j in i:
			if j== " ":
				estado_tablero="disponible"
	return estado_tablero

def opcion_usuario_jugar():
	"""
	Verifica que se introduzca la opcion correcta
	"""
	entrada=input("Porfavor introduce 'Yes' o 'No'").lower()
	opciones=["yes","no"]
	while entrada not in opciones:
		entrada =input("Porfavor asegurate de introducir 'Yes' o 'No'").lower()
		time.sleep(2)
		os.system("cls")
	return entrada

def opcion_jugador():
	"""
	verifica que se introduzcan solo numeros
	verifica que este en un rango de 0 a 9
	"""
	opciones=["1","2","3","4","5","6","7","8","9"]
	opcion_tablero=input("Marca la casilla donde quieres jugar -- > ")
	while opcion_tablero not in opciones:
		opcion_tablero=input("Asegurte de marcar una casilla valida -- (-_-) -- > ")
	return int(opcion_tablero)



def juego():
	"""
	Funcion principal en el juego
	"""
	nivel,ficha=presentacion()
	if nivel==1:

		if ficha=="X":
			jugador=ficha
			maquina="O"
		else:
			jugador="O"
			maquina="X"
		print()
		print("+++  La ficha asociada al jugador es: ",jugador," y a la maquina es: ",maquina," +++")
		print()
		print("+++                    Estamos jugando en el nivel,      >>",  nivel ,"<<        +++")
		print()
		posiciones_jugador=[]
		posiciones_maquina=[]
	

		while juego:
			print()
			opciones_marcadas=opciones_marcadas_lista(jugador,maquina,posiciones_jugador,posiciones_maquina)
			mostrar_tablero(opciones_marcadas)
			estado_tablero=condicion_tablero(opciones_marcadas)
			print()

			if estado_tablero == "disponible":
				posicion_jugador=opcion_jugador()
				
				time.sleep(2)
				os.system("cls")
				print()
				print("Has marcado la posicion",posicion_jugador)
				print()

				if posicion_jugador not in posiciones_jugador and posicion_jugador not in posiciones_maquina:
					posiciones_jugador.append(posicion_jugador)
				else:
					print("Esa posicion ya esta marcada en el tablero")
					continue
					print()

				opciones_marcadas=opciones_marcadas_lista(jugador,maquina,posiciones_jugador,posiciones_maquina)
				mostrar_tablero(opciones_marcadas)

				if ganador(jugador,opciones_marcadas):
					print("has ganado")
					break

				time.sleep(2)
				os.system("cls")
				print()

				posicion_maquina=defensa_maquina_facil(opciones_marcadas,jugador,posiciones_maquina,posiciones_jugador)
				print()
				print("La maquina ha marcado la posicion: ",posicion_maquina)
				posiciones_maquina.append(posicion_maquina)
				opciones_marcadas=opciones_marcadas_lista(jugador,maquina,posiciones_jugador,posiciones_maquina)

				if ganador(maquina,opciones_marcadas):
					print("Ha ganado la maquina")
					print()
					break

				else:
					opciones_marcadas=opciones_marcadas_lista(jugador,maquina,posiciones_jugador,posiciones_maquina)
					print()
					mostrar_tablero(opciones_marcadas)
					time.sleep(2)
					os.system("cls")
					continue

			else:
				print("El tablero esta lleno, Tenemos un empate")
				break
		print("Deseas volver a jugar?")
		jugar=opcion_usuario_jugar()
		
		if jugar=="yes":
			juego()
		elif jugar=="no":
			print("Gracias por jugar")
		

	if nivel==2:

		if ficha=="X":
			jugador=ficha
			maquina="O"
		else:
			jugador="O"
			maquina="X"
		print()
		print("+++  La ficha asociada al jugador es: ",jugador," y a la maquina es: ",maquina," +++")
		print()
		print("+++                    Estamos jugando en el nivel,      >>",  nivel ,"<<        +++")
		print()
		posiciones_jugador=[]
		posiciones_maquina=[]
	

		while juego:
			opciones_marcadas=opciones_marcadas_lista(jugador,maquina,posiciones_jugador,posiciones_maquina)
			mostrar_tablero(opciones_marcadas)
			estado_tablero=condicion_tablero(opciones_marcadas)
			print()

			if estado_tablero == "disponible":
				posicion_jugador=opcion_jugador()
				
				time.sleep(2)
				os.system("cls")
				print()
				print("Has marcado la posicion",posicion_jugador)
				print()

				if posicion_jugador not in posiciones_jugador and posicion_jugador not in posiciones_maquina:
					posiciones_jugador.append(posicion_jugador)
				else:
					print("Esa posicion ya esta marcada en el tablero")
					continue
					print()

				opciones_marcadas=opciones_marcadas_lista(jugador,maquina,posiciones_jugador,posiciones_maquina)
				mostrar_tablero(opciones_marcadas)

				if ganador(jugador,opciones_marcadas):
					print("has ganado")
					break

				time.sleep(2)
				os.system("cls")
				print()

				posicion_maquina,opcion_ganar=defensa_maquina_dificil(opciones_marcadas,maquina,posiciones_maquina,posiciones_jugador)
				if opcion_ganar:
					posicion_maquina=posicion_maquina
				else:
					posicion_maquina=defensa_maquina_facil(opciones_marcadas,jugador,posiciones_maquina,posiciones_jugador)

				print()
				print("La maquina ha marcado la posicion: ",posicion_maquina)
				posiciones_maquina.append(posicion_maquina)
				opciones_marcadas=opciones_marcadas_lista(jugador,maquina,posiciones_jugador,posiciones_maquina)

				if ganador(maquina,opciones_marcadas):
					print("Ha ganado la maquina")
					print()
					break

				else:
					opciones_marcadas=opciones_marcadas_lista(jugador,maquina,posiciones_jugador,posiciones_maquina)
					mostrar_tablero(opciones_marcadas)
					time.sleep(2)
					os.system("cls")
					continue

			else:
				print("El tablero esta lleno, Tenemos un empate")
				break
		print("Deseas volver a jugar?")
		print()
		jugar=opcion_usuario_jugar()
		
		if jugar=="yes":
			juego()
		elif jugar=="no":
			print("Gracias por jugar")	


juego()
