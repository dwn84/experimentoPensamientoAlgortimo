#Solución Examen 1

import random

promedioDiasAcabado=0
promedioDiasCorte=0
promedioDiasConfeccion=0
nroDiasAcabado=0
nroDiasCorte=0
nroDiasConfeccion=0
prob3Dias=0
probCorte=0
nroOrdenes3=0
ordenesViejasCorte=0
for i in range(1000):
    tresDias=0
    diasCorte2=0
    proceso="acabado"
    while proceso=="acabado":
        nroDiasAcabado+=1
        tresDias+=1
        r=random.random()
        if r<0.3:
            proceso="acabado"
        else:
            proceso="corte"
        while proceso=="corte":
            nroDiasCorte+=1
            diasCorte2+=1
            tresDias+=1
            r=random.random()
            if r<0.4:
                proceso="corte"
            else:
                proceso="confeccion"
                if diasCorte2>=2:
                    ordenesViejasCorte+=1
            while proceso=="confeccion":
                nroDiasConfeccion+=1
                tresDias+=1
                r=random.random()
                if r<0.2:
                    proceso="confeccion"
                else:
                    proceso="terminado"
                    if tresDias==3:
                        nroOrdenes3+=1
                    
promedioDiasAcabado=nroDiasAcabado/1000
promedioDiasCorte=nroDiasCorte/1000
promedioDiasConfeccion=nroDiasConfeccion/1000
print("promedio dias en acabado ", promedioDiasAcabado)
print("promedio dias en corte ", promedioDiasCorte)               
print("promedio dias en confección ", promedioDiasConfeccion)        
print("promedio dias para entrega ", promedioDiasCorte+promedioDiasAcabado+promedioDiasConfeccion)
print("Prob. de que una orden se demore tres dias: ", nroOrdenes3/1000)
print("Prob. de que una orden se demore 2 dias o mas en corte: ", ordenesViejasCorte/1000)