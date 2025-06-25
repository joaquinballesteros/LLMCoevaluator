#include "polinomio.h"
#include <stdlib.h>
#include <string.h>
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
    struct Polinomio* new=(struct Polinomio*)malloc(sizeof(struct Polinomio));
    if(new==NULL){
        printf("No se pudo reservar memoria");
        exit(-1);
    }else{
        new->primero=NULL;
        new->ultimo=NULL;
    }
}

/**
 * @brief Obtiene el grado de un polinomio.
 *
 * @param p Puntero a la estructura que representa el polinomio.
 * @return int El grado del polinomio. Devuelve -1 en caso de no poder calcularlo.
 */
int poly_grado(const struct Polinomio *p)
{
    int res=-1;
    struct Monomio* mon=p->ultimo;
    if(p->ultimo==NULL){
        //printf("No se pudo calcular el grado");
    }else{
        res=p->ultimo->exponente;
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
int poly_coeficiente(const struct Polinomio *p, int exp)
{
    int res=0;
    struct Monomio* mon=p->primero;
    if(p->primero==NULL){
        //printf("No se pudo calcular el grado");
    }else{
        while(mon->siguiente!=NULL){
            if(mon->exponente==exp){
                res=mon->exponente;
            }
            mon=mon->siguiente;
        }
        if(mon->exponente==exp){
                res=mon->exponente;
            }
    }
    return res;
}

/**
 * @brief Inserta un monomio en un polinomio. En caso de existir suma (ojo que coef puede ser negativo o positivo, si queda a cero se elimina)
 * En caso de no poder pedir memoria, debe finalizar el programa con código -1.
 * @param p Puntero a la estructura que representa el polinomio.
 * @param coef El coeficiente del monomio.
 * @param exp El exponente del monomio, debe ser mayor o igual a 0.
 * @return int En caso de no poder agregar, devuelve -1 en caso de no poder agregar. Devuelve 0 si puede agregar.
 */
int poly_agregar(struct Polinomio *p, int coef, int exp)
{
    int res=-1;
    if(p!=NULL && exp >=0){
        struct Monomio* mon=p->primero;
        while(mon->exponente!=exp && res!=0){
            if(mon->exponente==exp && mon==p->primero){
                if(mon->coeficiente+coef!=0){
                mon=mon->coeficiente+coef;
                res=0;
                }else{
                free(p->primero);
                p->primero=NULL;
                p->primero=mon->siguiente;
                res=0;
            }
            if(mon->exponente==exp){
                if(mon->coeficiente+coef!=0){
                mon=mon->coeficiente+coef;
                res=0;
                }else{
                struct Monomio* aux=mon;
                while(aux->siguiente->siguiente!=mon){
                    aux=aux->siguiente;
                }
                aux->siguiente->siguiente=mon->siguiente;
                free(mon);
                mon=NULL;
                res=0;
            }
            }
            if(mon->exponente<exp && exp>mon->siguiente->exponente){
                struct Monomio* new=(struct Monomio*)malloc(sizeof(struct Monomio));
                if(new==NULL){
                    //printf("No se pudo reservar memoria");
                    exit(-1);
                }
                struct Monomio* sig=mon->siguiente;
                new->siguiente=sig;
                new->coeficiente=coef;
                new->exponente=exp;
                res=0;
            }
            mon=mon->siguiente;
        }
        struct Monomio* ultmon=p->ultimo;
        if(ultmon->exponente!=exp && res!=0){
            if(ultmon->coeficiente+coef!=0){
                p->ultimo=ultmon->coeficiente+coef;
                res=0;
            }else{
                struct Monomio* primon=p->primero;
                while(primon->siguiente->siguiente!=NULL){
                    primon=primon->siguiente;
                }
                free(p->ultimo);
                p->ultimo=NULL;
                p->ultimo=primon;
                res=0;
            }
        }
    }
    return res;
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
void poly_imprimir(const struct Polinomio *p)
{ 
    struct Monomio* mon=p->primero;
    if(p==NULL || mon==NULL){
        printf("Polinomio no existe.");
    }else{
    while(mon->sig!=NULL){
        prinf("%dx^%d ",mon->coef,mon->exp);
        mon=mon->sig;
    }
    }
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
void poly_destruir(struct Polinomio *p)
{
   struct Monomio* mon=p->primero->sig;
   struct Monomio* aux=p->primero->sig;
   free(p->primero);
   p->primero=NULL;
   while(aux->sig!=NULL){
        free(mon);
        mon=NULL;
        aux=aux->sig;
        mon=aux;
   }
   free(aux);
    aux=NULL;
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
    struct Monomio* mon1=p1->primero;
    struct Monomio* mon2=p2->primero;
    struct Polinomio* nuevo=(struct Polinomio*)malloc(sizeof(struct Polinomio));
    if(nuevo==NULL){
        printf("No se pudo reservar memoria");
        exit(-1);
    }
    if(mon1->coef!=mon2->coef){
        return NULL;
    }else{

    }
    return nuevo;
}


