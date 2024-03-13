cambio=3
palabra_cifrada=[]

print('Vamos a cifrar palabras.')
print('')
print('')
while True:
	usuario=input('')
	for letra in usuario:
		posicion=ord(letra)
		if letra=='x':
			nuevaLetra='a'
		elif letra=='y':
			nuevaLetra='b'
		elif letra=='z':
			nuevaLetra='c'
		else:
			cifrado=posicion+cambio
			nuevaLetra=chr(cifrado)
			palabra_cifrada.append(nuevaLetra)
		
	print(palabra_cifrada)	
		
