from estudiante import Estudiante

class EstudiantePresencial(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad):
        super().__init__(nombres, apellidos, identificacion, edad)
        self.numero_creditos = 0
        self.costo_credito = 0.0
        self.matricula_presencial = 0.0

    def establecer_numero_creditos(self, numero):
        self.numero_creditos = numero

    def establecer_costo_credito(self, costo):
        self.costo_credito = costo

    def calcular_matricula_presencial(self):
        self.matricula_presencial = self.numero_creditos * self.costo_credito

    def obtener_numero_creditos(self):
        return self.numero_creditos

    def obtener_costo_credito(self):
        return self.costo_credito

    def obtener_matricula_presencial(self):
        return self.matricula_presencial

    def __str__(self):
        return (f"Apellidos Estudiante: {self.apellidos_estudiante}\n"
                f"Identificación: {self.obtener_identificacion_estudiante()}\n"
                f"Valor Matrícula: {self.obtener_matricula_presencial():.2f}\n")
