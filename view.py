class Vista:
    @staticmethod
    def mostrar_menu_principal():
        print("\n--- Menú Principal ---")
        print("1. Autenticación")
        print("2. Gestión de Cursos")
        print("3. Gestión de Usuarios")
        print("4. Evaluaciones")
        print("5. Progreso del Estudiante")
        print("6. Salir")
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_menu_autenticacion():
        print("=== Menú de Autenticación ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        return input("Seleccione una opción (1-3): ")



    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

    @staticmethod
    def pedir_input(prompt):
        return input(prompt)