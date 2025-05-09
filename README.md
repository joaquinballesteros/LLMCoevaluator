# LLMCoevaluator

Se incluye el requirements.txt para facilitar la instalación de las dependencias necesarias.

# COevaluador.ipynb
Programa para realizar la coevaluación. Espera una carpeta con los códigos de los estudiantes y un fichero CSV. En la primera parte del fichero están los parámetros para configurarlo. 
maximo_lineas = 60      # Número par con el largo de la intefaz, reducir si tu pantalla es más pequeña :)
lenguaje_programacion = ".java" # lenguaje de programación que vamos a corregir.
fichero_correciones_csv = "Calificaciones.csv" # Fichero que descargamos de Moodle de la actividad
fichero_solucion="" #Fichero con la solución del examen, en caso de no tener solución dejar vacío ""

# EvaluadorColabProC.ipynb
Proyecto para ser usado en Colab Pro para evaluar un conjunto de examenes en C usando el modelo de software libre Qwen2.5 con quantizacion.

#EvaluadorColabProJava.ipynb
Proyecto para ser usado en Colab Pro para evaluar un conjunto de examenes en JAVA usando el modelo de software libre Qwen2.5 con quantizacion.

# GeneradorRetroalimentacionEjemploC.ipynb
Proyecto para ser usado en VSCode con anaconda para evaluar un conjunto de examenes en C usando la API de OpenAI. DEbes tener configurado el token para hacer uso del mismo.

#GeneradorRetroalimentacionJavaMVN.ipynb
Proyecto para ser usado en VSCode con anaconda para evaluar un conjunto de examenes en JAVA usando la API de OpenAI. DEbes tener configurado el token para hacer uso del mismo.
