#include "polinomio.h"
#include <stdio.h>
#include <assert.h>

void test_poly_crear(void)
{
	struct Polinomio *p;
	poly_crear(&p);
	assert(p != NULL);			// Check if the polynomial was created successfully
	assert(p->primero == NULL); // Check if the first term is NULL
	assert(p->ultimo == NULL);	// Check if the last term is NULL
	poly_destruir(p);			// Check if the polynomial was destroyed successfully
								// Add more assertions based on the expected state of the polynomial
}

void test_poly_monomios_basico(void)
{
	struct Polinomio *p = NULL;
	poly_imprimir(p);				 //  debería imprimir "Polinomio no existe."
	int res = poly_agregar(p, 3, 2); // No está inicializado, debe devolver -1
	assert(res == -1);				 // Comprobamos que devuelva -1
	poly_crear(&p);
	res = poly_agregar(p, 0, 2); // Coeficiente 0, no debería agregar
	assert(res == -1);
	res = poly_agregar(p, 0, 0); // Coeficiente y exp 0, no debería agregar
	assert(res == -1);
	res = poly_agregar(p, 3, 2); // Add term 3x^2
	assert(res == 0);			 // Comprobamos que devuelva 0
	res = poly_agregar(p, 4, 5); // Add term 4x^5
	assert(res == 0);			 // Comprobamos que devuelva 0
	res = poly_agregar(p, 2, 4); // Add term 2x^4
	assert(res == 0);			 // Comprobamos que devuelva 0
	printf("\nDebería ser: 3x^2 2x^4 4x^5\n");
	poly_imprimir(p); //  3x^2 2x^4  4x^5
	poly_destruir(p); // Check if the polynomial was destroyed successfully
}

void test_poly_monomios_suma(void)
{
	struct Polinomio *p;
	poly_crear(&p);
	poly_agregar(p, 3, 2); // Add term 3x^2
	poly_agregar(p, 4, 5); // Add term 4x^5
	poly_agregar(p, 2, 2); // Add term 2x^2
	printf("\nDebería ser: 5x^2 4x^5\n");
	poly_imprimir(p); //  5x^2  4x^5
					  // Add assertions to verify the term was added correctly
	poly_destruir(p); // Check if the polynomial was destroyed successfully
}

void test_poly_monomios_anula(void)
{
	struct Polinomio *p;
	poly_crear(&p);
	poly_agregar(p, 3, 2);	// Add term 3x^2
	poly_agregar(p, 4, 5);	// Add term 4x^5
	poly_agregar(p, -3, 2); // Add term -3x^2
	printf("\nDebería ser: 4x^5\n");
	poly_imprimir(p); //
					  // Add assertions to verify the term was added correctly
	poly_destruir(p); // Check if the polynomial was destroyed successfully
}

void test_poly_coeficiente(void)
{
	struct Polinomio *p = NULL;
	double coef = poly_coeficiente(p, 2);
	assert(coef == 0); // Si pasan NULL, el coeficiente debe ser 0
	poly_crear(&p);
	coef = poly_coeficiente(p, 2);
	assert(coef == 0); // Si no existe, el coeficiente debe ser 0

	poly_agregar(p, 3, 2);		   // Add term 3x^2
	coef = poly_coeficiente(p, 2); // Get coefficient of x^2
	assert(coef == 3);			   // Coefficient should be 3
	poly_destruir(p);			   // Check if the polynomial was destroyed successfully
}

void test_poly_grado(void)
{
	struct Polinomio *p = NULL;
	int grado = poly_grado(p); // Get the degree of the polynomial
	assert(grado == -1);	   // Degree should be 5
	poly_crear(&p);
	grado = poly_grado(p); // Get the degree of the polynomial
	assert(grado == -1);   // Degree should be 5
	poly_agregar(p, 3, 2); // Add term 3x^2
	poly_agregar(p, 4, 5); // Add term 4x^5
	grado = poly_grado(p); // Get the degree of the polynomial
	assert(grado == 5);	   // Degree should be 5
	poly_destruir(p);	   // Check if the polynomial was destroyed successfully
}

void test_poly_sumar(void)
{
	struct Polinomio *p1, *p2, *resultado;
	poly_crear(&p1);
	poly_crear(&p2);

	// Add terms to the first polynomial
	poly_agregar(p1, 3, 2); // 3x^2
	poly_agregar(p1, 4, 5); // 4x^5

	// Add terms to the second polynomial
	poly_agregar(p2, 2, 2); // 2x^2
	poly_agregar(p2, 1, 3); // 1x^3

	// Sum the polynomials
	resultado = poly_sumar(p1, p2);

	// Expected result: 5x^2 1x^3 4x^5
	printf("\nDebería ser: 5x^2 1x^3 4x^5\n");
	poly_imprimir(resultado);

	// Add assertions to verify the result
	assert(poly_coeficiente(resultado, 2) == 5); // Coefficient of x^2 should be 5
	assert(poly_coeficiente(resultado, 3) == 1); // Coefficient of x^3 should be 1
	assert(poly_coeficiente(resultado, 5) == 4); // Coefficient of x^5 should be 4
	assert(poly_grado(resultado) == 5);			 // Degree should be 5
	poly_destruir(p1);							 // Check if the polynomial was destroyed successfully
	poly_destruir(p2);							 // Check if the polynomial was destroyed successfully
	poly_destruir(resultado);							 // Check if the polynomial was destroyed successfully
}

int main(void)
{
	test_poly_crear();
	test_poly_monomios_basico();
	test_poly_monomios_suma();
	test_poly_monomios_anula();
	test_poly_coeficiente();
	test_poly_grado();
	test_poly_sumar();
	printf("Se han pasado todos los test basicos!\n");
	return 0;
}
