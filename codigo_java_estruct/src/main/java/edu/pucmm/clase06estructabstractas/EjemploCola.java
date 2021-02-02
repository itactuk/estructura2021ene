package edu.pucmm.clase06estructabstractas;

import java.util.Deque;
import java.util.LinkedList;

/**
 * https://docs.oracle.com/javase/7/docs/api/java/util/Queue.html
 */
public class EjemploCola {

    public static void main(String[] args) {
        Deque<String> filaParaPruebaDelCovid =  new LinkedList<>();
        filaParaPruebaDelCovid.add("Enmanuel");
        filaParaPruebaDelCovid.add("Doris");
        filaParaPruebaDelCovid.add("Lorna");
        filaParaPruebaDelCovid.add("Waldry");

        filaParaPruebaDelCovid.pop();

        for(String s: filaParaPruebaDelCovid){
            System.out.println(s);
        }
    }
    
}
