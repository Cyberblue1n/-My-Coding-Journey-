class pattern{
    public static void main(String[] args) {
        int l=1;
        int r=7;
        int i,j;
        for (i=1;i<=7;i++)
        {
            for(j=1;j<=7;j++)
            {
                if(l==j || r==j)
                {
                    System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
            l+=1;
            r-=1;
        }
    }
}