package alergias;

import java.util.List;

public class AlergiaAmbiental extends Alergia{
	private List<Estacion> estaciones;
	
	public AlergiaAmbiental(String d, int s, List<Estacion> l) throws AlergiasException {
		super(d,s);
		estaciones = l;
	}

	public List<Estacion> getEstaciones() {
		return estaciones;
	}
	
	public String toString() {
		return "[Ambiental, "+getSeveridad()+", "+estaciones+", "+getDescripcion()+"]";
	}
}
