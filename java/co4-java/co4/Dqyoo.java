/*program to demonstrate the addition and deletion of elements in dequeue*/
import java.util.*;
import java.util.Deque;

public class Dqyoo
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		Deque<Integer> deque = new ArrayDeque<>();
		System.out.println("Enter the first element:");
		deque.addFirst(sc.nextInt());
		System.out.println("Enter the second element:");
		deque.addLast(sc.nextInt());
		int f = deque.removeFirst();
		int l = deque.removeLast();
		System.out.println("First: "+ f + ", Last: "+ l);
	}
}
