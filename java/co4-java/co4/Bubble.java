import java.util.*;
public class Bubble
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the array size: ");
		int i;
		int j;
		int n = sc.nextInt();
		int arr[] = new int[n];
		System.out.println("Enter the array elements: ");
		for(i=0;i<n;i++)
		{
			arr[i] = sc.nextInt();
		}
		System.out.println("Before sorting");
		for(i=0;i<n;i++)
		{
			System.out.print(arr[i]+" ");
		}
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(arr[i]>arr[j])
				{
					int temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
		System.out.println("\n"+"After sorting: ");
		for(i=0;i<n;i++)
		{
			System.out.print(arr[i]+" ");
		}
	}
}