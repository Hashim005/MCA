import java.util.*;
class Stack
{
	int d,n=10,top=-1;
	int st[] = new int[n];
	
	void push()
	{
		if(top==n-1)
		{
			System.out.println("STACK OVERFLOW!!!");
		}
		else
		{
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter a value:");
			d = sc.nextInt();
			top++;
			st[top]=d;
		}
	}
	void pop()
	{
		if(top==-1)
		{
			System.out.println("Stack empty!!!");
		}
		else
		{
			System.out.println("Popped element is: "+st[top]);
			top--;
		}
	}
	void display()
	{
		for(int i=top;i>=0;i--)
		{
			System.out.println(st[i]);
		}
	}
	public static void main(String[] args)
	{
		int ch,n;
		Scanner sc = new Scanner(System.in);
		Stack s = new Stack();
		do
		{
			System.out.println("***Stack operation***");
			System.out.println("1.push 2.pop 3.display 4.exit");
			System.out.println("Enter choice:");
			ch=sc.nextInt();
			switch (ch)
			{
				case 1:
				{
					s.push();
					break;
				}
				case 2:
				{
					s.pop();
					break;
				}
				case 3:
				{
					s.display();
					break;
				}
				default:
				{
					System.out.println("enter valid choice");
				}
			}
		}
		while(ch!=0);
	}
}
