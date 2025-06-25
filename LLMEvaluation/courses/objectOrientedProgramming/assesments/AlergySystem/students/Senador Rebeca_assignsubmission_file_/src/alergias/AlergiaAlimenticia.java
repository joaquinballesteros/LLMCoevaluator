package alergias;

public class AlergiaAlimenticia extends Alergia{
	private TipoAlimento tipo;
	
	public AlergiaAlimenticia(String d, int s, TipoAlimento t) throws AlergiasException {
		super(d,s);
		tipo = t;
	}

	public TipoAlimento getTipo() {
		return tipo;
	}
	
	public String toString() {
		return "[Alimenticia, "+tipo+", "+severidad+", "+descripcion+"]";	
	}
}
