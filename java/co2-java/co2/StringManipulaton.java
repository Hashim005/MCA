import java.util.*;
public class StringManipulaton{
	public static void main(String[] args){
		Scanner sg = new Scanner(System.in);
		System.out.println("Enter the String1:");
		String s1 = sg.nextLine();
		System.out.println("Enter the String2:");
		String s2 = sg.nextLine();
		System.out.println("The String concat is"+s1.concat(s2));
		System.out.println("The String length is"+s1.length());
		System.out.println("The String length is"+s2.length());
		if(s1.length()==s2.length())
		{
			System.out.println("String are same");
			
		}
		else
		{
			System.out.println("String are not same");
		}
		System.out.println("String are same:"+s1.equals(s2));
		System.out.println("String compare Uppercase:"+s1.toUpperCase());
		System.out.println("String compare Lowercase:"+s1.toLowerCase());
		System.out.println("The substring of s1"+s1.substring(3));
	}
}