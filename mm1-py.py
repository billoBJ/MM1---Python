import time
import random 
import math
import threading
import numpy as np
import queue
import copy


qu = queue.Queue() #cola de servicio
clientes = [] #lista de clientes

class Servicio:
    estado = False #indica si el servicio esta ocupado

    
    def __init__(self):
           self.estado = False #incicializamos el servicio como desocupado   
                     
       
class cliente(Servicio):
       cliente_nummero = 0
       llegada = 0 #tiempo en que llega el cliente
       espera = 0 #tiempo que espero el cliente
       servicio = 0 #tiempo que el cliente es atendido
       salida = 0 #tiempo de salida
       
       def __init__(self,cliente_num,lamnda):
              R = random.random() # Random float:  0.0 <= x < 1.0
              self.cliente_nummero = cliente_num #establesco el numero de cliente 
              if cliente_num == 0: 
                     self.llegada = int(-lamnda * math.log(R)) # Distribucion exponencial
              else:
                     index = cliente_num-1
                     self.llegada = int(-lamnda * math.log(R) + clientes[index].llegada) # Distribucion exponencial
                     


def Simular(num_clientes): #simulamos MM1
       atender_clientes = True #define si aun quedan clientes por atender
       t = 0 #tiempo 0
       server_busy = 0 #tiempo de servicio ocuapado
       wait_time = 0
       clientes_atendidos = 0
       servicio = Servicio()
       np.random.seed(123) #seed para numeros aleatorios
       
       while atender_clientes:
              
              if servicio.estado: #si el servicio esta ocupado
                     server_busy += 1 #aumentamos el tiempo del servidor ocupado 
                     cliente_atendido.servicio -= 1  #reducimos el tiempo de servicio
                     if not qu.empty(): # si la cola no esta vacia, algun cliente esta esperando 
                            wait_time +=1 #aumentamos tiempo de espera
                     
                     if cliente_atendido.servicio <= 0:#si agoto mi tiempo de servicio
                            print('Cliente N:',cliente_atendido.cliente_nummero,'dejo se der atendido en el tiempo',t )
                            servicio.estado =  False  #marco el servicio como desocupado
                            clientes_atendidos += 1 
                            if clientes_atendidos == len(clientes):
                                   atender_clientes = False
                                   break                     
                     
              
              #verificamos el cliente que llega en el tiempo t
              for j in range(num_clientes):
                     if t == clientes[j].llegada:
                            qu.put(clientes[j])#colocamos el cliente en cola
                            print('Cliente N:',clientes[j].cliente_nummero, 'llega en el tiempo:',t)
           
              #si el servicio no esta ocupado y la cola de servicio no esta vacia
              #marcamos el servicio ocupado
              if not servicio.estado and not qu.empty():#servicio libre
                     cliente_atendido = qu.get()
                     cliente_atendido.servicio = int(np.random.exponential(lamnda)) #le asignamos un tiempo de atencion
                     print('Cliente N:',cliente_atendido.cliente_nummero, 'es atendido en el tiempo:',t)
                     servicio.estado = True

              t += 1 #aumentamos el tiempo
       
       print ("\n----------------------------------------------")
       print ("\nIndicadores obtenidos: ")
       #Retraso de en cola 
       ret =  wait_time / clientes_atendidos #tiempo espera / n clientes
       print ("\nRETRASO EN COLA: %.2f" % ret)
       ret =  server_busy / t #tiempo serv ocupado / tiempo fin
       print ("\nUTILIZACION DEL SERVIDOR: %.2f" % ret)
       


def main():
    num_clientes =   int(input("\nIntroducir la cantidad de clientes: " ))
    global lamnda
    lamnda =  int(input("\nIntroducir promedio de llegada: " ))
    for i in range(num_clientes): #Recorro la cantidad de Clientes
        clientes.append(cliente(i,lamnda))  #creo los Cliente 

    Simular(num_clientes)
       

if __name__=="__main__": #correr el script principal 
    main() #ejecuta funcion main