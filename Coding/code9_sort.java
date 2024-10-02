class insertion_Sort{
    public static void main(String[] args) {
        int arr[] = {4, 8, 5, 2, 1};
        sort(arr);
        for (int i:arr){
            System.out.print(" "+i);
        }
    }
    private static void sort(int arr[]){
        int i,j;
        int key;
        for(i=0;i<arr.length;i++)
        {
            key=arr[i];
            j = i-1;
            while (j>=0 && arr[j]>key) {
                arr[j+1]=arr[j];
                j=j-1;
                arr[j+1]=key;
            }
        }

    }
}