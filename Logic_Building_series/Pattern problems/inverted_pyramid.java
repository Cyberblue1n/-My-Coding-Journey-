class inv_pyramid{
    public static void main(String[] args) {
        int l,r;
        int i,j;
        for(i=1, l=1,r=7;i<=4;i++,l++,r--){
            for(j=1;j<=7;j++)
            {
                if (j>=l && j<=r){
                    System.out.print("*");
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}