package Set_4;
import java.util.Scanner;
public class Square {
    public static long square(int n){
        return n * n;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number whose square is to be calculated: ");
        int num = sc.nextInt();
        System.out.print("The square of " + num + " is " + square(num));
        sc.close();
    }
}
