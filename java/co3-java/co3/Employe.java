import java.util.*;
public class Employe{
	int Eno;
	String Ename;
	int Esal;
	public void get(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the employe no:");
		Eno = sc.nextInt();
		System.out.println("Enter the employe Ename:");
		Ename = sc.next();
		System.out.println("Enter the employe Esal:");
		Esal = sc.nextInt();
	}
	
	public void put(){
		System.out.println("The Employe no:"+Eno);
		System.out.println("The Employe no:"+Ename);
		System.out.println("The Employe no:"+Esal);
	}
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("\n Eneter theLimit:");
		int n = sc.nextInt();
		
		Employe Emp[] = new Employe[n];
		System.out.println("Enter the element:");
		for(int i=0;i<n;i++)
		{
			Emp[i]= new Employe();
			Emp[i].get();
		}
		for(int i=0;i<n;i++){
			Emp[i].put();
		}
		System.out.println(" Eneter the no of employee to be searched:");
		int salary = sc.nextInt();
		int flag = 0;
		for(int i=0;i<n;i++)
		{
			if(Emp[i].Esal >=10000 <= 15000 )
			{
				flag = 1;
				Emp[i].put();
				break;
			}
		}
		if(flag==0){
			System.out.println("Employe is not found");
		}
	}
}