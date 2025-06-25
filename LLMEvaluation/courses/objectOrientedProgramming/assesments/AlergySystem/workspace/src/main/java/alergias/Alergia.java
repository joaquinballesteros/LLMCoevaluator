package alergias;

public abstract class Alergia {
	private final static int  minSeveridad=1;
	private final static int  maxSeveridad=10;
	protected String descripcion;
	protected int severidad;
	
	public Alergia(String descripcion,int severidad) {
		this.descripcion=descripcion;
		this.severidad=severidad;
		if(severidad<=minSeveridad || severidad>=maxSeveridad) {
			throw new AlergiasException("Severidad debe estar en el rango: ["+minSeveridad+","+maxSeveridad+"]");
		}
	}
	public Alergia(String descripcion) {
		this.descripcion=descripcion;
		severidad=minSeveridad;
		
	}
	public String getDescripcion() {
		return descripcion;
	}
	public int getSeveridad() {
		return severidad;
	}
	public void setSeveridad(int severidad) {
		this.severidad = severidad;
		if(severidad<=minSeveridad || severidad>=maxSeveridad) {
			throw new AlergiasException("Severidad debe estar en el rango: ["+minSeveridad+","+maxSeveridad+"]");
	}
	

	}
	
}
