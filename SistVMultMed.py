from datetime import datetime,date

def validar_enteros(msj):
    try:
        data = int(input(msj))
        return data
    except:
        print("--------------")
        print("Ingrese solo números enteros. Inténtelo nuevamente")
        print("--------------")
        return validar_enteros(msj)
    
def validar_flotantes(msj):
    try:
        data = float(input(msj))
        return data
    except:
        print("--------------")
        print("Ingrese solo números decimales. Inténtelo nuevamente")
        print("--------------")
        return validar_flotantes(msj)
    
import re
r2 = r'^[A-Za-z-ñÑ-áÁéÉíÍóÓúÚ  ]+$'
patron = re.compile(r2)

def validar_letras(msj):
    
    data = input(msj)
    if patron.match(data):
        return data
    else:
        print("----------------")
        print("Debe ingresar solo letras y espacios en blanco")
        print("----------------")
        return validar_letras(msj)
    
def validar_date(msj):
    while True:
        print("A continuación ingrese la fecha en la que se realizó el estudio")
        print("Ingrese el día: ")
        dia = validar_enteros(msj)

        print("Ingrese el mes: ")
        mes = validar_enteros(msj)

        print("Ingresar el año: ")
        año = validar_enteros(msj)

        if año < 2024:
            if mes > 12:
                print("-------------------------------------------")
                print("Fecha incorrecta, ingrese la fecha de nuevo")
                print("-------------------------------------------")

            elif mes == 2 and dia < 28:
                break 

            elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia < 32:
                break 

            elif mes != 2 and dia < 31: 
                break 

            else: 
                print("----------------")
                print("Fecha incorrecta, ingrese la fecha de nuevo")
                print("----------------")

        else: 
                print("----------------")
                print("Fecha incorrecta, ingrese la fecha de nuevo")
                print("----------------")


    fecha = date(año, mes, dia)
    print("fecha: ",fecha.strftime("%Y/%m/%d"))
    return str(fecha)
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
        mascota = validar_letras("Ingrese si es felino o canino: ")
        if mascota == "felino":
            m = validar_enteros("Ingrese la historia de la mascota: ")
            for m in self.__lista_felinos:
                if historia == m.verHistoria():
                    return True
            #solo luego de haber recorrido todo el ciclo se retorna False
            return False
        
        elif mascota == "canino":
            m = validar_enteros("Ingrese la historia de la mascota: ")
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
        mascota = validar_letras("Ingrese si es felino o canino: ")
        cantidad_de_felinos = 0
        cantidad_de_caninos = 0
        
        if mascota == "felino":
            cantidad_de_felinos = len(self.__lista_felinos)
            
        elif mascota == "canino":
            cantidad_de_caninos = len(self.__lista_caninos)
            
        else:
            print("---------------------------")
            print("Ingresó una opción inválida") 
            print("---------------------------")
        
        a = cantidad_de_caninos + cantidad_de_felinos
        return a 
    
    def ingresarMascota(self,mascota, historia):
        masco = validar_letras("Ingrese si es felino o canino: ")
        
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
        masc = validar_letras("Ingrese si es felino o canino: ")
        
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
        masc = validar_letras("Ingrese si es felino o canino: ")
            
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
        masc = validar_letras("Ingrese si es felino o canino: ")
        
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
        menu = validar_enteros('''Ingrese una opción: 
                       1. Ingresar una mascota
                       2. Ver fecha de ingreso
                       3. Ver número de mascotas en el servicio
                       4. Ver medicamentos
                       5. Eliminar mascota 
                       6. Eliminar medicamento
                       7. Salir
                       ''' )
        
        if menu == 1: # Ingresar una mascota 
            
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("------------------")
                print("No hay espacio ...") 
                print("------------------")
                continue
            
            historia = validar_enteros("Ingrese la historia clínica de la mascota: ")
            
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre = validar_letras("Ingrese el nombre de la mascota: ")
                tipo = validar_letras("Ingrese el tipo de mascota (felino o canino): ")
                peso = validar_flotantes("Ingrese el peso de la mascota: ")
                fecha = validar_date("Ingrese la fecha de ingreso: ")
                nm = validar_enteros("Ingrese cantidad de medicamentos: ")
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = validar_letras("Ingrese el nombre del medicamento: ")
                    dosis = validar_enteros("Ingrese la dosis: ")
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
                servicio_hospitalario.ingresarMascota(mas, historia)

            else:
                print("------------------------------------------------------")
                print("Ya existe la mascota con el numero de histoira clinica")
                print("------------------------------------------------------")

        elif menu == 2: # Ver fecha de ingreso
            
            q = validar_enteros("Ingrese la historia clínica de la mascota: ")
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("----------------------------------------------")
                print("La fecha de ingreso de la mascota es: " + fecha)
                print("----------------------------------------------")
                
            else:
                print("-------------------------------------------------------------------------------")
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
                print("-------------------------------------------------------------------------------")
            
        elif menu == 3: # Ver número de mascotas en el servicio 
            
            numero = servicio_hospitalario.verNumeroMascotas()
            print("-------------------------------------------------------")
            print("El número de pacientes en el sistema es: " + str(numero))
            print("-------------------------------------------------------")
            
        elif menu == 4: # Ver medicamentos que se están administrando
            
            q = validar_enteros("Ingrese la historia clínica de la mascota: ")
            medicamento = servicio_hospitalario.verMedicamento(q) 
            
            if medicamento != None: 
                print("------------------------------------")
                print("Los medicamentos suministrados son: ")
                print("------------------------------------")
                
                for m in medicamento:   
                    print("--------------------")
                    print(f"\n- {m.verNombre()}")
                    print("--------------------")
                    
            else:
                print("-------------------------------------------------------------------------------")
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
                print("-------------------------------------------------------------------------------")
        
        elif menu == 5: # Eliminar mascota
           
            q = validar_enteros("Ingrese la historia clínica de la mascota: ")
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("---------------------------------------")
                print("Mascota eliminada del sistema con exito")
                print("---------------------------------------")
                
            else:
                print("-----------------------------------")
                print("No se ha podido eliminar la mascota")
                print("-----------------------------------")
        
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





            

                

