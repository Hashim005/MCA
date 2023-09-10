import java.util.Arrays;
import java.util.Scanner;
public class StringSorting1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
  System.out.print("Enter the number of strings: ");
        int numStrings = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        String[] strings = new String[numStrings];

        for (int i = 0; i < numStrings; i++) {
            System.out.print("Enter string " + (i + 1) + ": ");
            strings[i] = scanner.nextLine();
        }

        Arrays.sort(strings);
		System.out.println("Sorted strings:");
        for (String str : strings) {
            System.out.println(str);
        }
 scanner.close();
    }
}
