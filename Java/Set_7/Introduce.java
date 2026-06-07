package Set_7;

public class Introduce {
    public void introduce(String name, int age){
        System.out.println("My name is " + name + " and I am " + age + " years old");
    }
    public static void main(String[] args){
        Introduce in = new Introduce();
        in.introduce("Aadarsha Nepal", 19);
    }
}
