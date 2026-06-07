package Set_6;
import java.util.Scanner;
public class CountChars {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String str = sc.nextLine();
        System.out.print("Enter the character to count: ");
        String ch = sc.nextLine();
        char c = ch.charAt(0);
        int count = 0;
        for(int i = 0; i<str.length(); i++){
            if(str.charAt(i) == c){
                count++;
            }
        }
        System.out.print("The character appears "+ count +" times");
        sc.close();
    }
}
