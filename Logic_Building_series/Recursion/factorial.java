import java.util.Scanner;
class factorial{
    public static int fact(int n){
        if(n==1){
            return n;
        }
        else {
            return n*fact(n-1);
        }
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int a = sc.nextInt();
        System.out.println("Factorial of the number "+a+" is: "+fact(a));
        sc.close();
    }
}