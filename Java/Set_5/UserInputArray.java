package Set_5;
import java.util.Scanner;
public class UserInputArray {
    public static void main(String[] args){
        int arr[] = new int[5];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++){
            System.out.print("Enter the arr[" + i +"]: ");
            arr[i] = sc.nextInt();
        }
        for(int num : arr){
            System.out.print(num + "\t");
        }
        sc.close();
    }
}
