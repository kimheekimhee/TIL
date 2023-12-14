package org.array;

public class gcd {

    // 최대공약수 구하는 함수
    public static int gcd(int a, int b) {
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }

    public static void main(String[] args) {
        System.out.println(gcd(24, 38));
        System.out.println(gcd(24, 36));
        System.out.println(gcd(24, 32));
        System.out.println(gcd(14, 35));
    }
}
