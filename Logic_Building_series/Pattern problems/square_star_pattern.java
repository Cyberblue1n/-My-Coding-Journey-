import java.util.Scanner;
class square_pattern{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int i,j,n;   
        System.out.println("Enter number: ");
        n = sc.nextInt();
        for(i=0;i<=n;i++)
        {
            for (j=0;j<=n;j++)
            {
                System.out.print("* ");
            }
            System.out.println();
        }
        sc.close();
    }
}