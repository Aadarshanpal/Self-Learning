package Set_6;
import java.util.Scanner;
public class Strings {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your string: ");
        String str = sc.nextLine();
        System.out.print("The string's length is " + str.length() + " its first letter is " + str.charAt(0) + " and the last letter is " + str.charAt((str.length() - 1)));
        sc.close();
    }
}
