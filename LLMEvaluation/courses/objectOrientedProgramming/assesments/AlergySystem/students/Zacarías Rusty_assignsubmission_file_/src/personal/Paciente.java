package personal;

import java.util.ArrayList;

import alergias.Alergia;
import alergias.AlergiasException;

public class Paciente {
	private final String nombre ;
	private int edad;
	private ArrayList<Alergia>alergias;
	
	public Paciente(String nombre,int edad) {
		this.nombre=nombre;
		this.edad=edad;
		this.alergias=new ArrayList<>();
	}
	public int getEdad() {
		return edad;
	}
	
	public void setEdad(int edad) {
		this.edad=edad;
	}
	public String getNombre() {
		return nombre;
	}
	public ArrayList<Alergia> getAlergias(){
		return alergias;
	}
	public boolean addAlergia(Alergia al) {
		if(alergias.add(al)) {
			return true;
		}
		if(alergias.add(null)) {
			throw new AlergiasException( "No se puede añadir una alergia sin inicializar");
		}
		
		return false;
	}
	public boolean removeAlergia(Alergia al) {
		if(alergias.remove(al)) {
			return true;
		}
		return false;
	}
	public ArrayList<Alergia> alergiasSeveridad(int umbral){
		ArrayList<Alergia>todasAlergias=new ArrayList<>();
		for(Alergia elemento:alergias) {
			if(elemento.getSeveridad()>=umbral ) {
			 todasAlergias.add(elemento);
			}
			
		}
		return todasAlergias;
	}
	@Override
	public String toString() {
		
		return "--Paciente--"
				+"Nombre: " + nombre +
				
				" Edad: " +  edad +
				
				" Alergias: "+alergias;
					
				}
				
	}
	
	
	


