class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        for(int i = 0; i < numbers.length; i++) {
            // System.out.println(i);
            int mulNumber = numbers[i]*2;
            // System.out.println(mulNumber);
            answer[i] = mulNumber;            
        }
        return answer;
    }
}