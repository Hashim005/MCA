import java.util.*;
public class ComplexNum{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the real part of 1st number: ");
		int r1 = sc.nextInt();
		System.out.println("Enter the imaginary part of 1st number:");
		int i1 = sc.nextInt();
		System.out.println("Enter the real part of 2nd number: ");
		int r2 = sc.nextInt();
		System.out.println("Enter the imaginary part of 2nd number:");
		int i2 = sc.nextInt();
		int r3 = r1 + r2;
		int i3 = i1 + i2;
		System.out.println("Complex numbers 1 is : "+ r1 +"+"+i1+"i");
		System.out.println("Complex numbers 2 is : "+ r2 +"+"+i2+"i");
		System.out.println("The sum of the complex numbers is: "+ r3 +"+"+i3+"i");
	}
}