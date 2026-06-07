package Set_5;

import java.util.Scanner;

public class NumberofEvens {
    public static void main(String[] args){
        int arr[] = new int[5];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++){
            System.out.print("Enter the arr[" + i +"]: ");
            arr[i] = sc.nextInt();
        }
        int evens = 0;
        for(int num : arr){
            if(num % 2 == 0){
                evens++;
            }
        }
        System.out.println("The number of even numbers in the given array is " + evens);
        sc.close();
    }
}
