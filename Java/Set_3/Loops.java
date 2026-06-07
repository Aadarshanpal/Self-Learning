package Set_3;
import java.util.Scanner;
public class Loops {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter \"While\" for using while loop and \"For\" for using the for loop: ");
        String choice = sc.nextLine();
        int i = 0;
        if(choice.equals("While")){
            while(i < 100){
                System.out.print((i+1) + "\t");
                i++;
            }
        }
        else if(choice.equals("For")){
            for(i = 0; i < 100; i++){
                System.out.print((i+1) + "\t");
            }
        }
        else{
            System.out.println("Enter a valid choice.");
        }
        sc.close();
    }
}
