package Set_4;
import java.util.Scanner;
public class LoginSimulator {
    String stored_username;
    String stored_password;
    LoginSimulator(){
        stored_password = "123456789";
        stored_username = "Aadarsha Nepal";
    }
    public boolean login(String username, String password){
        if(username.equals(stored_username) && password.equals(stored_password)){
            return true;
        }
        else{
            return false;
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your username: ");
        String username = sc.nextLine();
        System.out.print("Enter the password: ");
        String password = sc.nextLine();
        
        LoginSimulator ls = new LoginSimulator();
        if(ls.login(username,password)){
            System.out.print("Login Success!");
        }
        else{
            System.out.print("Login failed!");
        }
        sc.close();
    }
}
