class diamond_star {
    public static void main(String[] args) {
        int n=7;
        int i,j;
        int l,r;
        for(i=1,l=4,r=4;i<=n;i++)
        {
            for(j=1;j<=n;j++){
                if (j>=l && j<=r){
                    System.out.print("*");    
                }
                else
                {
                    System.out.print(" ");
                }
            }
            System.out.println();
            if (i<=n/2){
                l-=1;
                r+=1;
            }
            else{
                l++;
                r--;
            }

        }
    }   
}
