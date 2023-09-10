import java.util.*;
class MTable extends Thread
{
	public void run()
	{
		int i,n=5;
		Scanner sc = new Scanner(System.in);
		System.out.println("Multiplication Table of 5 is: ");
		for(i=0;i<10;i++)
		{
			System.out.println(n+"*"+i+"="+n*i);
		}
	}
}

class Prime extends Thread
{
	public void run()
	{
		Scanner sc = new Scanner(System.in);
		int i,j,flag;
		System.out.println("Enter the No. of prime numbers required: ");
		int N = sc.nextInt();
		System.out.println("Prime numbers in the range 1 to "+N);
		for(i=1;i<N;i++)
		{
			flag = 0;
			for(j=1;j<N;j++)
			{
				if(i%j==0)
				{
					flag++;
				}
			}
			if(flag==2)
			{
				System.out.print(i+" ");
			}
		}
	}
}

public class ThreadExt
{
	public static void main(String[] args) throws InterruptedException
	{
		MTable m = new MTable();
		m.start();
		m.sleep(2000);
		Prime p = new Prime();
		p.start();
		p.sleep(1000);
	}
}