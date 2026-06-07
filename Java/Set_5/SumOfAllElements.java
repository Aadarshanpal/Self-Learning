package Set_5;

import java.util.Scanner;

public class SumOfAllElements {
    public static void main(String[] args){
        int arr[] = new int[5];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++){
            System.out.print("Enter the arr[" + i +"]: ");
            arr[i] = sc.nextInt();
        }
        int sum = 0;
        for(int num : arr){
            sum += num;
        }
        System.out.println("The sum of all elements of the array is: " + sum);
        sc.close();
    }
}
