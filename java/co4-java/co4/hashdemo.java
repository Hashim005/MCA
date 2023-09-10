/*program to demostrate set object using linked hashset class*/
import java.util.*;
public class hashdemo
{
	public static void main(String args[])
	{
		Set<String> s1 = new HashSet<String>();
		Set<String> s2 = new HashSet<String>();
		Scanner sc = new Scanner(System.in);
		int n,i;
		System.out.println("Enter the limit: ");
		n = sc.nextInt();
		System.out.println("Enter the elements of set1: ");
		for(i=0;i<n;i++)
		{
			s1.add(sc.next());
		}
		System.out.println("Enter the elements of set2: ");
		for(i=0;i<n;i++)
		{
			s2.add(sc.next());
		}
		System.out.println("Set1: "+ s1);
		System.out.println("Set2: "+ s2);
		
		//Union operation
		Set<String> union = new HashSet<String>(s1);
		union.addAll(s2);
		System.out.println("Union of the set is :"+union);
		
		//Intersection
		Set<String> inter = new HashSet<String>(s1);
		inter.retainAll(s2);
		System.out.println("Intersection of the set is :"+inter);
		
		//Set difference
		Set<String> difer = new HashSet<String>(s1);
		inter.removeAll(s2);
		System.out.println("Difference of the set is :"+difer);
	}
}