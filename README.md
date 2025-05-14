# LLMCoevaluator

## Introducción

Este repositorio acompaña al artículo **“Coevaluando con LLM: generando una retroalimentación formativa a tiempo”** enviado a las *XXXI Jornadas sobre la Enseñanza Universitaria de la Informática (JENUI 2025)*, en el que se propone una metodología de coevaluación entre docente e inteligencia artificial para asignaturas de programación. 

La retroalimentación formativa es una herramienta pedagógica clave para fomentar la reflexión y el aprendizaje significativo. Sin embargo, proporcionar comentarios detallados y a tiempo en contextos con muchos estudiantes supone una carga excesiva para el profesorado. 

Para abordar este problema, se plantea una solución basada en **Modelos de Lenguaje de Gran Tamaño (LLM)** que actúan como evaluadores automáticos preliminares. Estos modelos generan una evaluación inicial del código del estudiante, que luego es revisada y ajustada por el docente. De esta forma, se reduce el tiempo necesario para ofrecer retroalimentación útil sin comprometer la calidad ni la fiabilidad del proceso.

Este repositorio contiene el código necesario para realizar esta coevaluación en dos fases:

1. Generación automática de retroalimentación usando LLM.
2. Revisión y ajuste por parte del docente para su entrega final en la plataforma Moodle.

<p align="center">
    <img src="image.png" alt="Vista del sistema" width="30%">
</p>

<p align="center">
    <em>Figura 1: Sistema propuesto para coevaluación con LLM.</em>
</p>


A continuación se describen los pasos para hacer uso de esta herramienta.

---

# Paso 0: Instalación y configuración

Se incluye un archivo `requirements.txt` para facilitar la instalación de las dependencias necesarias.

Además, es necesario completar las API Keys en el archivo `.env`. Este archivo ya está preparado para incluir claves de acceso a modelos de OpenAI y Anthropic. Todo el sistema está diseñado para tener esta carpeta en la raíz del proyecto.

---

# Paso 1: Evaluación automática con LLM

Actualmente se soportan dos lenguajes: **C (con GCC)** y **Java (con Maven)**. Esto sólo es necesario para compilar el código y es un paso que se podría saltar si es necesario.

Puedes utilizar **Google Colab Pro** para aprovechar GPU potentes, o bien utilizar las APIs comerciales de los LLM desde tu ordenador local.

## Evaluación en Java

En la carpeta `Java/` se incluyen dos notebooks:

- `Paso1_EvaluadorColabProJavaMVN.ipynb`: para uso en Google Colab Pro.
- `Paso1_EvaluadorRetroalimentacionJava.ipynb`: para uso en local.

Dentro de esta carpeta se encuentra un directorio `EspacioTrabajo` con un proyecto base.

Los evaluadores recorren los archivos `*.java` en la carpeta `pruebas`, los integran en el proyecto, y los compilan. Aunque se comprueba si el código compila, **la salida del compilador no se incluye en el prompt del LLM**, ya que no se ha observado un impacto positivo al hacerlo.

El código del estudiante, junto con una rúbrica (general y específica) y un ejemplo de salida esperado, se introduce en el prompt para que el LLM genere la retroalimentación.

## Evaluación en C

El procedimiento es análogo al de Java.

En la carpeta `C/` se incluyen:

- `Paso1_EvaluadorColabProC.ipynb`: para uso en Google Colab Pro.
- `Paso1_EvaluadorRetroalimentacionJava.ipynb`: (sí, aún con nombre “Java”, se usa también para C).

Se incluye un ejemplo de proyecto y pruebas en las subcarpetas `EspacioTrabajo/` y `pruebas/`.

Los evaluadores recorren archivos `*.c`, integran el código, compilan y formulan una petición al LLM con el prompt adecuado (rúbricas, código y resultado de la compilación).

---

# Licencia y contacto

Este trabajo ha sido desarrollado por:

- Joaquín Ballesteros — [jballesteros@uma.es](mailto:jballesteros@uma.es)
- Pablo Franco — [pablo.franco@uma.es](mailto:pablo.franco@uma.es)
- Lidia Fuentes — [lfuentes@uma.es](mailto:lfuentes@uma.es)

Universidad de Málaga, ITIS Software — Grupo CAOSD.

Si usas este código o metodología en tu investigación o docencia, te invitamos a citar el artículo asociado.

---

