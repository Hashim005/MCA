import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
public class CO6Q3 {
    public static void main(String[] args) throws IOException {
        FileInputStream fileinput = new FileInputStream("1.txt");
        FileOutputStream fileoutput = new FileOutputStream("2.txt");
        int i;
        while ((i = fileinput.read()) != -1) {
            fileoutput.write(i);
        }
        System.out.println("Successfully copied one file to another");
        fileinput.close();
        fileoutput.close();
    }
}

