package Set_7;

public class Rectangle {
    double length;
    double width;
    Rectangle(double length, double width){
        this.length = length;
        this.width = width;

    }
    double area(){
        return length*width;
    }
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(10, 20);
        System.out.println("The area is: " + rect.area());
    }
}