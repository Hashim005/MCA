import java.awt.*;
import java.awt.event.*;

public class calculator1 extends Frame implements ActionListener{
	String number[]={
		"1","2","3","+",
		"4","5","6","-",
		"7","8","9","*",
		"0","c","=","/"
	};
	int num1,num2,result;
	TextField text;
	String action;
	
	calculator1(){
		//create and object for pannel
		Panel panel=new Panel();
		panel.setLayout(new GridLayout(4,4));
		Button btn[]=new Button[16];
		text = new TextField();
		add(text,"North");
		for(int i=0;i<16;i++){
			btn[i]= new Button(number[i]);
			btn[i].addActionListener(this);
			panel.add(btn[i]);//adding button //adding button to panel
			
		}
		add(panel);
		addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent e){
				dispose();
			}
		});
		setSize(500,500);
		setVisible(true);
		//setLayout(new GridLayout(4,4));
	}
	public void actionPerformed(ActionEvent e){
		String event=e.getActionCommand(); //collect the string in the button
		if(event.equals("+")|| event.equals("-")||event.equals("*")||event.equals("/")){
			num1=Integer.parseInt(text.getText());
			action=event;
			text.setText("");
		}
		else if(event.equals("c")){
			num1=0;
			num2=0;
			action=null;
			text.setText("");
		}
		else if(event.equals("=")){
			num2=Integer.parseInt(text.getText());
			switch(action){
				case "+":result=num1+num2;
						break;
				case "-":result=num1-num2;
						break;
				case "*":result=num1*num2;
						break;
				case "/":result=num1/num2;
						break;
			}
			text.setText(String.valueOf(result));
		}
		else{
			text.setText(text.getText()+event);
		}
		
	}
	public static void main(String[] args){
		calculator1 obj = new calculator1();
	}
}