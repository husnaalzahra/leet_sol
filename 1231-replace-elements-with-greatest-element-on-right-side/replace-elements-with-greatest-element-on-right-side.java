class Solution {
    public int[] replaceElements(int[] arr) {
        int a=-1,b=0;
        for(int i=arr.length-1;i>=0;i--) 
        {
            b=arr[i];
            arr[i]=a;
            a=Math.max(a,b);
        }
        return arr;
    }
}