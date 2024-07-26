from estudiante_distancia import EstudianteDistancia

def main():
    nombre = "René"
    apellido = "Elizalde"
    identificacion = "110011"
    edad = 36

    est_distancia = EstudianteDistancia(nombre, apellido, identificacion, edad)
    est_distancia.establecer_costo_asignatura(50.5)
    est_distancia.establecer_numero_asignaturas(5)
    est_distancia.calcular_matricula_distancia()

    print(est_distancia)

    print("--------------------------")
    est_distancia.establecer_apellidos_estudiante("Elizalde Solano")
    print(est_distancia)

if __name__ == "__main__":
    main()
