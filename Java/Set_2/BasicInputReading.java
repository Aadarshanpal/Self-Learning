//name age fav prog language
import java.util.Scanner;
public class BasicInputReading {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name: ");
        String name = sc.nextLine();
        System.out.println("Enter your age: ");
        int age = sc.nextInt();
        sc.nextLine();
        System.out.println("What is your fav programming language? ");
        String fav_language = sc.nextLine();
        System.out.println("Name: " + name + "\nAge: " + age + "\nFavorite programming language: " + fav_language);
        sc.close();
    }
}
