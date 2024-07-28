height = float(input("Ingresa tu altura en centímetros: "))
credits = int(input("Ingresa el número de créditos que tienes: "))
altura_minima = 154  
creditos_minimos = 10  
if height >= altura_minima and credits >= creditos_minimos:
            print("¡Disfruta del viaje!")
elif credits >= creditos_minimos:
            print("No eres lo suficientemente alto para montar.")
elif height >= altura_minima:
            print("No tienes suficientes créditos.")
else:
            print("No has cumplido con ninguno de los requisitos.")