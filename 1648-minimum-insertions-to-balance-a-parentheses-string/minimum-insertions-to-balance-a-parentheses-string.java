class Solution {
    public int minInsertions(String s) {
        int insertions = 0;
        int openCount = 0; // Tracks unmatched '('

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                openCount++;
            } else { // c == ')'
                // Check if the next character is also ')' to form '))'
                if (i + 1 < s.length() && s.charAt(i + 1) == ')') {
                    i++; // Consume the second ')'
                } else {
                    // Single ')' found, we need to insert one ')' to make it '))'
                    insertions++;
                }

                // Match with an existing '(' or insert a missing '('
                if (openCount > 0) 
                {
                    openCount--;
                } 
                else 
                {
                    // No matching '(' available, insert one
                    insertions++;
                }
            }
        }
        // Each remaining unmatched '(' needs two ')'
        insertions += openCount * 2;

        return insertions;
    }
}