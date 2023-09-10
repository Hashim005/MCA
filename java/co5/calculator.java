import java.awt.*;
import java.awt.event.*;
public class calculator extends Frame{
	String number[]={
		"1","2","3","+",
		"4","5","6","-",
		"7","8","9","*",
		"0","=","c","/"
	};
	calculator()
	{
		Button btn[] = new Button[16];
		for(int i=0;i<16;i++)
		{
			btn = new Button(number[i]);
		}
		
		addWindowListener(new WindowAdapter(){
			public void WindowClosing(windowEvent e){
				dispose();
			}
			
		}
		);
		
	}
	public void actionPerformed(ActionEvent e){
		String s=e.getActionCommand();
	}
	public static void main(String[] args){
		new calculator();
	}
}