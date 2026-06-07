package Set_5;

import java.util.Scanner;

public class Methods {
    public static int sum(int[] arr){
        int sum = 0;
        for(int num : arr){
            sum += num;
        }
        return sum;
    }
    public static int largest(int[] arr){
        int largest = arr[0];
        for(int num : arr){
            if(num > largest){
                largest = num;
            }
        }
        return largest;
    }
    public static void main(String[] args){
        int arr[] = new int[5];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++){
            System.out.print("Enter the arr[" + i +"]: ");
            arr[i] = sc.nextInt();
        }
        System.out.print("The sum is " + sum(arr) + " and the largest element is " + largest(arr));
        sc.close();
    }
}
