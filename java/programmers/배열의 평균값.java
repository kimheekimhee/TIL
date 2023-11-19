class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        double number_sum = 0;
        for (int i = 0; i<numbers.length; i++) {
            number_sum += numbers[i];
        }
        // System.out.println(number_sum);
        answer = number_sum / numbers.length;
        return answer;
    }
}