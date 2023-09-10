import java.util.*;
class Shape
{
	int r,h,a,p1,p2,t2,t3;
	double b,l,w,t1;
public void area(double r)
{	
double c=3.14*(r*r);
System.out.println("Area of circle: "+c);
}
public void area(double b,int h)
{
	double t=(b*h)/2;
	System.out.println("Area of triangle: "+t);
}
public void area(int a)
{
int s=a*a;
System.out.println("Area of square: "+s);
}
public void area(double l,double w)
{
	double r=l*w;
	System.out.println("Area of rectangle: "+r);
}
public void area(int p1,int p2)
{
	int p=p1*p2;
	System.out.println("Area of parallelogram: "+p);
}
public void area(double t1,int t2,int t3)
{
	double tr=0.5*(t2+t3)*t1;
	System.out.println("Area of trapezium: "+tr);
}
public void area(float e1,float e2)
{	
double c=3.14*(e1*e2);
System.out.println("Area of ellipse: "+c);
}
public static void main(String[] args)
{ int ch;
    Scanner s=new Scanner(System.in);
	Shape sh =new Shape();
	System.out.println("Area of different shapes"+"\n"+" 1.Circle"+"\n"+" 2.Triangle"+"\n"+" 3.Square "+"\n"+" 4.Rectangle "+"\n"+" 5.Parallelogram "+"\n"+" 6.Trapezium"+"\n"+" 7.Ellipse");
	do
	{
	System.out.println("Enter choice: ");
	ch=s.nextInt();
	switch(ch)
	{
		case 1:
		{
	System.out.println("Enter the radius: ");
	double r=s.nextDouble();
	sh.area(r);
		}
		break;
		case 2:
		{
	System.out.println("Enter the breadth: ");
	double b=s.nextDouble();
	System.out.println("Enter the height: ");
	int h=s.nextInt();
	sh.area(b,h);
		}
		break;
		case 3:
		{
	System.out.println("Enter the length: ");
	int a=s.nextInt();
	sh.area(a);
		}
		break;
		case 4:
		{
	System.out.println("Enter the length: ");
	double l=s.nextDouble();
	System.out.println("Enter the breadth: ");
	double w=s.nextDouble();
	sh.area(l,w);
		}
		break;
		case 5:
		{
	System.out.println("Enter the base: ");
	int p1=s.nextInt();
	System.out.println("Enter the vertical height: ");
	int p2=s.nextInt();
	sh.area(p1,p2);
		}
		break;
		case 6:
		{
	System.out.println("Enter the height of trapezium: ");
	double t1=s.nextDouble();
	System.out.println("Enter the length of parallel side: ");
	int t2=s.nextInt();
	System.out.println("Enter the length of parallel side: ");
	int t3=s.nextInt();
	sh.area(t1,t2,t3);
		}
		break;
		case 7:
		{
	System.out.println("Enter the minor axis: ");
	float e1=s.nextFloat();
	System.out.println("Enter the major axis: ");
	float e2=s.nextFloat();
	sh.area(e1,e2);
		}
		break;
		/*default:
		System.out.println("invalid choice");
		break;*/
	}
	}
	while(ch!=7);
}}
