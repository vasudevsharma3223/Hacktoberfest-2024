import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Create a Scanner object to read input
        Scanner scanner = new Scanner(System.in);

        // Ask for the user's name
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        // Display a greeting message
        System.out.println("Hello, " + name + "! Welcome to the Java program.");

        // Ask for the user's age
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        // Display a message based on the age
        if (age < 18) {
            System.out.println("You are a minor.");
        } else {
            System.out.println("You are an adult.");
        }

        // Close the scanner
        scanner.close();
    }
}
