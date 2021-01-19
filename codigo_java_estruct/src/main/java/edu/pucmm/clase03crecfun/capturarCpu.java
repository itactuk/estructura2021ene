package edu.pucmm.clase03crecfun;

public class capturarCpu {
    public static void main(String[] args) {
        Long timeInicial = System.currentTimeMillis();
        for (int i = 0; i < 100000; i++) {

        }
        Long durationMs = System.currentTimeMillis() - timeInicial;
        System.out.println(durationMs);
    }
}
