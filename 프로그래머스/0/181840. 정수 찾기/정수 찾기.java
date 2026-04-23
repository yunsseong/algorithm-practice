class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        for (int i = 0; i < num_list.length; i++) {
            if (n == num_list[i]) {
                return answer + 1;
            }
        }
        return answer;
    }
}