puntos = {'Gryffindor': 0,'Ravenclaw': 0,'Hufflepuff': 0,'Slytherin': 0}

print("Te gusta el amanecer o el anochecer?")
print("    1) amanecer")
print("    2) anochecer")
respuesta1 = int(input("Ingrese su respuesta (1 o 2): "))

if respuesta1 == 1:
        puntos['Gryffindor'] += 1
        puntos['Ravenclaw'] += 1
elif respuesta1 == 2:
        puntos['Hufflepuff'] += 1
        puntos['Slytherin'] += 1
else:
        print("Entrada incorrecta")
        
        print("Cuando este muerto quiero que la gente me recuerde como:")
print("    1) el bien")
print("    2) el grande")
print("    3) los sabios")
print("    4) los audaces")
respuesta2 = int(input("Ingrese su respuesta (1, 2, 3 o 4): "))

if respuesta2 == 1:
        puntos['Hufflepuff'] += 2
elif respuesta2 == 2:
        puntos['Slytherin'] += 2
elif respuesta2 == 3:
        puntos['Ravenclaw'] += 2
elif respuesta2 == 4:
        puntos['Gryffindor'] += 2
else:
        print("Entrada incorrecta")
        
        print("Que tipo de instrumento le agrada mas a su oido?")
print("    1) el violín")
print("    2) la trompeta")
print("    3) el piano")
print("    4) el tambor")
respuesta3 = int(input("Ingrese su respuesta (1, 2, 3 o 4): "))

if respuesta3 == 1:
        puntos['Slytherin'] += 4
elif respuesta3 == 2:
        puntos['Hufflepuff'] += 4
elif respuesta3 == 3:
        puntos['Ravenclaw'] += 4
elif respuesta3 == 4:
        puntos['Gryffindor'] += 4
else:
        print("Entrada incorrecta")
        
        casa_mas_puntos = max (puntos, key=puntos.get)
print("La casa con más puntos es: ")
