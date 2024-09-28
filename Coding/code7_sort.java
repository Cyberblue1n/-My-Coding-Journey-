import java.util.Scanner;
class bubble_sort{
    public void b_sort(int arr[], int n){
        for (int i=0;i<n-1;i++)
        {
            for(int j=0;j<n-i-1;j++)
            {
                if (arr[j]>arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int i;
        System.out.println("Enter the size of the array: ");
        int arr_size = 0;
        if(sc.hasNextInt()){
            arr_size = sc.nextInt();
        }   

        int arr[] = new int[arr_size];
        System.out.println("Enter array elements: ");
        for (i=0;i<arr_size;i++)
        {
            if(sc.hasNextInt())
            {
                arr[i] = sc.nextInt();
            }
        }
        System.out.println("Array elements are: ");
        for(i=0;i<arr_size;i++)
        {
            System.out.print(arr[i]+" ");
        }
        bubble_sort bs = new bubble_sort();
        bs.b_sort(arr, arr_size);
        System.out.println();
        System.out.println("Sorted array");
        for(i=0;i<arr_size;i++)
        {
            System.out.print(arr[i]+" ");
        }
        sc.close();
    }   
}