class selection_Sort{
    public static void main(String args[]){
        int arr[] = {4, 8, 5, 2, 1};
        selectsort(arr);
        for (int i: arr){
            System.out.print(" "+i);
        }
    }
    private static void selectsort(int arr[]){
        int n = arr.length;
        int i,j;
        for (i=0;i<n;i++)
        {
            int min = i;
            for (j=i+1;j<n;j++)
            {
                if(arr[min]>arr[j]){
                    min = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
}