class Solution {
    public int lengthOfLastWord(String s) {
        String str = s.trim();
        int l = str.length();
        int n = 0;
        for(int i=l-1;i>=0;i--)
        {
            if(str.charAt(i)!=' ')
            {
                n++;
            }
            else
                break;
        }
        return n;
    }
}