import os
from LLMEvaluation.courses.dataStructures.data_structures_general import (
    DataStucturesGeneral,
)
import shutil  # To copy the student's code into the project for compilation
import subprocess  # To execute Java compilation and execution commands


class PolyC(DataStucturesGeneral):
    llm = None

    def __init__(self):
        super().__init__()

    def specific_rubric(self):
        """
        Returns the specific rubric for SplayTree methods.
        """
        return """Estos son los métodos a evaluar y dar una retroalimentación formativa:
 - `void poly_crear(struct Polinomio **polinomio)` (1 punto): Esta función se encarga de crear un polinomio, reservando la memoria necesaria para la estructura que lo representa y debe asignar a *p la memoria incializada. Inicializa los valores de la estructura para que esté listo para su uso posterior. En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 - `int poly_grado(const struct Polinomio *polinomio)` (1 punto): Obtiene el grado de un polinomio. Devuelve -1 en caso de no poder calcularlo.
 - `int poly_coeficiente(const struct Polinomio *polinomio, int exponente)` (1 punto): Obtiene el coeficiente de un polinomio. Devuelve el coeficiente del monomio, o 0 si no existe, puede ser negativo (-3x^2).
 - `int poly_agregar(struct Polinomio *polinomio, int coeficiente, int exponente)`(2.5 puntos): Inserta un monomio en un polinomio. En caso de existir suma (ojo que coeficiente puede ser negativo o positivo, si queda a cero se elimina). En caso de no poder pedir memoria, debe finalizar el programa con código -1. En caso de no poder agregar, devuelve -1 en caso de no poder agregar. Devuelve 0 si puede agregar
 - `void poly_imprimir(const struct Polinomio *polinomio)` (1.25 puntos): Imprime los coeficientes y exponentes de un polinomio. Esta función toma un puntero a una estructura Polinomio y muestra en la salida estándar los coeficientes y exponentes del polinomio en un formato legible. Un ejemplo de salida:3x^2 2x^4 4x^5 .Otro ejemplo cuando el polinomio no existe: Polinomio no existe.
 - `void poly_destruir(struct Polinomio *polinomio)`(1.25 puntos): Destruye un polinomio liberando la memoria que ocupaba y dejando la estructura inicializada para alojar otro polinomio. Esta función se encarga de liberar la memoria que ocupaba un polinomio previamente inicializado. Se encarga de liberar la memoria de cada monomio que lo compone. Deja la estructura struct Polinomio lista ser usada de nuevo.
 - `struct Polinomio *poly_sumar(const struct Polinomio *polinomio1, const struct Polinomio *polinomio2)` (2 puntos): Esta función toma dos estructuras de polinomios como entrada y devuelve una NUEVA estructura de polinomio que representa la suma de los dos polinomios de entrada. En caso de no poder realizar la suma, se debe devolver NULL. En caso de no poder pedir memoria, debe finalizar el programa con código -1.

 Esta es la estructura de datos:
 
struct Monomio
{
	int coeficiente;
	int eexponentexp;
	struct Monomio *siguiente;
};

struct Polinomio
{
	struct Monomio *primero;
	struct Monomio *ultimo;
};"""

    def sample_output(self):
        """
        Returns a sample output of the evaluation in HTML format.
        """
        return """
 ** Ejemplo de salida **:
Calificación final: 1/10

<table border="1">
  <tr>
    <th>Método</th>
    <th>Puntuación</th>
    <th>Retroalimentación</th>
  </tr>
  <tr>
    <td>poly_crear</td>
    <td>0.5 / 1</td>
    <td>
      <strong>Funcionalidad:</strong> La función no inicializa correctamente los punteros <code>primero</code> y <code>ultimo</code> después de reservar memoria. <br>
      <strong>Mantenimiento:</strong> Sin comentarios.<br>
      <strong>Claridad:</strong> Se crea una variable <code>aux</code> para pedir memoria y luego se asigna a la variable <code>*p</code>: usa directamente la variable <code>*p</code> y renombra a algo más descriptivo como <code>*polinomio</code>. Esto mejora la claridad del código con nombres descriptivos y elimina el uso de variables innecesarias que complica la compresión del código.<br>
      <strong>Eficiencia:</strong> Sin comentarios.<br>
      <em>Sugerencia Formativa:</em> Asegúrate de inicializar todos los campos de la estructura inmediatamente después de la asignación y utiliza <code>exit(-1)</code> para errores críticos en la reserva de memoria.
    </td>
  </tr>
  <tr>
    <td>poly_grado</td>
    <td>0.5 / 1</td>
    <td>
      <strong>Funcionalidad:</strong> El cálculo del grado del polinomio falla en casos en que el polinomio es nulo o la lista está vacía.<br>
      <strong>Mantenimiento:</strong>Se puede crear una función auxiliar es_polinomio_con_contenido(const struct Polinomio *polinomio) que se encargue de controlar si tiene o no contenido el polinomio. Esta función luego se puede usar en otros métodos y reduce la duplicidad de código que dificulta el mantenimiento.<br>
      <strong>Claridad:</strong> Usa nombres descriptivos para las variables, por ejemplo, en vez de usar <code>r</code>, usa <code>resultado</code>.
      <strong>Eficiencia:</strong> Es ineficiente (O(n)) recorrer la lista para encontrar el grado, ya que se puede hacer en O(1) si accedes al último del polinomio.<br>
      <em>Sugerencia Formativa:</em> La descomposición en subfunciones permite reducir la duplicidad de código y mejorar la legibilidad y el mantenimiento. 
    </td>
  </tr>
  <tr>
    <td>poly_coeficiente</td>
    <td>0.5 / 1</td>
    <td>
      <strong>Funcionalidad:</strong> La función no contempla correctamente el caso en que se solicite un exponente negativo o inexistente.<br>
      <strong>Mantenimiento:</strong>Se puede crear una función auxiliar void buscar_anterior_actual_monomio_exponente(const struct Polinomio *polinomio, int exponente, struct Monomio ** actual, struct Monomio ** anterior) que se encargue de buscar un exponente en el polinomio y de devuelva un puntero al monomio anterior y al actual. Esta función luego se puede usar en otros métodos y reduce la duplicidad de código que dificulta el mantenimiento.<br>
      <strong>Claridad:</strong> Usa nombres descriptivos para las variables, por ejemplo, en vez de usar <code>act</code>, usa <code>actual</code>.
      <strong>Eficiencia:</strong> Sin comentarios <br>
      <em>Sugerencia Formativa:</em> Revisa bien siempre los casos extremos, es dónde más suele fallar el código. ¡Usa la descomposición funcional! Esto permite reducir la duplicidad de código y mejorar la legibilidad y el mantenimiento. 
   </td>
  </tr>
  <tr>
    <td>poly_agregar</td>
    <td>1.0 / 2.5</td>
    <td>ejemp
      <strong>Funcionalidad:</strong> Al insertar un monomio, la función no suma correctamente coeficientes existentes y no elimina los nodos con coeficiente 0.<br>
      <strong>Mantenimiento:</strong> Una función así de larga y sin funciones auxiliares es compleja de mantener. Puedes sacar la inserción en cabeza y en medio/final en funciones a parte.
      <strong>Claridad:</strong> La función es muy larga y es complicada de seguir. Añadir comentarios y hacer uso de funciones auxiliares es vital para que se pueda entender.
      <strong>Eficiencia:</strong> Sin comentarios <br>
      <em>Sugerencia Formativa:</em> Una función muy larga es síntoma de que algo no va bien. Se debe siempre descomponer en bloques más simples, así haces código más mantenible.
    </td>
  </tr>
  <tr>
    <td>poly_imprimir</td>
    <td>1.25 / 1.25</td>
    <td>
      <strong>Funcionalidad:</strong> Sin comentarios <br>
      <strong>Mantenimiento:</strong> Sin comentarios <br>
      <strong>Claridad:</strong> Sin comentarios <br>
      <strong>Eficiencia:</strong> Sin comentarios <br>
      <em>Sugerencia Formativa:</em> Sin comentarios <br>
    </td>
  </tr>
  <tr>
    <td>poly_destruir</td>
    <td>0.75 / 1.25</td>
    <td>
      <strong>Funcionalidad:</strong> La función no libera correctamente todos los nodos, dejando posibles fugas de memoria. Además, debería poner a NULL el último y el primero tras eliminar el resto de nodos.<br>
      <strong>Mantenimiento:</strong> Sin comentarios <br>
      <strong>Claridad:</strong> ¡Usa nombres descriptivos! En vez de <code>aux</code>, puedes usar <code>cabeza</code> que describe mejor qué representa.<br>
      <strong>Eficiencia:</strong> Sin comentarios <br>
      <em>Sugerencia Formativa:</em> Con el depurador puedes ver si se están liberando todos los nodos. Además, es importante poner a NULL los punteros que ya no se usan para evitar errores futuros.
     </td>
  </tr>
  <tr>
    <td>poly_sumar</td>
    <td>1.0 / 2</td>
    <td>
      <strong>Funcionalidad:</strong> La función de suma no maneja correctamente los coeficientes cuando ambos polinomios tienen monomios con el mismo exponente; además, no se verifican los casos en que uno de los polinomios es NULL.<br>
      <strong>Mantenimiento:</strong> Sin comentarios <br>
      <strong>Claridad:</strong> ¡Usa nombres descriptivos! En vez de <code>aux</code>, puedes usar <code>cabeza</code> que describe mejor qué representa.<br>
      <strong>Eficiencia:</strong> Añades primero todos los de un polinomio y luego los del otro. Puedes ir añadiendo a la vez, así no recorres las dos listas al completo (cuando coinciden los exponentes, se suman y avanzan las dos a la vez).<br>
      <em>Sugerencia Formativa:</em> Revisa la salida por pantalla bien, falla en los casos básicos que se proporciona.
    </td>
  </tr>
</table>"""

    def input_files(self, input_folder):
        """
        Returns a list of all Java files in the input_folder (recursively).
        """
        files = []
        for root, _, files_in_dir in os.walk(input_folder):
            for file in files_in_dir:
                if file.endswith(tuple(".c")):
                    full_path = os.path.join(root, file)
                    files.append(full_path)
        return files

    def build_project(self, input_folder):
        """
        Copies user C file to the working directory, compiles the project using Maven,
        and returns the concatenated user code and the compilation output.
        """
        dest_path = (
            os.path.dirname(os.path.abspath(__file__)) + "/workspace/Polinomio.c"
        )
        main_path = (
            os.path.dirname(os.path.abspath(__file__)) + "/workspace/principal.c"
        )
        compilation_output = ""
        userCode = ""
        try:
            input_files = self.input_files(input_folder)
            for input_file in input_files:

                os.makedirs(os.path.dirname(input_file), exist_ok=True)
                compilation_output = ""
                shutil.copy(input_file, dest_path)

            # Command to execute
            command = f"""gcc {main_path} {dest_path} -Wall -Wextra -Wpedantic"""

            result = subprocess.run(command, shell=True, text=True, capture_output=True)

            compilation_output = (
                "compila con ERRORES"
                if "error" in result.stderr or "error" in result.stdout
                else "compila correctamente"
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
