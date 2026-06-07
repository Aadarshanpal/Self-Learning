package Set_7;
public class Student {
    String name;
    int age;
    public static void main(String[] args){
        Student s1 = new Student();
        Student s2 = new Student();
        s1.name = "Aadarsha Nepal";
        s1.age = 19;
        s2.name = "Aasana Rai";
        s2.age = 20;
        System.out.println("For student 1:\nName: "+s1.name+"\nAge: "+s1.age);
        System.out.println("For student 2:\nName: "+s2.name+"\nAge: "+s2.age);
    }
}
