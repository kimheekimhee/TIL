package org.Array;

public class Rotate_Array {

    // 배열을 왼쪽으로 한 칸 회전시키는 메소드
    static void leftRotateByOne(int arr[], int n) {
        int temp = arr[0];
        for (int i = 0; i < n - 1; i++) {
            arr[i] = arr[i + 1];
        }
        arr[n - 1] = temp;
    }

    // 배열을 왼쪽으로 'd'만큼 회전시키는 메소드
    static void leftRotate(int arr[], int d, int n) {
        for (int i = 0; i < d; i++) {
            leftRotateByOne(arr, n);
        }
    }

    // 배열을 출력하는 메소드
    static void printArray(int arr[], int n) {
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    // 메인 메소드
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
        int n = arr.length;

        leftRotate(arr, 2, n);
        printArray(arr, n);
    }

}
