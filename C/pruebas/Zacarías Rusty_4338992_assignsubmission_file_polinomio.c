#include "polinomio.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * @brief Crea un polinomio.
 *
 * Esta función se encarga de crear un polinomio, reservando la memoria
 * necesaria para la estructura que lo representa. Inicializa los valores
 * de la estructura para que esté listo para su uso posterior. En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 *
 * @param p Puntero a la estructura Polinomio que se va a crear.
 */
void poly_crear(struct Polinomio **p){
    (*p) = (struct Polinomio*)malloc(sizeof(struct Polinomio));
    if ((*p) == NULL){
        printf("Malloc couldnt allocate memory. Need to exit program");
        exit(1);
    }
    (*p)->primero = NULL;
    (*p)->ultimo = NULL;
}

/**
 * @brief Obtiene el grado de un polinomio.
 *
 * @param p Puntero a la estructura que representa el polinomio.
 * @return int El grado del polinomio. Devuelve -1 en caso de no poder calcularlo.
 */
int poly_grado(const struct Polinomio *p){
    int res = -1;
    if (p != NULL && p->ultimo != NULL){
        res = p->ultimo->exponente;
    }
    return res;
}

/**
 * @brief Obtiene el coeficiente de un polinomio.
 *
 * @param p Puntero a la estructura que representa el polinomio.
 * @param exp El exponente del monomio.
 * @return int El coeficiente del monomio, o 0 si no existe, puede ser negativo (-3x^2).
 */
int poly_coeficiente(const struct Polinomio *p, int exp){
    int res = 0;
    if (p != NULL && exp >= 0){
        struct Monomio* aux = p->primero;
        while(aux != NULL && aux->exponente <= exp){
            if (aux->exponente == exp){
                res = aux->coeficiente;
            }
            aux = aux->siguiente;
        }
    }
    return res;
}


void sumarMonomiosF(struct Polinomio* p, struct Monomio* current, struct Monomio* previous, int coef){
    int borraMonomio = 0;
    current->coeficiente += coef;
    if (current->coeficiente == 0){
        borraMonomio = 1;
    }
    if (borraMonomio == 1){
        if (p->primero == current && p->ultimo == current){
            p->primero = NULL;
            p->ultimo = NULL;
        }else if (p->primero == current){
            p->primero = current->siguiente;
        }else if (p->ultimo == current){
            p->ultimo = previous;
        }
        previous->siguiente = current->siguiente;
        free(current);
    }
}

/**
 * @brief Inserta un monomio en un polinomio. En caso de existir suma (ojo que coef puede ser negativo o positivo, si queda a cero se elimina)
 * En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 * @param p Puntero a la estructura que representa el polinomio.
 * @param coef El coeficiente del monomio.
 * @param exp El exponente del monomio, debe ser mayor o igual a 0.
 * @return int En caso de no poder agregar, devuelve -1 en caso de no poder agregar. Devuelve 0 si puede agregar.
 */
int poly_agregar(struct Polinomio *p, int coef, int exp){
    int res = -1;
    if (p != NULL && exp >= 0 && coef != 0){
        struct Monomio** aux = &(p->primero);
        struct Monomio* previo;
        while((*aux) != NULL && (*aux)->exponente < exp){
            previo = *aux;
            aux = &(*aux)->siguiente;
        }
        if ((*aux) != NULL && (*aux)->exponente == exp){
            sumarMonomiosF(p, (*aux), previo, coef);
        }else{
            struct Monomio* newTerm = (struct Monomio*)malloc(sizeof(struct Monomio));
            if (newTerm == NULL){
                printf("Malloc couldnt allocate memory. Need to exit program");
                exit(1);
            }
            newTerm->coeficiente = coef;
            newTerm->exponente = exp;
            newTerm->siguiente = (*aux);
            (*aux) = newTerm;
            if (newTerm->siguiente == NULL){
                p->ultimo = newTerm;
            }
        }
        res = 0;
    }
    return res;
}

void imprimirMonomio(const struct Monomio* m){
    if (m != NULL){
        printf("%ix^%i ", m->coeficiente, m->exponente);
    }
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
 * @param p Puntero a la estructura Polinomio que se desea poly_imprimir.
 */
void poly_imprimir(const struct Polinomio *p){
    if (p != NULL){
        struct Monomio* aux = p->primero;
        while(aux != NULL){
            imprimirMonomio(aux);
            aux = aux->siguiente;
        }
    }else{
        printf("Polinomio no existe");
    }printf("\n\n");
}

/**
 * @brief Destruye un polinomio liberando la memoria que ocupaba y dejando la estructura inicializada para alojar otro polinomio.
 *
 * Esta función se encarga de liberar la memoria que ocupaba un polinomio
 * previamente inicializado. Se encarga de liberar la memoria de cada monomio
 * que lo compone. Deja la estrutura struct Polinomio lista ser usada de nuevo.
 *
 * @param p Puntero a la estructura Polinomio que se va a poly_destruir.
 */
void poly_destruir(struct Polinomio *p){
    if (p != NULL){
        struct Monomio* head = p->primero;
        struct Monomio* aux;
        while(head != NULL){
            aux = head->siguiente;
            free(head);
            head = aux;
        }
        p->primero = NULL;
        p->ultimo = NULL;
    }
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

struct Polinomio *poly_sumar(const struct Polinomio *p1, const struct Polinomio *p2){
    struct Polinomio* res = NULL;
    poly_crear(&res);
    struct Monomio* aux;
    if (p1 != NULL){
        aux = p1->primero;
        while (aux != NULL){
            poly_agregar(res, aux->coeficiente, aux->exponente);
            aux = aux->siguiente;
        }
    }
    if (p2 != NULL){
        aux = p2->primero;
        while (aux != NULL){
            poly_agregar(res, aux->coeficiente, aux->exponente);
            aux = aux->siguiente;
        }
    }

    return res;
}
