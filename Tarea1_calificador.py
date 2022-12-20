#Scrip para calificar Tarea 1
l = []
factor = 1 #Valor de cada True

try:
  l.append((a_plus_abs_b(2,3) == 5)) 
except:
  l.append(False) 
  
print("Tu nota es:", sum(l)*factor)

