import java.util.Scanner;
public class MarksCalculator {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your marks: ");
        int marks = sc.nextInt();
        sc.close();
        if(marks > 100 || marks < 0){
            System.out.println("Enter a valid marks (0-100)");
            return;
        }
        if(marks > 90){
            System.out.println("A");
        }
        else if(marks > 70){
            System.out.println("B");
        }
        else if (marks > 50){
            System.out.println("C");
        }
        else{
            System.out.println("You have failed.");
        }
    }
}
