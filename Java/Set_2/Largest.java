import java.util.Scanner;
public class Largest {
    public static void main(String[] args){
        int a, b, c;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first the number");
        a = sc.nextInt();
        System.out.println("Enter second the number");
        b = sc.nextInt();
        System.out.println("Enter third the number");
        c = sc.nextInt();
        if(a>b){
            if(a>c){
                System.out.println(a + " is the largest number.");
            }
            else
            {
                System.out.println(c + " is the largest number.");
            }
        }
        else{
            if(b>c){
                System.out.println(b + " is the largest number.");
            }
            else{
                System.out.println(c + " is the largest number.");
            }
        }
        sc.close();
    }
}
