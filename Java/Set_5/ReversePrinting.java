package Set_5;

import java.util.Scanner;

public class ReversePrinting {
    public static void main(String[] args){
        int arr[] = new int[5];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++){
            System.out.print("Enter the arr[" + i +"]: ");
            arr[i] = sc.nextInt();
        }
        for(int i = (arr.length-1); i >= 0; i--){
            System.out.print(arr[i] + "\t");
        }
        sc.close();
    }
}
