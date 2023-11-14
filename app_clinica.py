#Aquí creamos el menú de opciones para el usuario:
from turneoOdontologico import Paciente, Profesional, Turno, Clinica
from datetime import datetime

def menu():
    opcion = 0
    while opcion < 1 or opcion > 11:
        print("--")  
        print("\nBienvenido al sistema de turnos Dental Desk. Por favor elija una opción: ")
        print("1. Registrar un nuevo paciente")
        print("2. Registrar un nuevo profesional")
        print("3. Registrar un nuevo turno")
        print("4. Mostrar listado de pacientes")
        print("5. Mostrar paciente")
        print("6. Mostrar listado de profesionales")
        print("7. Mostrar profesional")
        print("8. Mostrar listado de turnos")
        print("9. Mostrar turno")
        print("10. Dar de baja un turno")
        print("11. Salir")
        print("--")
        opcion = int(input("Ingrese la opción deseada: "))
    return opcion

def run(turneoOdontologico):
    opcion = 0

    while opcion != 11:
        opcion = menu()
        
        if opcion == 1: #Acá tengo que agregar el paciente a la lista de pacientes.
            nombre = input("Ingrese el nombre del paciente: ")
            apellido = input("Ingrese el apellido del paciente: ")
            dni = int(input("Ingrese el DNI del paciente: "))
            contacto = input("Ingrese el número de contacto del paciente: ")
            direccion = input("Ingrese la dirección del paciente: ")
            paciente = Paciente(dni, nombre, apellido, contacto, direccion)
            if turneoOdontologico.contiene_paciente(paciente.dni):
                print("El paciente ya se encuentra registrado")
            else:
                turneoOdontologico.alta_nuevo_paciente(paciente)
                print("¡Paciente registrado con éxito!")
            input("Presione Enter para continuar...")    
        
        elif opcion == 2: #Acá tengo que agregar el profesional a la lista de profesionales.
            nombre = input("Ingrese el nombre del profesional: ")
            apellido = input("Ingrese el apellido del profesional: ")
            dni = int(input("Ingrese el DNI del profesional: "))
            contacto = input("Ingrese el número de contacto del profesional: ")
            direccion = input("Ingrese la dirección del profesional: ")
            especialidad = input("Ingrese profesión: ")
            profesional = Profesional(dni, nombre, apellido, contacto, direccion,especialidad)
            if turneoOdontologico.contiene_profesional(profesional.dni):
                print("El profesional ya se encuentra registrado")
            else:
                turneoOdontologico.alta_nuevo_profesional(profesional)
                print("¡Profesional registrado con éxito!")
            input("Presione Enter para continuar...")    
        
        elif opcion == 3: #Se registra un nuevo turno # Paciente y Profesional deben estar registrados.
            dni_paciente = int(input("Ingrese el DNI del paciente: "))
            if  turneoOdontologico.buscar_paciente(dni_paciente) == False: 
                print("El paciente no se encuentra registrado, es necesario registrar el cliente para asignar un turno.")
                break
            else: 
                dni_profesional = int(input("Ingrese el DNI del profesional: "))
                profesional = turneoOdontologico.contiene_profesional(dni_profesional)
                if profesional is None:
                    print("El profesional no se encuentra registrado")
                    input("Presione Enter para continuar...")
                else:
                    fecha = input("Ingrese la fecha del turno en formato 'año,mes,dia,hora,min,seg': ")
                    anio, mes, dia, hora, minuto, segundo = fecha.split(",")
                    dato = datetime(int(anio), int(mes), int(dia), int(hora), int(minuto), int(segundo))
                    turno = Turno(paciente, profesional, dato)
                    if turneoOdontologico.contiene_turno(turno.dato):
                        print("El turno ya se encuentra registrado") 
                    else:
                        turneoOdontologico.registrar_turno(turno)
                        print("¡Turno registrado con éxito!")
                    input("Presione Enter para continuar...") 
        
        elif opcion == 4: #Mostrar lista de pacientes
            turneoOdontologico.mostrar_pacientes() #Se utiliza el método __str__ para mostrar la lista de pacientes
            input("Presione Enter para continuar...") 
        
        elif opcion == 5: #Tarea NO FUNCIONA. RETORNA NONE
            dni_busqueda = int(input("Ingrese DNI del paciente: "))
            resultado = turneoOdontologico.busqueda_individual(dni_busqueda)
            print(resultado) 
            input("Presione Enter para continuar...")
                     
        elif opcion == 6: #Mostrar lista de profesionales 
            turneoOdontologico.mostrar_profesionales() # habia que crear metodo __str__
            input("Presione Enter para continuar...")
        
        elif opcion == 7: #Tarea: NO FUNCIONA
            turneoOdontologico.busqueda_individual_profesional(profesional.dni)
        
        elif opcion == 8:  #Mostrar lista de turnos Tarea: #No muestra el nombre del profesional 
            turneoOdontologico.mostrar_turnos()
            input("Presione Enter para continuar...") #En caso que no haya turnos registrado debe haber un print "no hay turnos registrados"
        
        elif opcion == 9: # Tarea: NO FUNCIONA
            turneoOdontologico.busqueda_individual_turno(turno.dato)
        
        elif opcion == 10: #Dar de baja un turno
            fechaelim = input("Ingrese la fecha del turno en formato 'año,mes,dia,hora,min,seg': ")
            anio, mes, dia, hora, minuto, segundo = fechaelim.split(",")
            dato = datetime(int(anio), int(mes), int(dia), int(hora), int(minuto), int(segundo))
            
            if not turneoOdontologico.contiene_turno(turno.dato): #TAREA: NO FUNCIONA
                print("El turno no se encuentra registrado")
            else:
                turneoOdontologico.eliminar_turno(turno) 
                print("Turno eliminado con éxito")
            input("Presione Enter para continuar...")
        
        elif opcion == 11:
            print("Gracias por utilizar el sistema de turnos Dental Desk. Una buena salud oral es clave para el bienestar general.")
        else:
            print("Opción incorrecta. Por favor, ingrese una opción válida")
            
if __name__ == "__main__":
    turneoOdontologico = Clinica()
    run(turneoOdontologico)