/*Programs to remove all elements from a linked list*/
import java.util.*;
public class linkedlist
{
	public static void main(String args[])
	{
		LinkedList<String> list = new LinkedList<String>();
		Scanner sc = new Scanner(System.in);
		int n,i;
		System.out.println("Enter the limit: ");
		n = sc.nextInt();
		for(i=0;i<n;i++)
		{
			System.out.println("Enter the elements: ");
			list.add(sc.next());
		}
		System.out.println("List: "+list);
		list.clear();
		System.out.println("After removing all elements: "+list);
		
	}
	
	
}