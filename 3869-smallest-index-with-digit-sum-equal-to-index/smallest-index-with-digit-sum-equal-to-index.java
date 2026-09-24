class Solution {
    public int smallestIndex(int[] nums) {
        for(int i=0;i<nums.length;i++)
        {
            int a=0,b=0;
            int c=nums[i];
            while(c>0)
            {
                a=c%10;
                b+=a;
                c/=10;
            }
            if(b==i) return i;
        }
        return -1;
    }
}