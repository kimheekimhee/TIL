package org.array;

public class maxvalue_array {

    // 배열에서 회전을 해서 i*arr[i]의 합이 최대가 될 때의 값을 계산하는 메소드
    public static int maxVal(int arr[], int n) {
        int arrSum = 0; // arr[i]의 전체 합
        int curSum = 0; // i*arr[i]의 전체 합

        for (int i = 0; i < n; i++) {
            arrSum += arr[i];
            curSum += (i * arr[i]);
        }

        int maxSum = curSum;

        for (int j = 1; j < n; j++) {
            curSum = curSum + arrSum - n * arr[n - j];

            if (curSum > maxSum)
                maxSum = curSum;
        }

        return maxSum;
    }

    public static void main(String[] args) {
        int arr[] = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int n = arr.length; // 배열의 길이를 직접 계산
        System.out.println(maxVal(arr, n)); // 결과 출력
    }
}
