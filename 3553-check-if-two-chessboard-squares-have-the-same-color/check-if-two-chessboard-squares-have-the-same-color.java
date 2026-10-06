class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2)
    {
        String even = "aceg";
        char letter1 = coordinate1.charAt(0);
        int number1 = coordinate1.charAt(1) - '0';
        char letter2 = coordinate2.charAt(0);
        int number2 = coordinate2.charAt(1) - '0';
        boolean isOddColumn1 = false;
        boolean isOddColumn2 = false;
        for (int i = 0; i < even.length(); i++)
        {
            if (letter1 == even.charAt(i)) 
            {
                isOddColumn1 = true;
                break;
            }
        }
        for (int i = 0; i < even.length(); i++)
        {
            if (letter2 == even.charAt(i))
            {
                isOddColumn2 = true;
                break;
            }
        }
        boolean isBlack1 = (isOddColumn1 == (number1 % 2 != 0));
        boolean isBlack2 = (isOddColumn2 == (number2 % 2 != 0));
        return isBlack1 == isBlack2;
    }
}