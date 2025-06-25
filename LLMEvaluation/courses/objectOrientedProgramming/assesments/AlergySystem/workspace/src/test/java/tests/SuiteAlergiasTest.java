package tests;

import org.junit.platform.suite.api.SelectClasses;
import org.junit.platform.suite.api.Suite;

import alergias.AlergiaTest;
import personal.PacienteTest;

@Suite
@SelectClasses({
    AlergiaTest.class,
    PacienteTest.class
})
public class SuiteAlergiasTest {
}