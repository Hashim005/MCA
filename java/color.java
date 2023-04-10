import java.util.*;
public class color{
	String name1;
	String name2;
	color(int x, String y)
	{
		name1 = x;
		name2 = y;
		
	}
	public void display(){
		System.out.println("the color1 is"+name1);
		//System.out.println("the color2 is:"+name2);
	}
	System.out.println("the color1 is:"+name1);
	public static void main(String[] args){
		color one = new color("blue","black");
		
		
	}
	name1.display();
	//name2.display();
}