import java.util.Scanner;
class Cpu{
	int price;
	class Processor{
		int no_core;
		String manu;
		void getdata(){
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter the No. of cores: ");
			no_core = sc.nextInt();
			System.out.println("Enter the Manufacturer of processor: ");
			manu = sc.next();
		}	
		void showdata()
		{
			System.out.println("Core count: "+no_core);
			System.out.println("Manufacturer: "+manu);
		}
	}
	static class Ram{
		int mem;
		String manuf;
		void getdata(){
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter the Memory size of the RAM: ");
			mem = sc.nextInt();
			System.out.println("Enter the Manufacturer of RAM: ");
			manuf = sc.next();
		}
		void showdata()
		{
			System.out.println("RAM memory: "+mem);
			System.out.println("RAM manufacturer: "+manuf);
		}
	}
	void getdata(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the price of the CPU: ");
		price = sc.nextInt();
	}
	void showdata()
	{
		System.out.println("Price: "+price);
	}
}
public class Computer{
	public static void main(String[] args){
		Cpu c = new Cpu();
		Cpu.Processor  p = c.new Processor();
		Cpu.Ram r = new Cpu.Ram();
		c.getdata();
		p.getdata();
		r.getdata();
		c.showdata();
		p.showdata();
		r.showdata();
	}
}