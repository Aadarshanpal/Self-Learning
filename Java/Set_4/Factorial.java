package Set_4;
import java.util.Scanner;
public class Factorial {
    public static long factorial(int num){
        long fact = 1;
        for(int i = 1; i <= num; i++){
            fact*=i;
        }
        return fact;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number whose factorial is to be displayed: ");
        int num = sc.nextInt();
        System.out.println("The factorial of " + num + " is " + factorial(num));
        sc.close();
    }
}
