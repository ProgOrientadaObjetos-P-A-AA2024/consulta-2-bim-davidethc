from estudiante import Estudiante

class EstudianteDistancia(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad):
        super().__init__(nombres, apellidos, identificacion, edad)
        self.numero_asignaturas = 0
        self.costo_asignatura = 0.0
        self.matricula_distancia = 0.0

    def establecer_numero_asignaturas(self, numero):
        self.numero_asignaturas = numero

    def establecer_costo_asignatura(self, costo):
        self.costo_asignatura = costo

    def calcular_matricula_distancia(self):
        self.matricula_distancia = self.numero_asignaturas * self.costo_asignatura

    def obtener_numero_asignaturas(self):
        return self.numero_asignaturas

    def obtener_costo_asignatura(self):
        return self.costo_asignatura

    def obtener_matricula_distancia(self):
        return self.matricula_distancia

    def __str__(self):
        return (f"{super().__str__()}"
                f"Numero asignaturas: {self.numero_asignaturas}\n"
                f"Valor de la asignatura: {self.costo_asignatura:.2f}\n"
                f"Valor matrícula: {self.obtener_matricula_distancia():.2f}\n")
