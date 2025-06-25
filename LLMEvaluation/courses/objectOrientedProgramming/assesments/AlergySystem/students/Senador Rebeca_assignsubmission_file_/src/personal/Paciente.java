package personal;

import java.util.ArrayList;
import alergias.Alergia;
import alergias.AlergiasException;

public class Paciente {
	private final String nombre;
	private int edad;
	private ArrayList<Alergia> alergias;
	
	public Paciente(String n, int e) {
		this.nombre = n;
		this.edad = e;
		alergias = new ArrayList<>();
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public String getNombre() {
		return nombre;
	}

	public ArrayList<Alergia> getAlergias() {
		return alergias;
	}
	
	public boolean addAlergia(Alergia a) throws AlergiasException {
		alergias = new ArrayList<Alergia>();
		if(a == null) {
			throw new AlergiasException("No se puede añadir una alergia sin inicializar");
		}
		if(!alergias.contains(a)) {
			alergias.add(a);
			return true;
		}
		return false;
		
	}
	
	public boolean removeAlergia(Alergia a) {
		for(int i = 0; i<alergias.size(); i++) {
			if(a.equals(alergias.get(i))) {
				alergias.remove(i);
				return true;
			}
		}
		return false;
	}
	
	public ArrayList<Alergia> alergiasSeveridad(int u) {
		ArrayList<Alergia> nuevo = new ArrayList<Alergia>();
		for(Alergia a : alergias) {
			if(a.getSeveridad()>=u) {
				nuevo.add(a);
			}
		}
		return nuevo;
	}
	
	public String toString() {
		StringBuilder sb = new StringBuilder("--Paciente--");
		sb.append("\n");
		sb.append("Nombre: "+nombre);sb.append("\n");
		sb.append("Edad: "+edad);sb.append("\n");
		sb.append("Alergias: ");sb.append("\n");
		
		for(Alergia a : alergias) {
			sb.append(a);
		}
		
		return sb.toString();
	}
	
	
	
	
	
	
}
