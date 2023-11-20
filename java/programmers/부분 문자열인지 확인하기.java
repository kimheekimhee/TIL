class Solution {
    public int solution(String my_string, String target) {
        int answer = 0;
        // System.out.println(target);
        if (my_string.contains(target)) {
            answer += 1;
        }
        return answer;
    }
}