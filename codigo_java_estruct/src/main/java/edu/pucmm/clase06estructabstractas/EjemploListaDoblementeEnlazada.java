package edu.pucmm.clase06estructabstractas;

import java.util.LinkedList;
import java.util.List;

/**
 * https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html
 */
public class EjemploListaDoblementeEnlazada {
    public static void main(String[] args) {
        List<String> listaDeque = new LinkedList<>();
        listaDeque.add("Nicol");   
        listaDeque.add("Darwin");
        listaDeque.add("Dante");
        for(String s:listaDeque){
            System.out.println(s);
        }
    }
}
