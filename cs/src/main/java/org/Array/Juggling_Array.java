package org.Array;

public class Juggling_Array {

    // 최대공약수 구하는 함수
    public static int gcd(int a, int b) {
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }

    // 배열을 왼쪽으로 d번 회전시키는 함수
    public static void leftRotate(int arr[], int d, int n) {
        for (int i = 0; i < gcd(d, n); i++) {
            int temp = arr[i];
            int j = i;

            while (true) {
                int k = j + d;
                if (k >= n)
                    k = k - n;

                if (k == i)
                    break;

                arr[j] = arr[k];
                j = k;
            }
            arr[j] = temp;
        }
    }

    // 배열 출력 함수
    public static void printArray(int arr[], int size) {
        for (int i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // 테스트를 위한 메인 메서드
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
        int n = arr.length;

        // 배열 회전 함수 호출
        leftRotate(arr, 2, n);
        printArray(arr, n);
    }
}
