package alergias;

import java.util.ArrayList;
import java.util.List;

public class AlergiaAmbiental extends Alergia {
	private List<Estacion>estaciones;
	
	public AlergiaAmbiental(String descripcion,int severidad,List<Estacion>estaciones) {
		super(descripcion,severidad);
		this.estaciones=estaciones;
	}
	public List<Estacion> getEstaciones(){
		return estaciones;
	}
	@Override
	public String toString() {
		return "[Ambiental, "+ severidad+", "+estaciones+", "+descripcion;
	}
	

}
//Vacia la lista de estaciones