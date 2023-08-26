import funciones 
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
 
    def __init__(self):
        self.__lista_caninos = {}
        self.__lista_felinos = {}
    
    def verificarExiste(self,historia):
        mascota = input("Ingrese si es felino o canino: ")
        if mascota == "felino":
            m = int(input("Ingrese la historia de la mascota: "))
            for m in self.__lista_felinos:
                if historia == m.verHistoria():
                    return True
            #solo luego de haber recorrido todo el ciclo se retorna False
            return False
        
        elif mascota == "canino":
            m = int(input("Ingrese la historia de la mascota: "))
            for m in self.__lista_caninos:
                if historia == m.verHistoria():
                    return True
            #solo luego de haber recorrido todo el ciclo se retorna False
            return False
        
        else: 
            print("---------------------------")
            print("Ingresó una opción inválida") 
            print("---------------------------")
    
    def verNumeroMascotas(self):
        mascota = input("Ingrese si es felino o canino: ")
        
        if mascota == "felino":
            cantidad_de_feninos = len(self.__lista_caninos)
            
        elif mascota == "canino":
            cantidad_de_caninos = len(self.__lista_caninos)
            
        else:
            print("---------------------------")
            print("Ingresó una opción inválida") 
            print("---------------------------")
        
        a = cantidad_de_caninos + cantidad_de_feninos
        return a 
    
    def ingresarMascota(self,mascota, historia):
        masco = input("Ingrese si es felino o canino: ")
        
        if masco == "felino":
            self.__lista_felinos[historia] = mascota
            
        elif masco == "canino":
            self.__lista_caninos[historia] = mascota
            
        else: 
            print("---------------------------")
            print("Ingresó una opción inválida") 
            print("---------------------------")
            
    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        masc = input("Ingrese si es felino o canino: ")
        
        if masc == "felino":
            for masc in self.__lista_felinos:
                if historia == masc.verHistoria():
                    return masc.verFecha() 
        
        elif masc == "canino":
            for masc in self.__lista_caninos:
                if historia == masc.verHistoria():
                    return masc.verFecha()
                
        else: 
            print("---------------------------")
            print("Ingresó una opción inválida") 
            print("---------------------------")
            
        return None
            
    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        masc = input("Ingrese si es felino o canino: ")
            
        if masc == "felino":
            for masc in self.__lista_felinos:    
                if historia == masc.verHistoria():
                    return masc.verLista_Medicamentos() 
                
        elif masc == "canino": 
            for masc in self.__lista_caninos:
                if historia == masc.verHistoria():
                    return masc.verLista_Medicamentos()
                
        else: 
            print("---------------------------")
            print("Ingresó una opción inválida") 
            print("---------------------------")
            
        return None
    
    def eliminarMascota(self, historia):
        masc = input("Ingrese si es felino o canino: ")
        
        if masc == "felino":
            for masc in self.__lista_felinos:
                if historia == masc.verHistoria():
                    valor_d = self.__lista_felinos.pop(historia, "No encontrado")  #opcion con el pop
                return valor_d  #eliminado con exito
            
        elif masc == "caninos":
            for masc in self.__lista_caninos:
                if historia == masc.verHistoria():
                    valor_d = self.__lista_caninos.pop(historia, "No encontrado")
                return valor_d
            
        else:
            print("---------------------------")
            print("Ingresó una opción inválida")
            print("---------------------------")
                    
        return False 
    
    def eliminarMedicamento(self, historia):
        pass
        

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    
    while True:
        menu=int(input('''Ingrese una opción: 
                       1. Ingresar una mascota
                       2. Ver fecha de ingreso
                       3. Ver número de mascotas en el servicio
                       4. Ver medicamentos
                       5. Eliminar mascota 
                       6. Eliminar medicamento
                       7. Salir
                       ''' ))
        
        if menu == 1: # Ingresar una mascota 
            
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("------------------")
                print("No hay espacio ...") 
                print("------------------")
                continue
            
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("------------------------------------------------------")
                print("Ya existe la mascota con el numero de histoira clinica")
                print("------------------------------------------------------")

        elif menu == 2: # Ver fecha de ingreso
            
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu == 3: # Ver número de mascotas en el servicio 
            
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu == 4: # Ver medicamentos que se están administrando
            
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
           
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu == 6: #eliminar medicamento
            pass
        
        elif menu == 7:
            
            print("-------------------------------------------------------------")
            print("Usted ha salido del sistema de servicio de hospitalización...")
            print("-------------------------------------------------------------")
            break
        
        else:
            
            print("-----------------------------------------------------------")
            print("Usted ingresó una opción no válida, intentelo nuevamente...")
            print("-----------------------------------------------------------")
            
if __name__=='__main__':
    main()





            

                

