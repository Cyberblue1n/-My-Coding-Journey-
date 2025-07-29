class hollow_square {
    public static void main(String[] args) {
        int n = 4;
        int i,j;
        for(i=1;i<=4;i++){
            for (j=1;j<=4;j++){
                if(i==1 || i==n || j==1 ||j==n){
                    System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
