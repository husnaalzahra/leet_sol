class Solution {
    public boolean hasAllCodes(String s, int k)
    {
        int need = 1 << k;
        Set<String> got = new HashSet<>();
        for (int i = 0; i <= s.length() - k; i++)
        {
            String sub = s.substring(i, i + k);
            got.add(sub);
            if (got.size() == need)
            {
                return true;
            }
        }
        return got.size() == need;
    }
}