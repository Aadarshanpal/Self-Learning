package Set_6;
import java.util.Scanner;
public class Counting {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char[] vowels = {'a','e','i','o','u'};

        System.out.print("Enter your string: ");
        String str = sc.nextLine();
        String stri = str.toLowerCase();
        int v = 0;
        for(int i = 0; i < str.length(); i++){
            for(char vowel : vowels){
                if(vowel == stri.charAt(i)){
                    v++;
                }
            }
        }
        System.out.println("The string " + str + " has " + v + " vowels and " + (str.length() - v) + " consonants ");
        sc.close();
    }
}
