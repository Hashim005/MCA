import java.util.*;
class Fibonacci implements Runnable
{
	public void run()
	{
		int a = 0, b = 1, c;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the limit for Fibonacci series: ");
		int n = sc.nextInt();
		System.out.println("Fibonacci series: ");
		for(int i=0;i<n;i++)
		{
			System.out.println(a+" ");
			c = a + b;
			a = b;
			b = c;
		}
	}
}

class EvenNo implements Runnable
{
	public void run()
	{
		Scanner sc = new Scanner(System.in);
		int lt,ut;
		System.out.println("Enter the lower limit: ");
		lt = sc.nextInt();
		System.out.println("Enter the upper limit: ");
		ut = sc.nextInt();
		for(int i=lt;i<ut;i++)
		{
			if(i%2==0)
			{
				System.out.println(i+" ");
			}
			else
			{
				continue;
			}
		}
	}
}

public class ThreadRunner
{
	public static void main(String[] args) throws InterruptedException
	{
		Fibonacci f = new Fibonacci();
		Thread t1 = new Thread(f);
		t1.start();
		t1.sleep(2000);
		EvenNo e = new EvenNo();
		Thread t2 = new Thread(e);
		t2.start();
		t2.sleep(1000);
	}
}