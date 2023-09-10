import java.util.*;
public class Product{
	int pcode;
	String pname;
	int price;
	public void get(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the pcode:");
		pcode =sc.nextInt();
		System.out.println("Enter the pname:");
		pname =sc.next();
		System.out.println("Enter the price:");
		price =sc.nextInt();
	}
	public void master(){
		System.out.println("poduct code :"+pcode);
		System.out.println("poduct pname :"+pname);
		System.out.println("poduct price :"+price);
	}
	public static void main(String[] args){
		
		Product p1 = new Product();
		Product p2 = new Product();
		Product p3 = new Product();
		System.out.println("poduct details1:");
		p1.get();
		System.out.println("poduct details2:");
		p2.get();
		System.out.println("poduct details3:");
		p3.get();
		
		System.out.println("poduct details1 first:");
		p1.master();
		System.out.println("poduct details1 second:");
		p2.master();
		System.out.println("poduct details1 third:");
		p3.master();
	}
}