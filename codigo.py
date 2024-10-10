
# Diccionario de especialidades disponibles
ESPECIALIDADES = {
    1: "Cardiología",
    2: "Neurología",
    3: "Pediatría",
    4: "Ginecología"
}

# Definimos la clase Doctor con nombre y especialidad
class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    # Método para obtener el nombre de la especialidad
    def get_especialidad_nombre(self):
        return ESPECIALIDADES.get(self.especialidad, "Especialidad no encontrada")

# Definimos la clase Paciente con nombre y edad
class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = []

    def agregar_historial(self, cita):
        self.historial_clinico.append(cita)

    def listar_historial(self):
        for cita in self.historial_clinico:
            print(cita.get_info())

# Definimos la clase CitaMedica
class CitaMedica:
    def __init__(self, fecha, doctor, paciente):
        self.fecha = fecha
        self.doctor = doctor
        self.paciente = paciente

    # usamos el Método get_info() para mostrar la información 
    def get_info(self):
        return (f"Cita programada:\nFecha: {self.fecha}\n"
                f"Doctor: {self.doctor.nombre} ({self.doctor.get_especialidad_nombre()})\n"
                f"Paciente: {self.paciente.nombre}, Edad: {self.paciente.edad}")

# Definimos la clase Hospital para manejar doctores y pacientes
class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []
        self.pacientes = []

    # Agregar un doctor al hospital
    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    # Agregar un paciente al hospital
    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    # Listar todos los doctores del hospital
    def listar_doctores(self):
        print("Doctores registrados en el hospital:")
        for doctor in self.doctores:
            print(f"Nombre: {doctor.nombre}, Especialidad: {doctor.get_especialidad_nombre()}")

    # Listar todos los pacientes del hospital
    def listar_pacientes(self):
        print("Pacientes registrados en el hospital:")
        for paciente in self.pacientes:
            print(f"Nombre: {paciente.nombre}, Edad: {paciente.edad}")

# Esta es la función principal para registrar doctor, paciente y programar una cita
def main():
    # Crear una instancia del hospital
    hospital = Hospital("Hospital Uniminuto")

    # Ingresar nombre y especialidad del doctor
    nombre_doctor = input("Ingrese el nombre del doctor: ")

    # Mustra las opciones de especialidades de los doctores
    print("Seleccione la especialidad del doctor:")
    for clave, especialidad in ESPECIALIDADES.items():
        print(f"{clave}: {especialidad}")
    especialidad_doctor = int(input("Ingrese el número de la especialidad: "))

    doctor = Doctor(nombre_doctor, especialidad_doctor)
    hospital.agregar_doctor(doctor)

    # Ingresar nombre y edad del paciente
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    edad_paciente = int(input("Ingrese la edad del paciente: "))
    paciente = Paciente(nombre_paciente, edad_paciente)  

    # Agregar paciente al hospital
    hospital.agregar_paciente(paciente)
    fecha_cita = input("Ingrese la fecha de la cita (Año-Mes-Dia): ")
    cita = CitaMedica(fecha_cita, doctor, paciente)

    # Mostrar la información de la cita
    print(cita.get_info())

    # Listar los doctores y pacientes en el hospital
    hospital.listar_doctores()
    hospital.listar_pacientes()

# Ejecutar la función principal
# Ejecutar la funcion

if __name__ == "__main__":
    main()