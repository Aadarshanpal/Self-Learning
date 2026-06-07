package Set_3;
import java.util.Scanner;
public class Multiplication {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number whose multiplication is required: ");
        int num = sc.nextInt();
        for(int i = 1; i <= 10; i++){
            System.out.println(num + " x " + i + " = " + (num*i));
        }
        sc.close();
    }
}
