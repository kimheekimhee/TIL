package org.Data_Structure.Array;

public class Reversal_Array {

    // 배열의 일부분을 역전시키는 메소드
    public static void reverseArr(int arr[], int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;
        }
    }

    // 배열을 왼쪽으로 d 만큼 회전시키는 메소드
    public static void rotateLeft(int arr[], int d, int n) {
        reverseArr(arr, 0, d - 1);
        reverseArr(arr, d, n - 1);
        reverseArr(arr, 0, n - 1);
    }

    // 배열을 출력하는 메소드
    public static void printArray(int arr[], int n) {
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    // 메인 메소드
    public static void main(String[] args) {

        int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int n = arr.length;
        int d = 4;

        rotateLeft(arr, d, n);
        printArray(arr, n);
    }
}
