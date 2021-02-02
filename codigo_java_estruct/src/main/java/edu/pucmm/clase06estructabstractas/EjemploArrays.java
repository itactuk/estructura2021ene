package edu.pucmm.clase06estructabstractas;

public class EjemploArrays {
    public static void main(String[] args) {
        int arr[] = new int[3];
        
        // No es permitido
        // arr.add(1);

        arr[0] = 1;
        arr[1] = 2;
        arr[2] = 3;

        
        // arr[3]

        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(arr[2]);
    }
}
