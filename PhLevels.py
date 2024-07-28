ph = float(input("Ingrese un valor de ph entre 0 or 14: "))
if ph < 0 or ph > 14:
      print("El valor de pH debe estar entre 0 or 14: ")
if ph > 7:
      print("Basico")
elif ph < 7:
      print("Acido")
else:
      print("Neutral")

