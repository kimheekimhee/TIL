package org.Data_Structure.Array;

public class Rearrange_Array {
    public static void fix(int[] A) {
        int len = A.length;

        for (int i = 0; i < len; i++) {
            if (A[i] != -1 && A[i] != i) {
                int x = A[i];

                while (A[x] != -1 && A[x] != x) {
                    int y = A[x];
                    A[x] = x;
                    x = y;
                }

                A[x] = x;

                if (A[i] != i) {
                    A[i] = -1;
                }
            }
        }
    }

    public static void printArray(int[] A) {
        for (int i = 0; i < A.length; i++) {
            System.out.print(A[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] A = { -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 };

        fix(A);
        printArray(A);
    }
}
