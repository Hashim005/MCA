// find the largest number
import java.util.*;
class AddNumbers
{
	int a,b,c;
	public void num(int x,int y)
	{
		a=x;
		b=y;
		
		if(a>b)
		{
			System.out.println("The largest number is a");
			
	
	}
	else
	{
		System.out.println("The largest number is b");
	}
	}
	public void num(int e,int f,int g)
	{
		a=e;
		b=f;
		c=g;
		if(a>b  && a>c)
		{
			System.out.println("The largest no is a");
		}
		else if(b>a && b>c)
		{
			System.out.println("The largest no is b");
		}
		else 
		{
			System.out.println("The largest is c");
		}
	}
	
	public static void main(String [] args)
	{
		Add ob = new Add();
		ob.num(10,20);
		ob.num(10,20,30);
	}
}
		
	