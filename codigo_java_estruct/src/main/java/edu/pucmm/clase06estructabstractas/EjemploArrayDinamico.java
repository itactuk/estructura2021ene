package edu.pucmm.clase06estructabstractas;

import java.util.ArrayList;
import java.util.List;

public class EjemploArrayDinamico {
    private static final int INCR = 10;
    int arr[] = new int[INCR];
    int i = 0;
    int n = INCR;

    public void add(int x){
        if(i<=n){
            realloc();
        }
        arr[i++] = x;
    }

    public int get(int i){
        return this.arr[i];
    }

    private void realloc(){
        int arrTmp[] = this.arr;
        n += INCR;
        this.arr = new int[n];
        for(int i=0; i< arrTmp.length; i++){
            this.arr[i] = arrTmp[i];
        }
    }

    public static void main(String[] args) {
        List<Integer> valores = new ArrayList<>();

        valores.add(1);
        valores.add(2);
        valores.add(3);

        for (Integer i: valores){
            System.out.println(i);
        }
    }
}
