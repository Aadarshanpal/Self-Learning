import java.util.Scanner;
public class LoginSimulator {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String stored_username = "Aadarsha Nepal";
        String stored_password = "123456789";
        System.out.print("Enter the username:");
        String username = sc.nextLine();
        System.out.print("Enter the password:");
        String password = sc.nextLine();
        if(username.equals(stored_username) && password.equals(stored_password)){
            System.out.println("Login Sucessful!");
        }
        else{
            System.out.println("Login failed... Incorrect Username or Password");
        }
        sc.close();
    }
}
