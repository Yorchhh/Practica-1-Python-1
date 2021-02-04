'''
EJERCICIO CADENAS
a=3
b=4
print("Antes del cambio")
print("el valor de a es",a)
print ("el valor de b es ",b)
temp = a
a=b
b= temp
print("Despues del cambio")
print("el valor de a es",a)
print ("el valor de b es ",b)'''
'''print("¿Como te llamas?")
nombre=input()
print("¿En que año naciste",nombre,"?")
year=int(input())
edad = 2021- year
#print("Hola",nombre," tienes",edad," años")
if edad<18:
  print("Eres menos de edad")
else:
    print("Eres mayor de edad")'''
'''
print("¿Cuantos invitados vienen?")
invitados=int(input())
if invitados > 5 :
  if invitados <10:
    print("Hoy fiestuki")
  else:
      print("Somos muchos, hay Covid")
else :
  print("Pa eso me veo una peli")
'''
'''Pide dos números, y te da a elegir sumarlos, restarlos o
multiplicarlos
print("Introduce el primer numero, porfavor")
num1=int(input())
print("Introduce el segundo numero, porfavor")
num2= int(input())
print("Elige una operacion:")
print("Sumar(s), Restar(r) o Multiplicar(m)")
operacion=input()
if operacion == "s":
  print("El resultado de la suma es:",num1+num2)
elif operacion == "r":
  print("El resultado de la resta es:",num1-num2)
elif operacion == "m":
  print("El resultado de la multiplicaicon es:",num1*num2)
else :  
 print("Operacion introducida no existente")

lista_extraña = [2,'Hola', 3.5]
print(lista_extraña[0])
print(lista_extraña[1])
print(lista_extraña[2])

Mi_aula = [["Luis","Maria","Juan"],["Gemma","Celeste","Raquel"]]
print(Mi_aula[1][2])
print(Mi_aula[1])
print(len(Mi_aula))
print(len(Mi_aula[1]))

print([2,3]+[4,6])
prueba=[3,4,6,8,12]
print(prueba[1:3])
prueba[2]="Perro"
print(prueba[2])
print(prueba)
del prueba[2]
print(prueba)



letras_dni=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
print("Introduce el numero del DNI (sin letra)")
num = int(input())
resto = num%23
letra = letras_dni[resto]
print("La letra de su dni es",letra)

nombres=['Paco','María','Raquel']
print("Lista previa")
print(nombres)
print("Introduzca un nuevo nombre para introducir en la lista, por favor")
nuevo_nombre=input()
nombres.append(nuevo_nombre)
print("Lista Modificada")
print(nombres)
print("Lista Previa 2")
print("Introduzca otro nombre a la lista")
nombre2=input()
print("¿En que posicion quiere insertar el nombre?")
pos=int(input())
nombres.insert(pos,nombre2)
print("Lista Modificada 2")
print(nombres)'''
'''Programa para ver el funcionamiento de distintos bucles
print("Hagamos una lista de jugadores de basket")
equipo=[]#Lista vacia
print("Introduce el nombre del primer jugador")
equipo.append(input())
print("Introduce el nombre del segundo jugador")
equipo.append(input())
#Esto es un toston, por eso realizaremosun bucle for
for i in range(5):
  print("Introduce el nombre del judador numero",i+1)
  equipo.append(input())
print(equipo)'''
'''Programa que muestre los 100 primeros numeros pares
print("Estos son los 100 primeros numeros pares")
for i in range(1,101):
  if (i%2==0):
    print(i)'''
'''Programa que calcule las potencias 

print("Escriba la base")
base=int(input())
print("Escriba el exponente")
exponente=int(input())
acumulado=base

for i in range(exponente-1):
  acumulado=acumulado*base
print("El resultado es:",acumulado)'''
'''Cuenta las letras A que hay en una palabra
print ("Escribe un palabra en minusculas y sin tildes")
palabra=input()
contador=0
for i in (palabra):
  if i == "a":
    contador= contador+1
print("En",palabra,"hay",contador,"veces la letra A")

notas = [[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]
for i in range (3):
  for j in range (5):
    #print(i,j)
    if(notas[i][j]==10):
      print("Aumno de la fila",i+1,"columna",j+1)
    
Pide al usuario que adivine un número usando un while
clave = 2
prueba =0
print("EMPIEZA EL JUEGO")
while prueba!=clave:
  print("Adivina un numero entre 0 y 100, listillo")
  prueba=int(input())
print("Has acertado, si que eres un listillo")    '''
'''Te pide una contraseña en un bucle infinito hasta que la
aciertas
contraseña="esternocleidomastoideo"
while True:
  print("Bartolo introduce una contraseña")
  guess=input()
  if guess==contraseña:
    break
  else:
    print("Bartolo, te has equivocado. Intentalo de nuevo")
print("La has acertado, eres un fiera")

while True:
 print('¿Quién eres?')
 nombre = input()
 if nombre != 'Jorge':
  continue
 print('Hola, Jorge. Dime la contraseña')
 password = input()
 if password == '123456':
  break
print('Estás dentro!')'''


'''Función que suma dos números


def sumador(a, b):
    resultado = a + b
    return resultado


num1 = int(input("Introduzca el primero numero"))
num2 = int(input("Introduzca el segundo numero"))
resultado = sumador(num1, num2)
print("El resultado de la suma es", resultado)
'''
