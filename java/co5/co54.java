import java.awt.*;
import java.awt.event.*;
import java.applet.*;
public class Maxthree extends Applet implements ActionListener
{
 TextField t1 = new TextField(10);
 TextField t2 = new TextField(10);
 TextField t3 = new TextField(10);
 TextField t4 = new TextField(10);
 Label l1 = new Label("FIRST NUMBER=:");
 Label l2 = new Label("SECOND NUMBER:");
 Label l3 = new Label("THIRD NUMBER:");
 Label l4 = new Label("RESULT IS");
 Button b = new Button("Find MAXIMUM");


 public void init()
 {
 add(l1);
 add(t1);
 add(l2);
 add(t2);
 add(l3);
 add(t3);
 add(l4);
 add(t4);
 add(b);
 b.addActionListener(this);
 }
 public void actionPerformed(ActionEvent e)
 {
 if (e.getSource() == b)
 {
 int num1 = Integer.parseInt(t1.getText());
 int num2 = Integer.parseInt(t2.getText());
 int num3 = Integer.parseInt(t3.getText());
 if (num1 >= num2 && num1 >= num3)
 t4.setText("Result"+num1);
 else if (num2 >= num1 && num2 >= num3)
 t4.setText(""+num2);
 else
 t4.setText("Result"+num3);

 }
 }
}



//html file
<html>
<head>
<title> First Applet </title>
</head>
<body>
<APPLET CODE="Maxthree.class" width="400" height="400">
</applet>
</body>
</html>