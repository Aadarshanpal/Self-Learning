package Set_6;
import java.util.Scanner;
public class Reverse {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string that needs to be reversed: ");
        String str = sc.nextLine();
        char rev[] = new char[str.length()];
        for(int i = (str.length()-1); i >= 0; i--){
            rev[str.length()-1-i] = str.charAt(i);
        }
        String reversedstr = new String(rev);
        System.out.print("The reverse String is: "+reversedstr);
        sc.close();
    }
}
