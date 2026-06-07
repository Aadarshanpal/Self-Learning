package Set_6;

import java.util.Scanner;

public class UsingDoubleMethods {
    public static String reverse(String text){
        char[] rev = new char[text.length()];
        for(int i = (text.length()-1); i >= 0 ; i--){
            rev[text.length()-i-1] = text.charAt(i);
        }
        return new String(rev);
    }
    public static boolean isPalindrome(String text){
        String rev_string = reverse(text);
        if(text.equalsIgnoreCase(rev_string)){
            return true;
        }
        else{
            return false;
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string that you want to test palindrome on: ");
        String text = sc.nextLine();
        if(isPalindrome(text)){
            System.out.print("The string given is palindrome.");
        }
        else{
            System.out.print("The string is not palindrome.");
        }
        sc.close();
    }
}
