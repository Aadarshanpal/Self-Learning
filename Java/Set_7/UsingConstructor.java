package Set_7;

public class UsingConstructor {
    String name;
    int age;
    UsingConstructor(String name, int age){
        this.name = name;
        this.age = age;
        System.out.println("My name is " + this.name + " and I am " + this.age + " years old");
    }
    public static void main(String[] args){
        new UsingConstructor("Aadarsha Nepal", 19);
    }
}
