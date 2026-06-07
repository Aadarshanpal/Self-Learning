package Set_4;
import java.util.Scanner;
public class Positivity {
    public static boolean isPositive(int num){
        return num > 0;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int num = sc.nextInt();
        if(num == 0){
            System.out.print("The number is neither positive nor negative");
        }
        else if(isPositive(num)){
            System.out.print("The number is positive.");
        }
        else{
            System.out.print("The number is negative.");
        }
        sc.close();
    }
}
