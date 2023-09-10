import java.awt.*;
import java.awt.event.*;
import java.applet.*;
public class Keyhandle extends Applet implements KeyListener
{
String msg="Typed";
int x=30,y=50;
public void init()
{
addKeyListener(this);
requestFocus();
}
public void keyTyped(KeyEvent ke)
{
msg+=ke.getKeyChar();
repaint();
}
public void keyReleased(KeyEvent ke)
{
showStatus("Key Up!");
}
public void keyPressed(KeyEvent ke)
{
showStatus("Key Down!");
}
public void paint(Graphics G)
{
G.drawString(msg,x,y);
}
}


//html file
<html>
<body>
<applet code="Keyhandle.class" width="600" height="600">
</applet>
</body>
</html>