package Arithmetic;

import java.util.Scanner;

public class basic implements Operation
{
	int a,b;
	Scanner cin = new Scanner(System.in);
	public void get()
	{
		System.out.println("Enter 1st number");
        a = cin.nextInt();
        System.out.println("Enter 2nd number");
        b = cin.nextInt();
	}
	public void add()
	{
		int sum = a+b;
		System.out.println("Sum is :"+sum);
	}
	public void sub()
	{
		int d = a-b;
		System.out.println("Differnce is :"+d);
	}
	public void multi()
	{
		int p = a*b;
		System.out.println("Product is :"+p);
	}
	public void div()
	{
		int divv = a/b;
		System.out.println("Quotient is :"+divv);
	}
	public static void main(String[] args)
	{
		basic obj = new basic();
		obj.get();
		obj.add();
		obj.sub();
		obj.multi();
		obj.div();
	}
}
