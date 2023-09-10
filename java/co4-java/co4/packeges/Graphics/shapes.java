//shapes.java
package Graphics;
import java.util.*;

public class shapes implements Area
{
	double lr,lb,ra,th,tb,ta,sa,s,cr,cc;
	public void getRect()
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the length of the rectangle: ");
		lr = sc.nextInt();
		System.out.println("Enter the breadth of the rectangle: ");
		lb = sc.nextInt();
	}
	public void Rectangle()
	{
		ra = lr*lb;
		System.out.println("Area of Rectangle is "+ra);
	}
	public void getTri()
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the height of the Triangle: ");
		th = sc.nextInt();
		System.out.println("Enter the base of the Triangle: ");
		tb = sc.nextInt();
	}
	public void Triangle()
	{
		ta = 0.5*th*tb;
		System.out.println("Area of Triangle angle is "+ta);
	}
	public void getSqr()
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Side of the Square: ");
		s = sc.nextInt();
	}
	public void Square()
	{
		sa = s*s;
		System.out.println("Area of Square is: "+sa);
	}

	public void getCrl()
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the radius of the Circle: ");
		cc = sc.nextInt();
	}
	public void Circle()
	{
		cr = 3.14*cc*cc;
		System.out.println("Area of Square is: "+cr);

	}
	public static void main(String[] args)
	{
		shapes o= new shapes();
		o.getRect();
		o.Rectangle();
		o.getTri();
		o.Triangle();
		o.getSqr();
		o.Square();
		o.getCrl();
		o.Circle();
	}
}