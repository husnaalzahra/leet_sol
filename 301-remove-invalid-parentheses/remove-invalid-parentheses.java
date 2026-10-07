import java.util.*;

class Solution {
    public List<String> removeInvalidParentheses(String s) {
        Set<String> result = new HashSet<>();

        int left = 0;
        int right = 0;

        // Find extra parentheses that need to be removed
        for (char c : s.toCharArray()) {
            if (c == '(') {
                left++;
            } else if (c == ')') {
                if (left > 0) {
                    left--;
                } else {
                    right++;
                }
            }
        }

        backtrack(s, 0, left, right, new StringBuilder(), result);

        return new ArrayList<>(result);
    }

    private void backtrack(String s, int index, int left, int right,
                            StringBuilder current, Set<String> result) {

        if (index == s.length()) {
            if (left == 0 && right == 0 && isValid(current)) {
                result.add(current.toString());
            }
            return;
        }

        char c = s.charAt(index);

        // Remove current character
        if (c == '(' && left > 0) {
            backtrack(s, index + 1, left - 1, right, current, result);
        }

        if (c == ')' && right > 0) {
            backtrack(s, index + 1, left, right - 1, current, result);
        }

        // Keep current character
        current.append(c);
        backtrack(s, index + 1, left, right, current, result);
        current.deleteCharAt(current.length() - 1);
    }

    private boolean isValid(StringBuilder s) {
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                count++;
            } else if (c == ')') {
                count--;

                if (count < 0) {
                    return false;
                }
            }
        }

        return count == 0;
    }
}
