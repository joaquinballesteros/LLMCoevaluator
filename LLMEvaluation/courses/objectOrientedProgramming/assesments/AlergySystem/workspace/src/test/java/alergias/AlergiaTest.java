package alergias;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;

public class AlergiaTest {

    @Test
    @DisplayName("Crear AlergiaAlimenticia válida y verificar toString")
    void testAlergiaAlimenticiaValida() {
        AlergiaAlimenticia aa = new AlergiaAlimenticia("Reacción a mariscos", 7, TipoAlimento.MARISCOS);
        assertEquals("Reacción a mariscos", aa.getDescripcion());
        assertEquals(7, aa.getSeveridad());
        assertEquals(TipoAlimento.MARISCOS, aa.getTipo());
        assertEquals("[Alimenticia, MARISCOS, 7, Reacción a mariscos]", aa.toString());
    }

    @Test
    @DisplayName("Crear AlergiaAmbiental válida y verificar toString")
    void testAlergiaAmbientalValida() {
        List<Estacion> estaciones = Arrays.asList(Estacion.PRIMAVERA, Estacion.OTOÑO);
        AlergiaAmbiental aa = new AlergiaAmbiental("Polen", 6, estaciones);
        assertEquals("Polen", aa.getDescripcion());
        assertEquals(6, aa.getSeveridad());
        assertEquals(estaciones, aa.getEstaciones());
        assertEquals("[Ambiental, 6, [PRIMAVERA, OTOÑO], Polen]", aa.toString());
    }

    @Test
    @DisplayName("Lanzar excepción si severidad es inválida")
    void testSeveridadInvalida() {
        Exception ex = assertThrows(AlergiasException.class, () -> new AlergiaAlimenticia("Gluten", 11, TipoAlimento.GLUTEN));
        assertTrue(ex.getMessage().contains("Severidad debe estar en el rango"));
    }
}