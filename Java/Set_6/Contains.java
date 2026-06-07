package Set_6;
import java.util.Scanner;
public class Contains {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the string: ");
        String str = sc.nextLine();

        if(str.contains("Java")){
            System.out.print("The String contains the word \"Java\".");
        }
        else{
            System.out.print("The string does not contain the word \"Java\".");
        }

        sc.close();
    }
}
