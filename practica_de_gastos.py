Ingresos = float(input('Ingresos:'))
Gastos = float(input('Gastos:'))

def mostrar_numero(n):
    if n == int(n):
        return int(n)
    else:
        return round (n, 2)

if Gastos > 0 and Ingresos > 0:
    porcentaje_gasto = (Gastos/Ingresos)*100
    pgastos =  round(porcentaje_gasto, 2)
    resta = (Ingresos - Gastos)
    presta = mostrar_numero(resta)
    
    if porcentaje_gasto > 50:
        print(f'gastas mucho, el {pgastos}% de tus ingresos, te quedan {presta}')
    elif porcentaje_gasto < 40:
        print(f'estas bien solo gastas el {pgastos}% de tus ingresos, te quedan {presta}')
    else: 
        print(f'estas bien pero ojo gastas el {pgastos}% de tus ingresos, te quedan {presta}')

else:
    print('error: los ingresos y gastos deben ser mayores a 0')