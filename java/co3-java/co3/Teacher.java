// employees and teacher single inheritence
class Employee{
	int Empid;
	String Name;
	int Salary;
	String Address;
	
	Employee(int w,String x,int y, String z){
		Empid = w;
		Name = x;
		Salary = y;
		Address = z;
		
	}
	void display(){
		System.out.println("The Employee is Empid:"+w);
		System.out.println("The Employee is Name:"+x);
		System.out.println("The Employee is Salary:"+y);
		System.out.println("The Employee is Address:"+z);
	}
}
public  class Teacher extends Employee{
	int depart;
	String sub;
void get(){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the the department name:"+depart);
	depart =sc.next();
	System.out.println("Enter the teacher subject is :"+depart);
	sub = sc.next();
}
	Teacher(String Tdep, String Tsub){
		super(Empid,Name,Salary,Address)
		depart = Tdep;
		sub = Tsub;
	}
	void display(){
		System.out.println("The Teacher Department:"+depart);
		System.out.println("The Teacher subject is:"+sub);
	}
	
}
public class inherits(){
	
}