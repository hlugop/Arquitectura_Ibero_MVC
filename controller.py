from model import BaseDatos
from view import Vista

class Controlador:
    def __init__(self):
        self.modelo = BaseDatos()
        self.vista = Vista()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu_principal()
            if opcion == "1":
                self.menu_autenticacion()
            elif opcion == "2":
                self.menu_cursos()
            elif opcion == "3":
                self.menu_usuarios()
            elif opcion == "4":
                self.menu_evaluaciones()
            elif opcion == "5":
                self.menu_progreso()
            elif opcion == "6":
                self.vista.mostrar_mensaje("Gracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida")

    def menu_autenticacion(self):
        while True:
            opcion = self.vista.mostrar_menu_autenticacion()
            if opcion == '1':
                usuario = self.vista.pedir_input("Ingrese su nombre de usuario: ")
                contraseña = self.vista.pedir_input("Ingrese su contraseña: ")
                # Implementar lógica de inicio de sesión
            elif opcion == '2':
                nombre = self.vista.pedir_input("Ingrese un nuevo nombre de usuario: ")
                rol = self.vista.pedir_input("Ingrese rol del usuario (estudiante/profesor): ")
                if self.modelo.crear_usuario(nombre, rol):
                    self.vista.mostrar_mensaje("Usuario creado exitosamente")
                else:
                    self.vista.mostrar_mensaje("El usuario ya existe")
            elif opcion == '3':
                break

  