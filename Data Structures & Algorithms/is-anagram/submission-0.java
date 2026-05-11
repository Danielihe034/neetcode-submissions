class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int [] freq = new int [256];
        int [] freqOther = new int [256];
        for (int i = 0; i < s.length(); i++) {
            char curChar = s.charAt(i);
            char otherCur = t.charAt(i);
            freq[curChar]++;
            freqOther[otherCur]++;
        }

        for (int j = 0; j < s.length(); j++) {
            char index = s.charAt(j);
            if (freq[index] != freqOther[index]) {
                return false;
            }
        }
        return true;
    }
}
