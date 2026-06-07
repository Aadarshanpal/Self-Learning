package Set_5;
import java.util.Scanner;
public class SmallestLargest {
    public static void main(String[] args){
        int arr[] = new int[5];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++){
            System.out.print("Enter the arr[" + i +"]: ");
            arr[i] = sc.nextInt();
        }
        int largest = arr[0];
        int smallest = arr[0];
        for(int num : arr){
            if(num > largest){
                largest = num;
            }
            if(num < smallest){
                smallest = num;
            }
        }
        System.out.println("The largest number is " + largest + " and the smallest number is " + smallest);
        sc.close();
    }
}
