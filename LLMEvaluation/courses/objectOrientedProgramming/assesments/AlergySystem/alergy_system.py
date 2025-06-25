import os
from LLMEvaluation.courses.dataStructures.data_structures_general import (
    DataStucturesGeneral,
)
import shutil  # To copy the student's code into the project for compilation
import subprocess  # To execute Java compilation and execution commands


class AlergySystem(DataStucturesGeneral):
    llm = None

    def __init__(self):
        super().__init__()

    def specific_rubric(self):
        """
        Returns the specific rubric for SplayTree methods.
        """
        return """Estas son las clases y métodos a evaluar y dar una retroalimentación formativa:
1) La clase AlergiasException es una excepción no comprobada (hereda de RuntimeException). Crea la clase con un constructor por defecto y otro con un String como entrada.

2) Para la representación de las alergias, necesitamos dos enumerados:
a.	TipoAlimento: que contiene la información de los distintos tipos de alimentos que se han identificado que pueden producir alergias:  LACTOSA, GLUTEN, FRUTOS_SECOS, MARISCOS.
b.	Estacion: que contiene la información de las estaciones en las que se pueden producir las alergias:  INVIERNO, PRIMAVERA, VERANO, OTOÑO.

3). La clase ABSTRACTA Alergia contiene 2 variables de instancia, una de tipo int, severidad, y una de tipo String, descripción. También contiene dos constantes de tipo int, minSeveridad (inicializar a 0), maxSeveridad (inicializar a 10), las cuales establecen el rango válido de severidad <= maxSeveridad y severidad >= minSeveridad. 
a.	La clase debe proporcionar dos constructores:
i)	Uno que inicialice todos los atributos de instancia, debiendo validarse que la severidad se encuentra en rango válido. En caso de no estar en rango válido lanza una excepción AlergiasException con el mensaje Severidad debe estar en el rango [min,max] siendo min y max los valores del rango válido.
ii)	Otro que inicialice la descripción y ponga la severidad al valor mínimo.
b.	Realizar todos los métodos getter y setter para poder consultar y modificar los diferentes parámetros. Cuando se establece la severidad, también se lanza la excepción AlergiasException si está fuera de rango válido.

4) La clase AlergiaAlimenticia es una especialización de la clase Alergia. La superclase Alergia se aplica a todas las alergias y la clase que definimos en este apartado permite indicar sobre qué alimento es la alergia. Para ello se usa un atributo adicional que es del tipo enumerado TipoAlimento. Se pide:
a.	Constructor que recibe los mismos parámetros que Alergia y además el tipo de alimento.
b.	Un método para obtener el tipo de alimento del que es alérgico.
c.	La redefinición del método toString() de forma que devuelva la representación textual del objeto con el formato: [Alimenticia, tipo, severidad, descripcion] como se muestra en el ejemplo: [Alimenticia, LACTOSA, 8, Alergia Severa a la lactosa]

5)	La clase AlergiaAmbiental es una especialización de la clase Alergia. La clase que definimos en este apartado permite indicar una lista de estaciones en las que está activa. Para ello se usa un atributo adicional que es una lista del tipo enumerado Estacion. Se pide:
a.	Constructor que recibe los mismos parámetros que Alergia y además la lista de estaciones.
b.	Un método para obtener la lista de estaciones.
c.	La redefinición del método toString() de forma que devuelva la representación textual del objeto con el formato: [Ambiental, severidad, estaciones, descripcion] como se muestra en el ejemplo: Ambiental, 6, [PRIMAVERA, VERANO, OTOÑO, INVIERNO], Alergia a los gatos]

6)	La clase Paciente del paquete personal tiene tres atributos: uno constante de tipo String (nombre), otro de tipo int (edad), y otro que es ArrayList<Alergia> (alergias). Se pide:
a.	Constructor que recibe los datos del paciente y deberá inicializar la lista de alergías como vacía.
b.	Métodos para obtener el nombre y la edad, y modificar la edad.
c.	Método getAlergias() que devuelve la lista de las alergias.
d.	Método addAlergia(Alergia) que añade una alergia a la lista devolviendo verdadero si se ha añadido o falso si no se hizo ningún cambio. En caso de recibir una alergia sin inicializar (valor null) lanza una excepción AlergiasException con el mensaje ¨No se puede añadir una alergia sin inicializar¨.
e.	Método boolean removeAlergia(Alergia) que recibe una alergia y la elimina de la lista. Devuelve verdadero si la elimina correctamente o falso si no estaba.
f.	Método alergiasSeveridad(int) que recibe un umbral de severidad y devuelve un nuevo ArrayList que incluye todas las alergias de ese paciente que tienen una severidad igual o superior a ese umbral. Puede devolver una lista vacía si ninguna alergia tiene una severidad igual o superior al umbral.
g.	La redefinición del método toString() de forma que devuelva la representación textual del objeto con el formato: 
--Paciente--
 Nombre: nombre del paciente
 Edad: edad del paciente
 Alergias: 
[…]
[…]
Por ejemplo:
--Paciente--
 Nombre: Juan Perez
 Edad: 25
 Alergias: 
[Ambiental, 6, [PRIMAVERA, VERANO, OTOÑO, INVIERNO], Alergia a los gatos]
[Ambiental, 3, [PRIMAVERA], Alergia al polen del Olivo]
[Alimenticia, FRUTOS_SECOS, 2, Alergia Leve a los frutos secos]
Se recomienda el uso de StringBuilder.
"""

    def sample_output(self):
        """
        Returns a sample output of the evaluation in HTML format.
        """
        return """Este es un ejemplo de salida:
Calificación final: 44/70 <br>
<table border="1">
  <tr>
    <th>Clase</th>
    <th>Puntuación</th>
    <th>Retroalimentación</th>
  </tr>
  <tr>
    <td>AlergiasException</td>
    <td>0/10</td>
    <td><strong>Funcionalidad</strong>: La clase hereda de Exception (excepción comprobada) y ¡debería heredar de RuntimeException! (se pedía una excepción NO comprobada)</td>
  </tr>
  <tr>
    <td>TipoAlimento</td>
    <td>10/10</td>
    <td><strong>Claridad</strong>: Separa cada elemento del enumerado en una nueva línea, mejora la legibilidad.</td>
  </tr>
  <tr>
    <td>Estacion</td>
    <td>10/10</td>
    <td><strong>Claridad</strong>: Separa cada elemento del enumerado en una nueva línea, mejora la legibilidad.</td>
  </tr>
  <tr>
    <td>Alergia</td>
    <td>6/10</td>
    <td>
      <strong>Funcionalidad</strong>: Los atríbutos minSeveridad y maxSeveridad son finales y deben inicializarse. En el constructor se debe validar que la severidad está en rango válido.<br>
      <strong>Claridad</strong>: Usa el tabulador para dejar en el constructor todas las líneas de código al mismo nivel de indentación.<br>
      <strong>Cobertura de casos límite y gestión de excepciones</strong>: El método setSeveridad, debería lanzar una excepción AlergiasException si se intenta establecer una severidad fuera de rango.<br>
      <strong>Eficiencia</strong>: ¿Está bien resuelto en cuanto a tiempo y espacio?<br>
      <strong>Calidad del código auxiliar</strong>: ¿Descompone la lógica en métodos privados útiles?<br>
      <strong>Buenas prácticas locales</strong>: ¿Usa estructuras de control y variables adecuadas?
    </td>
  </tr>
  <tr>
    <td>AlergiaAlimenticia</td>
    <td>8/10</td>
    <td>
      <strong>Funcionalidad</strong>: Cuando heredas, debes llamar al constructor del padre (super()) para que se puedan inicializar los atributos declarados en él.<br>
      <strong>Claridad</strong>: En los constructores, cuando declaras los parámetros formales, usa nombres descriptivos.<br>
     </td>
  </tr>
  <tr>
    <td>AlergiaAmbiental</td>
    <td>10/10</td>
    <td>
      <strong>Correcto</strong>
    </td>
  </tr>
    <tr>
    <td>Paciente</td>
    <td>0/10</td>
    <td>
      <strong>Cobertura de casos límite y gestión de excepciones</strong>: en addAlergia, deberías controlar si la alergia que entra es null para lanzar una AlergiasException.<br>
      <strong>Eficiencia</strong>: En alergiasSeveridad, puedes buscar en una sola iteración, así es más rápido.<br>
      <strong>Calidad del código auxiliar</strong>: En alergiasSeveridad podrías haber creado un método privado para comprobar si una alergia supera un umbral, así queda más legible el código.<br>
      <strong>Buenas prácticas locales</strong>: En alergiasSeveridad, puedes usar un bucle for-each ya que tienes que recorrer la estructura entera. Es menos verboso que le while, que requiere de variables auxiliares.
    </td>
  </tr>
</table>
    """

    def validate_path(self, input_file):
        # Verifica si el archivo existe
        if os.path.isfile(input_file):
            return True
        # Verifica la extensión del archivo
        if input_file.endswith(".java"):
            return True
        return False

    def input_files(self, input_folder):
        """
        Returns a list of all Java files in the input_folder (recursively).
        """
        files = []
        for root, _, files_in_dir in os.walk(input_folder):
            for file in files_in_dir:
                if file.endswith(tuple(".java")):
                    full_path = os.path.join(root, file)
                    files.append(full_path)
        return files

    def build_project(self, input_folder):
        """
        Copies user C file to the working directory, compiles the project using Maven,
        and returns the concatenated user code and the compilation output.
        """
        work_space_folder = os.path.dirname(os.path.abspath(__file__)) + "/workspace/"
        main_path = work_space_folder + "src/main/java/"
        compilation_output = ""
        userCode = ""
        try:
            input_files = self.input_files(input_folder)
            for input_file in input_files:
                # Construye el destino manteniendo la estructura desde "src/"

                if not self.validate_path(input_file):
                    print(
                        f"Formato de archivo inválido (debe empezar con src/): {input_file}"
                    )
                    continue

                # Quita del input file todo lo que va antes del src y el src
                quitado_src = input_file.split("src/")[-1]
                # pon en minuscula lo que va antes del /
                quitado_src = quitado_src[0].lower() + quitado_src[1:]
                dest_path = os.path.join(main_path, quitado_src)

                os.makedirs(os.path.dirname(input_file), exist_ok=True)
                shutil.copy(input_file, dest_path)

                # Command to execute
            command = f"""mvn -f {work_space_folder} compile"""

            result = subprocess.run(command, shell=True, text=True, capture_output=True)

            compilation_output = (
                "Compila con ERRORES."
                if "COMPILATION ERROR" in result.stdout
                else "Compila correctamente. "
            )

            # Read the contents of all the files in the inputs_files and append to userCode
            for input_file in input_files:
                # Read the contents of the file
                with open(input_file, "r") as f:
                    content = f.read()
                    # Append the content to userCode
                    userCode += content + "\n ------------------\n"
        except Exception as e:
            print("An error occurred while running the compilation command:", str(e))

        return userCode, compilation_output
