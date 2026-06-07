package Set_3;
import java.util.Scanner;
import java.util.Random;
public class GuessingGame {
    public static void main(String[] args){
        Random ran = new Random();
        int num_to_guess = ran.nextInt(100) + 1;
        int choice;
        Scanner sc = new Scanner(System.in);

        System.out.println("A number has been selected from 1-100, Try to guess it.");
        while(true){
            while(true){
                try{
                    System.out.print("Enter your choice: ");
                    choice = sc.nextInt();

                    if(choice > 0 && choice <= 100){
                        break;
                    }
                    else{
                        System.out.println("Enter a valid range of number 0-100.");
                        continue;
                    }
                }
                catch(Exception e){
                    System.out.println("Enter a valid number.");
                    sc.nextLine();
                    continue;
                }
            }
            if(choice < num_to_guess){
                System.out.println("Go Higher!");
            }
            else if(choice > num_to_guess){
                System.out.println("Go Lower!");
            }
            else{
                System.out.println("Congratulations you have found the number!");
                break;
            }
        }
        sc.close();
    }
}
