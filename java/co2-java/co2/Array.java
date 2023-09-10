import java.util.*;
public class Array{
	public static void main(String[] args){
		Scanner bs = new Scanner(System.in);
		int i,flag=0;
		int arr[] = new int[5];
		
		System.out.println("Enter the array element");
		for(i=0;i<arr.length;i++)
		{
			arr[i] = bs.nextInt();
		}
		System.out.println("Array Elent are");
		for(i=0;i<arr.length;i++)
		{
			System.out.println(arr[i]);
		}
		
		System.out.println("Enter the value to searched");
		int Number = bs.nextInt();
		for(i=0;i<arr.length;i++)
		{
			if(arr[i] == Number)
			{
				flag=1;
				System.out.println("Number is found"+" "+(i+1));
			}
			
		}
		if(flag==0){
			System.out.println("Number is not found");
		}
		
		
		
		
	}
}
