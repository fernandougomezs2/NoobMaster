print("---MENU---")
print("1.-sacar el area de un circulo")
print("2.- numeros de fibonacci ")

sigma = int(input("ingresa la funcion requerida"))

if sigma == int(1):
# Austin
    pi1 = float(3.1416)
    rad1 = int()
    res = int()
    resu = float()


    rad1 = int(input("Buenas tardes, digame el radio de su ciculo."))

    res = int(input("deseas calcular el area del ciculo 1. para si 0. para cancelar"))


    if res > int(0):
        resu = pi1 * rad1**2
        print(resu, "es el area de su circulo.")
    else:
        res == int(1)
        res = int(input("disculpe el error, vulve a introducir el pi"))
        resu = pi1 * rad1^2
        print(resu, "es el perimetro de su circulo.")






# Alexis
elif sigma == 2:
	print("Ingresar el rango de numeros que se desea obtener en secuencia fibonacci")
	Heidis = int(input("Rango: "))


	def Fibonacci(n):
		Alexis = 0
		Austin = 1

		for x in range(n):
			Fernando = Alexis + Austin
			Alexis = Austin
			Austin = Fernando
		return Austin

	for Ara in range(Heidis):
		print(Fibonacci(Ara))

else:
	print("Error")