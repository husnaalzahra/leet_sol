class Solution {
    public List<String> simplifiedFractions(int n) {
        List<String> list= new ArrayList<>();
        for(int d=2;d<=n;d++) 
        {
            for(int nu=1;nu<d;nu++) 
            {
                boolean haha= true;
                for(int f=2;f<=nu;f++) 
                {
                    if(nu%f==0 && d%f==0) 
                    {
                        haha=false;
                        break;
                    }
                }
                if(haha) list.add(nu+"/"+ d);
            }
        }
        return list;
    }
}