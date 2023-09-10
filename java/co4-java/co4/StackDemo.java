import java.util.*;
import java.util.Stack;
public class stackdemo
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n,i;
		Stack<String> obj = new Stack<String>();
		System.out.println("Enter the limit: ");
		n = sc.nextInt();
		for(i=0;i<n;i++)
		{
			System.out.println("Enter the stack elements: ");
			obj.add(sc.next());
		}
		System.out.println("Stack is: " + obj);
		System.out.println("Enter the position of element to be popped: ");
		int p = sc.nextInt();
		System.out.println("New Stack: "+ obj);
	}
}