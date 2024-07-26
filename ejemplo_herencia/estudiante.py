class Estudiante:
    def __init__(self, nombres, apellidos, identificacion, edad):
        self.nombres_estudiante = nombres
        self.apellidos_estudiante = apellidos
        self.identificacion_estudiante = identificacion
        self.edad_estudiante = edad

    def establecer_nombres_estudiante(self, nombres):
        self.nombres_estudiante = nombres

    def establecer_apellidos_estudiante(self, apellidos):
        self.apellidos_estudiante = apellidos

    def establecer_identificacion_estudiante(self, identificacion):
        self.identificacion_estudiante = identificacion

    def establecer_edad_estudiante(self, edad):
        self.edad_estudiante = edad

    def obtener_nombres_estudiante(self):
        return self.nombres_estudiante

    def obtener_apellidos_estudiante(self):
        return self.apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self.identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self.edad_estudiante

    def __str__(self):
        return (f"Nombre: {self.nombres_estudiante}\n"
                f"Apellido: {self.apellidos_estudiante}\n"
                f"Identificación: {self.identificacion_estudiante}\n"
                f"Edad: {self.edad_estudiante}\n")
