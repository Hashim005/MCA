import java.applet.*;
import java.awt.*;
import java.awt.Graphics;
import java.awt.event.*;
public class Shapechoose extends Applet implements ItemListener
{
Choice figure = new Choice();
int Select;
public void init()
{
figure.addItem("Select your choice");
figure.addItem("Rectangle");
figure.addItem("Square");
figure.addItem("Circle");
figure.addItem("Triangle");
add(figure);
figure.addItemListener(this);
}
public void itemStateChanged (ItemEvent e)
{
Select = figure.getSelectedIndex();
repaint();
}
public void paint(Graphics g)
{
g.setColor(Color.red);
super.paint(g);
if (Select == 1)
{
g.drawRect(280, 100, 160,40);
}
if (Select == 2)
{
g.drawRect(50,50,100,100);
}
if (Select == 3)
{
g.drawOval(150,150,100,100);
}
if (Select ==4)
{
g.drawLine(120, 130, 280, 130);
g.drawLine(120, 130, 200, 65);
g.drawLine(200, 65, 280, 130);
}
}
}


//html file
<html>
<body>
<applet code="Shapechoose.class" width="600" height="600">
</applet>
</body>
</html>