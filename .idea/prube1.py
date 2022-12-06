esBisiesto = lambda x : x%4==0 and not x%100==0 or x%400==0
listaAno = []
for listadoAno in range(1500,2022):
    if esBisiesto(listadoAno) == True:
        listaAno.append(listadoAno)
print(listaAno)


"""
# Este es el ejercicio pedido de tarea. Lo modifique para que 
# directamente entregue la lista de bisiestos completa.
res = esBisiesto()

if res == True:
    print("El ano ingresado es Bisiesto")
else:
    print('Este ano NOOO es bisiesto')
"""

