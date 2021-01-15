package edu.pucmm.clase02introjava;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class FuerzaTest {

    @Test
    public void testCalcularFueza()
    {
        assertEquals(12.0, new Fuerza().calcular_fuerza(3, 4), 3);
    }

}