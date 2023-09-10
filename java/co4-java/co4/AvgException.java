import java.util.*;

class NegativeNumberException extends Exception {
    public NegativeNumberException(String message) {
        super(message);
    }
}

class AvgException {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of integers: ");
        int n = scanner.nextInt();

        int sum = 0;
        int count = 0;

        for (int i = 0; i < n; i++) {
            try {
                System.out.print("Enter a positive integer: ");
                int num = scanner.nextInt();

                if (num < 0) {
                    throw new NegativeNumberException("Negative numbers are not allowed");
                }

                sum += num;
                count++;
            } catch (NegativeNumberException e) {
                System.out.println(e.getMessage());
            }
        }

        if (count == 0) {
            System.out.println("No positive numbers were entered");
        } else {
            double average = (double) sum / count;
            System.out.println("The average of the " + count + " positive numbers is " + average);
        }
    }
}
