#ifndef POLINOMIO_H_
#define POLINOMIO_H_

struct Monomio
{
	int coeficiente;
	int exponente;
	struct Monomio *siguiente;
};

struct Polinomio
{
	struct Monomio *primero;
	struct Monomio *ultimo;
};

/**
 * @brief Crea un polinomio.
 *
 * Esta función se encarga de crear un polinomio, reservando la memoria
 * necesaria para la estructura que lo representa. Inicializa los valores
 * de la estructura para que esté listo para su uso posterior. En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 *
 * @param polinomio Puntero a la estructura Polinomio que se va a crear.
 */
void poly_crear(struct Polinomio **polinomio); // 1 punto

/**
 * @brief Obtiene el grado de un polinomio.
 *
 * @param polinomio Puntero a la estructura que representa el polinomio.
 * @return int El grado del polinomio. Devuelve -1 en caso de no poder calcularlo.
 */
int poly_grado(const struct Polinomio *polinomio); // 1 punto

/**
 * @brief Obtiene el coeficiente de un polinomio.
 *
 * @param polinomio Puntero a la estructura que representa el polinomio.
 * @param exponente El exponente del monomio.
 * @return int El coeficiente del monomio, o 0 si no existe, puede ser negativo (-3x^2).
 */
int poly_coeficiente(const struct Polinomio *polinomio, int exponente); // 1 punto

/**
 * @brief Inserta un monomio en un polinomio. En caso de existir suma (ojo que coeficiente puede ser negativo o positivo, si queda a cero se elimina)
 * En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 * @param polinomio Puntero a la estructura que representa el polinomio.
 * @param coeficiente El coeficiente del monomio.
 * @param exponente El exponente del monomio, debe ser mayor o igual a 0.
 * @return int En caso de no poder agregar, devuelve -1. Devuelve 0 si puede agregar.
 */
int poly_agregar(struct Polinomio *polinomio, int coeficiente, int exponente); // 2.5 puntos

/**
 * @brief Imprime los coeficientes y exponentes de un polinomio.
 *
 * Esta función toma un puntero a una estructura Polinomio y
 * muestra en la salida estándar los coeficientes y exponentes
 * del polinomio en un formato legible.
 * Un ejemplo de salida:
 * 3x^2 2x^4 4x^5
 * Otro ejemplo cuando el polinomio no existe:
 * Polinomio no existe.
 *
 * @param polinomio Puntero a la estructura Polinomio que se desea poly_imprimir.
 */
void poly_imprimir(const struct Polinomio *polinomio); // 1.25 punto

/**
 * @brief Destruye un polinomio liberando la memoria que ocupaba y dejando la estructura inicializada para alojar otro polinomio.
 *
 * Esta función se encarga de liberar la memoria que ocupaba un polinomio
 * previamente inicializado. Se encarga de liberar la memoria de cada monomio
 * que lo compone. Deja la estrutura struct Polinomio lista ser usada de nuevo.
 *
 * @param polinomio Puntero a la estructura Polinomio que se va a poly_destruir.
 */
void poly_destruir(struct Polinomio *polinomio); // 1.25 punto

/**
 * @brief Suma dos polinomios.
 *
 * Esta función toma dos estructuras de polinomios como entrada y devuelve una NUEVA estructura de polinomio que representa la suma de los dos polinomios de entrada.
 * En caso de no poder realizar la suma, se debe devolver NULL.
 * En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 *
 * @param polinomio1 Puntero al primer polinomio.
 * @param polinomio2 Puntero al segundo polinomio.
 * @return Puntero a una nueva estructura de polinomio que representa la suma de polinomio1 y polinomio2.
 */

struct Polinomio *poly_sumar(const struct Polinomio *polinomio1, const struct Polinomio *polinomio2); // 2 punto
#endif																				  /* POLINOMIO_H_ */
