//Paula Alcala Fiol, ingenieria de la salud, A, PC 0904

import java.util.ArrayList;
import java.util.List;

import alergias.*;
import personal.Paciente;

public class Principal {

	public static void main(String[] args) {
		//Crea varia alergias 
		AlergiaAlimenticia alergiaLactosaSevera = new AlergiaAlimenticia("Alergia Severa a la lactosa", 8, TipoAlimento.LACTOSA);
		AlergiaAlimenticia alergiaGlutenModerada = new AlergiaAlimenticia("Alergia Moderada al gluten", 5, TipoAlimento.GLUTEN);
		AlergiaAlimenticia alergiaFrutosSecosLeve = new AlergiaAlimenticia("Alergia Leve a los frutos secos", 2, TipoAlimento.FRUTOS_SECOS);
		AlergiaAmbiental alergiaPolenOlivo = new AlergiaAmbiental("Alergia al polen del Olivo", 3, List.of(Estacion.PRIMAVERA));
		AlergiaAmbiental alergiaPolenGraminias = new AlergiaAmbiental("Alergia al polen de las Graminias", 4,
				List.of(Estacion.VERANO));
		AlergiaAmbiental alergiaGatos = new AlergiaAmbiental("Alergia a los gatos", 6,
				List.of(Estacion.PRIMAVERA, Estacion.VERANO, Estacion.OTOÑO, Estacion.INVIERNO));

		//Muestra por pantalla varios tipos de alergias
		System.out.println("Mostramos una alergia Ambiental:");
		System.out.println(alergiaGatos);
		
		
		System.out.println("\nMostramos una alergia Ambiental:");
		System.out.println(alergiaLactosaSevera);
		
		
		
		//Creamos una alergia con una severidad fuera de rango, debería saltar una excepcion
		
		try {
			System.out.println("\nCreamos una alergia fuera de rango de severidad, debería saltar la excepción ");
			AlergiaAlimenticia alergiaFueraRango = new AlergiaAlimenticia("Fuera de rango", 100, TipoAlimento.FRUTOS_SECOS);
		}
		catch(AlergiasException e) {
			System.out.println("Se captura correctamente la excepción, mensaje recibido: " + e.getMessage());
		}
		
		
		System.out.println("\nCreamos un primer paciente con 25 años, Juan Perez");
		
		//Crea dos pacientes y les asigna alergias
		Paciente paciente1 = new Paciente("Juan Perez", 25);
		paciente1.addAlergia(alergiaGatos);
		paciente1.addAlergia(alergiaPolenOlivo);
		paciente1.addAlergia(alergiaFrutosSecosLeve);
		
		System.out.println("\nLe agregamos una alergia  un primer paciente con 25 años, Juan Perez");
		
		
		
		
		System.out.println("\nMostramos un paciente con tres alergias con 25 años, Juan Perez");
		System.out.println(paciente1);

		Paciente paciente2 = new Paciente("Maria Lopez", 30);
		paciente2.addAlergia(alergiaPolenGraminias);
		paciente2.addAlergia(alergiaGlutenModerada);
		paciente2.addAlergia(alergiaLactosaSevera);

		//Crea una lista de pacientes y agrega los pacientes creados
		List<Paciente> pacientes = new ArrayList<>();
		pacientes.add(paciente1);
		pacientes.add(paciente2);

		System.out.println("\nImprime los dos pacientes y sus alergias con severidad mayor o igual a 5:\n");
		for (Paciente paciente : pacientes) {
			System.out.println("Nombre: " + paciente.getNombre());
			System.out.println("Alergias: \n" + paciente.alergiasSeveridad(5));
			System.out.println("\n");
		}

		
	}

}

