PPP = int(input('Cuanto vale el primer parcial: '))
PPS = int(input('Cuanto vale el segundo parcial: '))
PPT = int(input('Cuanto vale el tercer parcial: '))

NP = int(input('Cuanto te sacaste: '))
NS = int(input('Cuanto te sacaste: '))
NT = int(input('Cuanto te sacaste: '))
NL = int(input('Nota laboratorio: '))
PE = int(input('Puntos ganados: '))

def muestra (n):
    if  n == int(n):
        return int(n)
    else:
        return round(n, 2)
        

if PPP >= 0 and PPS >= 0 and PPT >= 0:
    Promedio1 = (NP/100)*PPP
    Promedio2 = (NS/100)*PPS
    Promedio3 = (NT/100)*PPT
    
    total = Promedio1 + Promedio2 + Promedio3 + NL + PE  
    total = min(total, 100)
    rtotal = round(total, 2)
    ftotal = muestra(rtotal)

    if total >= 70:
        print(f'Crack, tenes {ftotal}')
    elif total >= 51:
        print(f'Te salvaste, tenes {ftotal}')
    else:
        print(f'Te tiraste, tenes {ftotal}')
        
else: 
    print('Ingrese un numero valido')
   
    

    