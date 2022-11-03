import sqlite3
from sqlite3 import Error

import sys
import random
import datetime

procede = 0

try:
    with sqlite3.connect("PrimerIntentoDemo.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Clientes (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Salas (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Reservaciones (salas INTEGER PRIMARY KEY, cliente TEXT NOT NULL, nombre TEXT NOT NULL, folio INTEGER, turno TEXT NULL, fecha_registro timestamp);")
        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

while True:
    print("MENU DE RESERVACION DE SALAS")
    print("1- Reservaciones")
    print("2- Reportes")
    print("3- Registrar una sala")
    print("4- Registrar un cliente")
    print("5- Salir")
    print("*" * 60)

    opciones = input("¿Cual opcion quiere escoger?: \n")
    
    try:
        opciones_1 = int(opciones)
    except ValueError:
        print("Opcion Incorrecta")
    except Exception:
        print("Se ha presentado una excepcion:")
        print(Exception)

    print("*" * 60)

    if opciones_1 == 1:
      print("1- Registrar una nueva reservacion")
      print("2- Modificar descripcion de la reservacion")
      print("3- Consultar disponibilidad de salas para una fecha")
      print("4- Eliminar una reservacion")
      print("5- Volver al menu principal")
      print("*" * 60)
      submenu = input("¿Cual opcion quiere escoger?: \n")

      
      try:
        submenu_1 = int(submenu)
      except ValueError:
        print("Opcion Incorrecta")
      except Exception:
        print("Se ha presentado una excepcion:")
        print(Exception)

      if submenu_1 == 4:
        folio = int(input("Ingrese el folio para eliminar su reservacion: "))
       
        try:
          with sqlite3.connect("PrimerIntentoDemo.db") as conn:
            mi_cursor = conn.cursor()
            valores = {"folio":folio}
            mi_cursor.execute("DELETE * FROM Reservaciones WHERE clave = :folio", valores)
            registro = mi_cursor.fetchall()

            if registro:
                for clave, nombre in registro:
                    print(f"{clave}\t{nombre}")
            else:
                print(f"Su reservacion fue eliminada correctamente: {valor_clave}")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
      
      
      
      
      
      try:
        submenu_1 = int(submenu)
      except ValueError:
        print("Opcion Incorrecta")
      except Exception:
        print("Se ha presentado una excepcion:")
        print(Exception)

      if submenu_1 == 1:
        cliente = input("¿Es usted un cliente registrado?:\n")
        if cliente == 'Si':
         clave_usuario = input("Ingrese su clave de usuario:\n")
         try:
            with sqlite3.connect("PrimerIntentoDemo.db") as conn:
              mi_cursor = conn.cursor()
              valores = {"clave":clave_usuario}
              mi_cursor.execute("SELECT * FROM Clientes WHERE clave = :clave", valores)
              registros = mi_cursor.fetchall()
              if registros:
                print("Claves\tNombre")
                print("*" * 30)
                for clave, nombre in registros:
                  print(f"{clave:^6}\t{nombre}\n")
              else:
                print("No se encontraron registros, por favor registrese")
                continue
              
         except Error as e:
            print (e)
         except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
         finally:
            conn.close() 

            cliente = input("Ingrese su nombre:\n")
            salas = input("Ingrese la sala a reservar:\n")
            evento = input("Ingrese el evento a registrar:\n")
            folio = print(f"Su folio es {random.randrange(2000000)}:\n")
            print("Turnos: \n Matutino\n Vespertino\n Nocturno\n")
            turno = input("Ingrese el turno a reservar en mayusculas:\n")
            fecha_actual = datetime.date.today()
            fecha_registro = input("Ingresa la fecha a reservar con este formato dd/mm/aaaa: \n")
            if procede == 0:
                fecha_procesada = datetime.datetime.strptime(fecha_registro, "%d/%m/%Y" ).date()
                print(f"La fecha que estas solicitando es: {fecha_procesada}\n")
                cant_dias = 2
                nueva_fecha = fecha_procesada + datetime.timedelta(days=-cant_dias)
                if fecha_actual < nueva_fecha:
                    print("Su registro se completo con exito\n")
                    print(f"Su fecha se confirma registrada para, {fecha_procesada}\n")
                else:
                  print("La fecha no cumple con el requisito de 2 dias de anticipacion")
                  print("Porfavor intente con otra fecha:\n")
            else:
              print("No es una fecha")
            try:
              with sqlite3.connect("PrimerIntentoDemo.db") as conn:
                mi_cursor = conn.cursor()
                datos = (salas, cliente, evento, folio, turno, fecha_registro)
                mi_cursor.execute("INSERT INTO Reservaciones VALUES (?,?,?,?,?,?)", datos)
                print("Su reservacion se genero exitosamente")
            except Error as e:
              print (e)
            except:
              print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
            finally:
              conn.close() 

        elif cliente == 'No':
          print("Debe registrarse primero")
          print("*" * 60)

      elif submenu_1 == 2:
        modificar = input("¿Desea modificar su reservacion?:\n")
        if modificar == 'Si':
          try:
            with sqlite3.connect("PrimerIntentoDemo.db") as conn:
              mi_cursor = conn.cursor()
              mi_cursor.execute("SELECT salas, cliente, nombre, turno FROM Reservaciones")
              modificacion = mi_cursor.fetchall

              salas = input("Modifique su sala:\n")
              cliente = input("Modifique su nombre:\n")
              nombre = input("Modifique el evento:\n")
              turno = input("Modifique el turno en mayusculas:\n")
              folio = print(f"Su nuevo folio es {random.randrange(2000000)}:\n")
              fecha_actual = datetime.date.today()
              fecha_registro = input("Ingresa la nueva fecha a reservar con este formato dd/mm/aaaa:\n")
              if procede == 0:
                fecha_procesada = datetime.datetime.strptime(fecha_registro, "%d/%m/%Y" ).date()
                print(f"La fecha que estas solicitando es: {fecha_procesada}\n")
                cant_dias = 2
                nueva_fecha = fecha_procesada + datetime.timedelta(days=-cant_dias)
                if fecha_actual < nueva_fecha:
                    print("Su registro se completo con exito\n")
                    print(f"Su fecha se confirma registrada para, {fecha_procesada}\n")
                else:
                  print("La fecha no cumple con el requisito de 2 dias de anticipacion")
                  print("Porfavor intente con otra fecha:\n")
              else:
                print("No es una fecha")
              nuevo = (salas, cliente, nombre, turno, folio, fecha_registro)
              mi_cursor.execute("INSERT INTO Reservaciones VALUES (?,?,?,?,?,?)", nuevo)
              print(f"Su modificacion ha sido generada con exito")
          except Error as e:
            print (e)
          except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
          finally:
            conn.close() 

    elif opciones_1 == 2:
      print("1- Consultar reporte de reservaciones para una fecha:")
      print("2- Reporte en Excel:")
      print("3- Volver al menu principal:")
      print("*" * 60)
      submenu_2 = input("¿Cual opcion quiere escoger: \n")

      try:
        submenu_3 = int(submenu_2)
      except ValueError:
        print("Opcion Incorrecta")
      except Exception:
        print("Se ha presentado una excepcion:")
        print(Exception)

      print("*" * 60)

      if submenu_3 == 1:
        fecha_consultar = input("Ingrese la fecha a consultar:\n")
        print("*" * 60)
        print(f"**\tREPORTE DE RESERVACIONES PARA EL DIA {fecha_consultar}\t**")
        print("*" * 60)
        try:
          with sqlite3.connect("PrimerIntentoDemo.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT salas, cliente, nombre, turno FROM Reservaciones")
            consultas = mi_cursor.fetchall()

            for salas, cliente, nombre, turno in consultas:
              print("*" * 60)
              print("SALA \t CLIENTE  \t  EVENTO    \t    TURNO")
              print("*" * 60)
              print(f"{salas} \t {cliente}   \t  {nombre}    \t    {turno}")
              print("**************Fin del reporte**************")

        except sqlite3.Error as e:
          print (e)
        except Exception:
          print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
              conn.close()
              print("Se ha cerrado la conexión")
              
      elif submenu_3:
        continue

    elif opciones_1 == 3:
       nueva_clave = int(input("Dime la clave a agregar para las sala:\n"))
       nuevo_nombre = input("Dime el nombre de la sala:\n")
       try:
          with sqlite3.connect("PrimerIntentoDemo.db") as conn: #1- Puente
              mi_cursor = conn.cursor()
              valores = (nueva_clave, nuevo_nombre)#2- Mensajero
              mi_cursor.execute("INSERT INTO Salas VALUES(?,?)", valores) #3- Envío instrucciones
              print("Registro agregado exitosamente\n")
       except Error as e:
            print (e)
       except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    
    elif opciones_1 == 4:
        nueva_clave = int(input("Dime la clave a agregar:\n"))
        nuevo_nombre = input("Dime tu Nombre:\n")
        
        try:
            with sqlite3.connect("PrimerIntentoDemo.db") as conn: #1- Puente
                mi_cursor = conn.cursor()
                valores = (nueva_clave, nuevo_nombre)#2- Mensajero
                mi_cursor.execute("INSERT INTO clientes VALUES(?,?)", valores) #3- Envío instrucciones
                print("Registro agregado exitosamente")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    
    elif opciones_1 == 5:
      print("Gracias por usar este programa")
      break
        

    
    try:
            with sqlite3.connect("PrimerIntentoDemo.db") as conn:
              mi_cursor = conn.cursor()
              valores = {"clave":clave_usuario}
              mi_cursor.execute("SELECT * FROM Clientes WHERE clave = :clave", valores)
              registros = mi_cursor.fetchall()
              if registros:
                print("Claves\tNombre")
                print("*" * 30)
                for clave, nombre in registros:
                  print(f"{clave:^6}\t{nombre}\n")
              else:
                print("No se encontraron registros, por favor registrese")
                try:
                  with sqlite3.connect
              
         except Error as e:
            print (e)
         except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
         finally:
            conn.close()        
  
    
    if registros:
                          print("Clave Sala /////// Nombre Sala")
                          for clave, nombre in registros:
                              print(f"{clave:^6}\t{nombre}")
                              
                          clave = input("Ingresa la clave de la sala: ") 
                          nombre = input("Ingresa el nombre del evento: ")
                          turno = input.upper("Ingrese el turno en el que desea reservar: ")
                          fecha_actual = datetime.date.today()
                          fecha_capturada = input("Ingresa la fecha a reservar con este formato dd/mm/aaaa: \n")
                          if procede == 0:
                              fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y" ).date()
                              print(f"La fecha que estas solicitando es: {fecha_procesada}\n")
                              cant_dias = 2
                              nueva_fecha = fecha_procesada + datetime.timedelta(days=-cant_dias)
                              if fecha_actual < nueva_fecha:
                                  print("Su registro se completo con exito\n")
                                  print(f"Su fecha se confirma registrada para, {fecha_procesada}\n")
                                  reservaciones = {regis_cliente:[salas, folio, evento, turno, fecha_capturada]}

                              else:
                                  print("La fecha no cumple con el requisito de 2 dias de anticipacion")
                                  print("Porfavor intente con otra fecha:\n")
    
