import java.util.Scanner;
public class accountbal{
	int acno;
	String name;
	int bal;
	public void getdata(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Account No: ");
		acno = sc.nextInt();
		System.out.println("Enter the Name: ");
		name = sc.next();
		System.out.println("Enter the Balance: ");
		bal = sc.nextInt();
	}
	
	public void showdata()
	{
		System.out.println("Account No: "+acno);
		System.out.println("Name : "+name);
		System.out.println("Balance: "+bal);
	}
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the no users : ");
		int n = sc.nextInt();
		account a[] = new account[n];
		for(int i=0;i<n;i++)
		{
			a[i] =  new account();
			a[i].getdata();
		}
		System.out.println("Accounts without minimum balance ");
		for(int i=0;i<n;i++)
		{
			if(a[i].bal<500)
			{
				a[i].showdata();
			}
		}
	}
	
}