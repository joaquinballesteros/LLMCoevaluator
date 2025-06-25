package personal;

import static org.junit.jupiter.api.Assertions.*;

import alergias.*;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class PacienteTest {

    @Test
    @DisplayName("Crear paciente y verificar getters")
    void testCrearPaciente() {
        Paciente p = new Paciente("Luis", 30);
        assertEquals("Luis", p.getNombre());
        assertEquals(30, p.getEdad());
        assertTrue(p.getAlergias().isEmpty());
    }

    @Test
    @DisplayName("Agregar alergia válida")
    void testAgregarAlergia() {
        Paciente p = new Paciente("Ana", 25);
        Alergia a = new AlergiaAlimenticia("Frutos secos", 5, TipoAlimento.FRUTOS_SECOS);
        assertTrue(p.addAlergia(a));
        assertEquals(1, p.getAlergias().size());
    }

    @Test
    @DisplayName("Eliminar alergia existente")
    void testEliminarAlergia() {
        Paciente p = new Paciente("Lucía", 50);
        Alergia a = new AlergiaAlimenticia("Lactosa", 4, TipoAlimento.LACTOSA);
        p.addAlergia(a);
        assertTrue(p.removeAlergia(a));
        assertTrue(p.getAlergias().isEmpty());
    }

    @Test
    @DisplayName("Filtrar alergias por severidad")
    void testFiltrarPorSeveridad() {
        Paciente p = new Paciente("Miguel", 22);
        p.addAlergia(new AlergiaAlimenticia("Mariscos", 3, TipoAlimento.MARISCOS));
        p.addAlergia(new AlergiaAlimenticia("Frutos secos", 8, TipoAlimento.FRUTOS_SECOS));
        assertEquals(1, p.alergiasSeveridad(5).size());
    }

    @Test
    @DisplayName("Verificar toString de paciente con alergias")
    void testToStringPaciente() {
        Paciente p = new Paciente("Elena", 28);
        Alergia a1 = new AlergiaAlimenticia("Gluten", 6, TipoAlimento.GLUTEN);
        Alergia a2 = new AlergiaAmbiental("Polen", 5, Arrays.asList(Estacion.PRIMAVERA));
        p.addAlergia(a1);
        p.addAlergia(a2);

        String salida = p.toString();
        assertTrue(salida.contains("Nombre: Elena"));
        assertTrue(salida.contains("Edad: 28"));
        assertTrue(salida.contains(a1.toString()));
        assertTrue(salida.contains(a2.toString()));
    }

    @Test
    @DisplayName("Lanzar excepción al añadir alergia nula")
    void testAlergiaNula() {
        Paciente p = new Paciente("Pedro", 33);
        assertThrows(AlergiasException.class, () -> p.addAlergia(null));
    }
}