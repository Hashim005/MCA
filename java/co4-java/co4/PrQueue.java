import java.util.*;
public class PrQueue
{
	public static void main(String args[])
	{
		PriorityQueue<Integer> pqueue = new PriorityQueue<Integer>();
		Scanner sc = new Scanner(System.in);
		int n,i;
		System.out.println("Enter the limit: ");
		n = sc.nextInt();
		for(i=0;i<n;i++)
		{
			System.out.println("Enter the Queue elements: ");
			pqueue.add(sc.nextInt());
		}
		System.out.println("Top element: "+ pqueue.peek());
		System.out.println("Deleted element: "+ pqueue.poll());
		System.out.println("Top element: "+ pqueue.peek());
		System.out.println("Queue Elements: "+ pqueue);
	}
}

