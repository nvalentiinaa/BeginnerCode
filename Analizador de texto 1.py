print('Sea usted bienvenido al Analizador de texto')
mi_texto=input('Ingrese aqui su texto: ')
letras=input('Ingrese aqui 3 letras a buscar: ')

texto=mi_texto.lower().replace(' ','').replace('.','').replace(',','')
largo=len(texto)
print('Su texto contiene ' + str(largo) + ' letras')

if len(letras) != 3:
    print('Porfavor ingrese exactamente 3 letras')
    print('Nota: Evite el uso de coma, espacio o separadores')

else:

    a, b, c=letras[0], letras[1], letras[2]

    lista_texto = list(texto)

    variable_a = lista_texto.count(a)
    variable_b = lista_texto.count(b)
    variable_c = lista_texto.count(c)

    print(f'En su texto se repitio {a} {variable_a} veces')
    print(f'En su texto se repitio {b} {variable_b} veces')
    print(f'En su texto se repitio {c} {variable_c} veces')

mayus_minus= texto.upper()

print('La primera letra de su texto es "' + mayus_minus[0] + '"')
print('La ultima letra de su texto es "' + mayus_minus[-1] + '"')

texto_invertido = mi_texto[::-1]
print('Su texto a la inversa seria: ' + texto_invertido)

palabras_separadas= mi_texto.split()
palabras_reordenadas= palabras_separadas[::-1]
palabras_invertidas= ' '.join(palabras_reordenadas)


print('Las palabras de su texto al inverso serian: ' + palabras_invertidas)

if 'python' not in texto:
    print('La palabra Python no se encuentra en su texto')

if 'python' in texto:
        print('Hemos detectado que la palabra Python se encuentra en su texto')