#### PROCESO PARA REGISTRAR UNA NUEVA RESERVACION###     
      try:
        submenu_1 = int(submenu)
      except ValueError:
        print("Opcion Incorrecta")
      except Exception:
        print("Se ha presentado una excepcion:")
        print(Exception)


      
      if submenu_1 == 1:
          cliente = input("¿Es usted un cliente registrado?('si' o 'no')\n")
          if cliente == 'si':
              clave_usuario = input("Ingrese su clave  de usuario: ")
              try:
                  with sqlite3.connect("PrimerIntentoDemo.db") as conn:
                      mi_cursor = conn.cursor()
                      valores = {"clave":clave_usuario}
                      mi_cursor.execute("SELECT * FROM Clientes WHERE clave = :clave", valores)
                      registros = mi_cursor.fetchall()

        
                      if registros:
                          print("Claves\tNombre")
                          print("*" * 30)
                          for clave, nombre in registros:
                              print ("Usted esta registrado como: ")
                              print(f"{clave:^6}\t{nombre}\n")
                    #Si no hay registros en la respuesta
                      else:
                         print("No se encontraron registros Por favor registrese")
              except Error as e:
                print (e)
              except Exception:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
              finally:
                conn.close()
                
              print("*" * 30)  
              
              ### SE MOSTRARAN LAS SALAS EXISTENTES ###
              try:
                  with sqlite3.connect("PrimerIntentoDemo.db") as conn:
                      mi_cursor = conn.cursor()
                      mi_cursor.execute("SELECT * FROM Salas ORDER BY clave")
                      registros = mi_cursor.fetchall()
                      
                      if registros:
                          print("Clave Sala /////// Nombre Sala")
                          for clave, nombre in registros:
                              print(f"{clave:^6}\t{nombre}")
                              
                          clave = input("Ingresa la clave de la sala: ") 
                          nombre = input("Ingresa el nombre del evento: ")
                          turno = input.upper("Ingrese el turno en el que desea reservar: ")
                          fecha_actual = datetime.date.today()
                          fecha_capturada = input("Ingresa la fecha a reservar con este formato dd/mm/aaaa: \n")
                          




                      else:
                          print("No hay salas existentes")

                      
              except Error as e:
                print (e)
              except Exception:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")    
    