import java.util.*;
public class StringSorting{
	public static void main (String[] args){
		Scanner sr = new Scanner(System.in);
		String arr[] = new String[10];
		int i,j;
		String temp,n;
		System.out.println("Enetr the array element:");
		n = sr.next();
		for(i=0;i<n;i++){
			arr[i] = sr.nextLine();
		}
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(arr[i].compareTo(arr[j])>0)
				{
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
	}
}