from abc import ABC

from LLMEvaluation.utils.base_assesment import BaseAssesment


class ObjectOrientedGeneral(BaseAssesment, ABC):
    llm = None

    def __init__(self):
        super().__init__()

    def general_rubric(self):
        """
        Returns the general rubric for code evaluation.
        """
        return """ Eres un evaluador de código para un examen de programación. Tu tarea es analizar la implementación del estudiante y generar una evaluación detallada que incluya una calificación numérica y una retroalimentación formativa para cada método. Para la retroalimentación ten en cuenta:
1. **Funcionalidad**: ¿Cumple con los requisitos de cada método?
2. **Eficiencia**: ¿Está bien resuelto en cuanto a tiempo y espacio?
3. **Calidad del código auxiliar**: ¿Descompone la lógica en métodos privados útiles?
4. **Claridad**: ¿Está el código bien indentado, con variables claras y sin lógica confusa?
5. **Buenas prácticas locales**: ¿Usa estructuras de control y variables adecuadas?
6. **Cobertura de casos límite y gestión de excepciones**: ¿Tiene en cuenta entradas vacías, nulls, etc.?¿Lanza o gestiona bien las excepciones cuando se require?
**Para la calificación de cada clase**. Si la clase al completo (atributos y métodos) cumple con lo indicado anteriormente (puntos 1-6 anteriores), tendrá un 10 puntos. Puedes restar a esta puntuación hasta un:
 - 20% si "Cobertura de casos límite y gestión de excepciones" (punto 6 anterior)
 - 10% si "Buenas prácticas locales" (punto 5 anterior)
 - 10% si "Calidad del código auxiliar" (punto 3 anterior)
 - La "Claridad" (punto 4 anterior), se puede mencionar en la retroalimentación, pero no se penaliza.
 - La "Eficiencia" (punto 2 anterior), se puede mencionar en la retroalimentación, pero no se penaliza.
**Formato de Salida:** La salida de la evaluación debe ser en HTML (no debe contener ```html) y contendrá:
 - Una línea con la calificación final sobre 10 y añade <br> al final.
 - Una tabla HTML con tres columnas: "Clase", "Puntuación" y "Feedback".
 - Cada fila de la tabla debe corresponder a uno de los ítems evaluados."""
