package org.example;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        System.out.println("public class Main, public static void main");

        // Public 클래스 사용 예제
        PublicExample pubExample = new PublicExample();
        pubExample.showPublicName();

        // Protected 클래스 사용 예제
        ProtectedExample protExample = new ProtectedExample();
        protExample.showProtectedName();

        // Default 클래스 사용 예제
        DefaultExample defExample = new DefaultExample();
        defExample.showDefaultName();

        // Private 클래스 사용 예제
        PrivateExample privExample = new PrivateExample();
        privExample.displayPrivateName();
    }
}