parsimport java.applet.*;
import java.awt.*;
public class Co51 extends Applet
{
public void paint(Graphics g)
{
g.drawLine(20,20,200,20);
g.drawRect(20,100,200,40);
g.drawOval(20,120,200,160);
}
}

//html file
<html>
<head>
</head>
<title> APPLET </title>
<body>
<applet code="Co51.class" height="300" width="300"> </applet>
</body>
</html>
