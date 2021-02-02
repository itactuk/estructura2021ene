package edu.pucmm.clase06estructabstractas;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * https://docs.oracle.com/javase/7/docs/api/java/util/Stack.html
 * https://stackoverflow.com/questions/12524826/why-should-i-use-deque-over-stack
 */
public class EjemploPila {
    public static void main(String[] args) {
        Deque<String> pila = new ArrayDeque<>();
        pila.push("1 de corazones");
        pila.push("2 de trébol");
        pila.push("3 de diamantes");

        pila.pop();

        for(String s: pila){
            System.out.println(s);
        }
    }
}
