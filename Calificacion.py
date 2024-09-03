class Calificacion:
    def __init__(self, nota):
        self.nota = nota
    def determinar_letra(self):
        if self.nota > 9.0:
            return "A"
        elif self.nota > 8.0:
            return "B"
        elif self.nota >= 7.5:
            return "C"
        else:
            return "R"

    def mostrar_calificacion(self):
        letra = self.determinar_letra()
        print(f"La calificación es {letra}.")
