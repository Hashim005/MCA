import java.util.*;
 public class Employee
{
	int eno;
	String ename;
	int esalary;
	
	public void get(){
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the employee number:");
		eno=sc.nextInt();
		System.out.println("Enter the employee name:");
		ename=sc.next();
		System.out.println("Emter the salary of the employee:");
		esalary=sc.nextInt();
	}
	public void put()
	{
		System.out.println("The employee details:");

		System.out.println(eno);
		System.out.println(ename);
		System.out.println(esalary);
	}
	public static void main(String args[]){
		int i,val;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the number of employees:");
		int n=sc.nextInt();
		Employee e[]=new Employee[n];
		for(i=0;i<n;i++)
		{
			e[i]=new Employee();
			e[i].get();
		}
		for(i=0;i<n;i++){
			e[i].put();
		}
		System.out.println("Enter the employee number to search for an employee:");
		val=sc.nextInt();
		for(i=0;i<n;i++)
		{
			if(e[i].eno==val){
				e[i].put();
			}
		}
	}}
