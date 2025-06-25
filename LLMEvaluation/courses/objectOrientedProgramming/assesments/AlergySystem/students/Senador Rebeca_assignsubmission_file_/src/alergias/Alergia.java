package alergias;

public class Alergia {
	private static final int minSeveridad = 1;
	private static final int maxSeveridad = 10;
	protected String descripcion;
	protected int severidad;
	
	public Alergia(String d, int s) throws AlergiasException {
		this.descripcion = d;
		this.severidad = s;
		
		if(s<minSeveridad || s>maxSeveridad) {
			throw new AlergiasException("Severidad debe estar en el rango ["+minSeveridad+","+maxSeveridad+"]");
		}
	}
	
	public Alergia(String d) {
		descripcion = d;
		severidad = minSeveridad;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public int getSeveridad() {
		return severidad;
	}

	public void setSeveridad(int severidad) throws AlergiasException {
		this.severidad = severidad;
		if(severidad<minSeveridad || severidad>maxSeveridad) {
			throw new AlergiasException("Severidad debe estar en el rango ["+minSeveridad+","+maxSeveridad+"]");
		}
	}

	public static int getMinseveridad() {
		return minSeveridad;
	}

	public static int getMaxseveridad() {
		return maxSeveridad;
	}
	
}
