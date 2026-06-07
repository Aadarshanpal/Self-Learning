package Set_3;
import java.util.Scanner;
public class FactorialCalculator {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number whose factorial is to be calculated: ");
        int num = sc.nextInt();
        long fact = 1;
        for(int i = 1 ; i <= num; i++){
            fact = fact * i;
        }
        System.out.print("The factorial of " + num + " is " + fact);
        sc.close();
    }
}
