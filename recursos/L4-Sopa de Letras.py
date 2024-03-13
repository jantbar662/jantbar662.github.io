
palabras=['ARBOL','AMBAR','PATA']

intentos=0

print('Bienvenido a la sopa de letras.')
print('Escribe las palabras en mayúsculas, por favor.')
print('')
print('')
print('A Q T N J')
print('T R F H L')
print('A M B A R')
print('P F Z O N')
print('R V I B L')
print('')
print('')
print('Escribe las respuestas a continuación:')
print('')
print('')

while True:

	usuario=input('')
	if usuario in palabras:
		print('Respuesta correcta.')
		palabras.remove(usuario)

	else:
		print('Respuesta incorrecta.')
	intentos=intentos+1
	a=len(palabras)
	if a==0:
		break

print('')
print('')
print('Enhorabuena')
print('Has ardado', intentos, 'intentos.')




