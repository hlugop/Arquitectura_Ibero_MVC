class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

class Curso:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class Evaluacion:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso

class Progreso:
    def __init__(self, estudiante, curso, porcentaje):
        self.estudiante = estudiante
        self.curso = curso
        self.porcentaje = porcentaje

class BaseDatos:
    def __init__(self):
        self.usuarios = {}
        self.cursos = {}
        self.evaluaciones = {}
        self.progreso = {}

    def crear_usuario(self, nombre, rol):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre, rol)
            return True
        return False

