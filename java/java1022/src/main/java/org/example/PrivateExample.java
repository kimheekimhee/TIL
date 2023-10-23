package org.example;

// 4. private 예제
class PrivateExample {
    private String privateName = "Private Name";

    private void showPrivateName() {
        System.out.println(privateName);
    }

    // 외부에서 privateName에 접근하기 위한 public 메서드
    public void displayPrivateName() {
        showPrivateName();
    }
}