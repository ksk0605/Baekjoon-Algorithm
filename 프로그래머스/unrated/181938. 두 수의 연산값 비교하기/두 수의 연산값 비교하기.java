class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int ab = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        int twoab = 2 * a * b;
        return Math.max(ab, twoab);
    }
}