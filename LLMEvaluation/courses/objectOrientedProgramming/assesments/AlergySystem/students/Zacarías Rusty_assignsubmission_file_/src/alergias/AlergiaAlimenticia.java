package alergias;

public class AlergiaAlimenticia extends Alergia {
	private TipoAlimento tipo;
	
	public AlergiaAlimenticia(String descripcion,int severidad,TipoAlimento tipo) {
		super(descripcion,severidad);
		this.tipo=tipo;
	}
	public TipoAlimento getTipo() {
		return tipo;
	}
	@Override
	public String toString() {
		return "[Alimenticia, "+tipo+", "+severidad+", "+descripcion+"]";
	}
	

}
