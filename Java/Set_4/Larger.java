package Set_4;
import java.util.Scanner;
public class Larger {
    public static int largest(int a, int b){
        if(a>b){
            return a;
        }
        else{
            return b;
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int a  = sc.nextInt();
        System.out.print("Enter the second number: ");
        int b = sc.nextInt();
        System.out.print("The larger number among the two is: " + largest(a,b));
        sc.close();
    }
}
