#include "polinomio.h"
#include <stdlib.h>
#include <stdio.h>


/**
 * @brief Verifica si el polinomio dado tiene contenido.
 *
 * Esta función determina si la estructura de polinomio proporcionada
 * contiene algún contenido significativo o está vacía.
 *
 * @param polinomio Puntero a una estructura `Polinomio` que se va a verificar.
 * @return Un entero que indica si el polinomio tiene contenido.
 *         Generalmente, un valor distinto de cero indica la presencia de contenido,
 *         mientras que cero indica que no hay contenido.
 */
int es_polinomio_con_contenido(const struct Polinomio *polinomio)
{
    return (polinomio != NULL && polinomio->ultimo != NULL);
}


/**
 * @brief Busca el monomio actual y el anterior en un polinomio dado un exponente.
 *
 * @param polinomio Puntero constante al polinomio en el que se realizará la búsqueda.
 * @param exponente El exponente del monomio que se desea buscar.
 * @param actual Doble puntero donde se almacenará el monomio actual encontrado (si existe).
 * @param anterior Doble puntero donde se almacenará el monomio anterior al encontrado (si existe).
 *
 * Esta función recorre el polinomio y localiza el monomio con el exponente especificado.
 * Si se encuentra, se asigna el puntero correspondiente al parámetro `actual`.
 * Si existe un monomio anterior al encontrado, se asigna al parámetro `anterior`.
 * Si no se encuentra el monomio o no hay un monomio anterior, los punteros se asignan a NULL.
 */
void buscar_anterior_actual_monomio_exponente(const struct Polinomio *polinomio, int exponente, struct Monomio ** actual, struct Monomio ** anterior)
{
    *actual = polinomio->primero;
    *anterior = NULL;

    while (*actual != NULL && exponente > (*actual)->exponente)
    {
        *anterior = *actual;
        *actual = (*actual)->siguiente;
    }
}


/**
 * @brief Crea un polinomio.
 *
 * Esta función se encarga de crear un polinomio, reservando la memoria
 * necesaria para la estructura que lo representa. Inicializa los valores
 * de la estructura para que esté listo para su uso posterior. En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 *
 * @param polinomio Puntero a la estructura Polinomio que se va a crear.
 */
void poly_crear(struct Polinomio **polinomio)
{
    *polinomio = (struct Polinomio*)malloc(sizeof(struct Polinomio));
    if (*polinomio == NULL)
    {
        exit(-1);
    }
    (*polinomio)->primero = NULL;
    (*polinomio)->ultimo = NULL;
}


/**
 * @brief Obtiene el grado de un polinomio.
 *
 * @param polinomio Puntero a la estructura que representa el polinomio.
 * @return int El grado del polinomio. Devuelve -1 en caso de no poder calcularlo.
 */
int poly_grado(const struct Polinomio *polinomio)
{
    int resultado = -1;
    struct Monomio *p = polinomio->primero;
    while (p->siguiente!=NULL){
        p = p->siguiente;
    }
    resultado = p->exponente;
    return 0;
}


/**
 * @brief Crea un monomio con el coeficiente y exponente dados.
 * 
 * @param monomio Puntero doble a una estructura Monomio donde se almacenará el monomio creado.
 * @param coeficiente El coeficiente del monomio.
 * @param exponente El exponente del monomio.
 */
int poly_coeficiente(const struct Polinomio *polinomio, int exponente)
{
    int resultado = 0;
    // Si no existe el polinomio 
    if (es_polinomio_con_contenido(polinomio))
    {
        //Buscamos el monomio, están ordenados por exponente
        struct Monomio *actual;
        struct Monomio *anterior;
        buscar_anterior_actual_monomio_exponente(polinomio, exponente,&actual,&anterior);

        //Se ha econtrado actualizamos el resultado
        if (actual != NULL && actual->exponente == exponente)
        {
            resultado= actual->coeficiente;
        }
    }
    return resultado;
}

/**
 * @brief Inserta un monomio en un polinomio. En caso de existir suma (ojo que coef puede ser negativo o positivo, si queda a cero se elimina)
 * En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 * @param p Puntero a la estructura que representa el polinomio.
 * @param coef El coeficiente del monomio.
 * @param exp El exponente del monomio, debe ser mayor o igual a 0.
 * @return int En caso de no poder agregar, devuelve -1 en caso de no poder agregar. Devuelve 0 si puede agregar.
 */
