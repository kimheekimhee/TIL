class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String upper_myString = myString.toUpperCase();
        String upper_pat = pat.toUpperCase();
        if (upper_myString.contains(upper_pat)) {
            answer = 1;
        }
        return answer;
    }
}