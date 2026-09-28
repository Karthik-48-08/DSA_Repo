class Solution {
    public int maxDepth(String s) {
        int cnt = 0;
        int maxP = 0;

        for (char ch:s.toCharArray()){
            if (ch=='(') cnt++;
            else if (ch==')') cnt--;

            maxP = Math.max(cnt, maxP);
        }
        return maxP;
    }
}