int poly_agregar(struct Polinomio *polinomio, int coeficiente, int exponente)
{
    if (polinomio == NULL || coeficiente == 0 || exponente < 0)
    {
        return -1;
    }
    if (polinomio->primero == NULL)
    {
        struct Monomio* n = (struct Monomio*)malloc(sizeof(struct Monomio));
        if (n==NULL)
            exit(-1);

        n->coeficiente = coeficiente;
        n->exponente = exponente;
        n->siguiente = NULL;
        polinomio->primero = n;
        polinomio->ultimo = n;
    }
    else
    {
        struct Monomio* it = polinomio->primero;
        struct Monomio* prev = NULL;
        while (it != NULL && exponente > it->exponente)
        {
            prev = it;
            it = it->siguiente;
        }
        //Existe ya un monomio de ese grado
        if (it == NULL || it->exponente != exponente)
        {
            struct Monomio* n = (struct Monomio*)malloc(sizeof(struct Monomio));
            if(n==NULL)
                exit(-1);
            n->coeficiente = coeficiente;
            n->exponente = exponente;
            if (n == NULL)
            {
                return -1;
            }
            //Puede estar al principio el medio o el final
            //Al principio
            if (prev == NULL)
            {
                n->siguiente = polinomio->primero;
                polinomio->primero = n;
            }
            //Al final
            else if (it == NULL)
            {
                prev->siguiente = n;
                n->siguiente = NULL;
                polinomio->ultimo = n;
            }
            //En medio
            else
            {
                prev->siguiente = n;
                n->siguiente = it;
            }
        }
    }
    return 0;
}


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
void poly_imprimir(const struct Polinomio *polinomio)
{
    if(es_polinomio_con_contenido(polinomio))
    {
        struct Monomio* it = polinomio->primero;
        while (it != NULL)
        {
            printf("%dx^%d ", it->coeficiente, it->exponente);
            it = it->siguiente;
        }
        printf("\n");
    }
    else printf("Polinomio no existe.\n");
}

/**
 * @brief Destruye un polinomio liberando la memoria que ocupaba y dejando la estructura inicializada para alojar otro polinomio.
 *
 * Esta función se encarga de liberar la memoria que ocupaba un polinomio
 * previamente inicializado. Se encarga de liberar la memoria de cada monomio
 * que lo compone. Deja la estrutura struct Polinomio lista ser usada de nuevo.
 *
 * @param polinomio Puntero a la estructura Polinomio que se va a poly_destruir.
 */
void poly_destruir(struct Polinomio *polinomio)
{
    if (es_polinomio_con_contenido(polinomio)) // Si está inicializado y tiene al menos un monomio
    {
        struct Monomio* cabeza = polinomio->primero;
        struct Monomio *monomio_liberar;
        while (cabeza != NULL)
        {
            monomio_liberar = cabeza;
            cabeza = cabeza->siguiente;
            free(monomio_liberar);
        }
    }
    polinomio->primero = NULL;
    polinomio->ultimo = NULL;
}

/**
 * @brief Suma dos polinomios.
 *
 * Esta función toma dos estructuras de polinomios como entrada y devuelve una NUEVA estructura de polinomio que representa la suma de los dos polinomios de entrada.
 * En caso de no poder realizar la suma, se debe devolver NULL.
 * En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 *
 * @param p1 Puntero al primer polinomio.
 * @param p2 Puntero al segundo polinomio.
 * @return Puntero a una nueva estructura de polinomio que representa la suma de p1 y p2.
 */

struct Polinomio *poly_sumar(const struct Polinomio *p1, const struct Polinomio *p2)
{
    struct Polinomio* polinomio=NULL;
    poly_crear(&polinomio);

    struct Monomio* cabezaPrimero = (p1!=NULL?p1->primero:NULL);
    struct Monomio* cabezaSegundo = (p2!=NULL?p2->primero:NULL);

    while(cabezaPrimero!=NULL || cabezaSegundo !=NULL){
        if(cabezaPrimero == NULL){ //Si el primero no le quedan elementos o tiene exponente menor, añadimos el segundo
            poly_agregar(polinomio, cabezaSegundo->coeficiente, cabezaSegundo->exponente);
            cabezaSegundo = cabezaSegundo->siguiente;
        }
        else if(cabezaSegundo == NULL){ //Si el segundo no le quedan elementos o tiene exponente menor, añadimos el primero
            poly_agregar(polinomio, cabezaPrimero->coeficiente, cabezaPrimero->exponente);
            cabezaPrimero = cabezaPrimero->siguiente;
        }
        else if(cabezaPrimero->exponente < cabezaSegundo->exponente){ //Si el primero tiene menor exponente, lo añadimos
            poly_agregar(polinomio, cabezaPrimero->coeficiente, cabezaPrimero->exponente);
            cabezaPrimero = cabezaPrimero->siguiente;
        }
        else if(cabezaPrimero->exponente > cabezaSegundo->exponente){ //Si el segundo tiene menor exponente, lo añadimos
            poly_agregar(polinomio, cabezaSegundo->coeficiente, cabezaSegundo->exponente);
            cabezaSegundo = cabezaSegundo->siguiente;
        }
        else{ //Si son iguales sumamos los coeficientes
            poly_agregar(polinomio, (cabezaPrimero->coeficiente + cabezaSegundo->coeficiente), cabezaPrimero->exponente);
            cabezaPrimero = cabezaPrimero->siguiente;
            cabezaSegundo = cabezaSegundo->siguiente;
        }
    }
    return polinomio;
}


