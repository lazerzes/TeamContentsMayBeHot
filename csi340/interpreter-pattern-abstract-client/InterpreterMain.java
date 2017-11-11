import java.util.Scanner;
import interpreter.*;
import rpn.*;

public class InterpreterMain
{
    public static void main(String [] args)
    {
        AbstractContext rpn = new RPN();
        InterpreterClient client = new InterpreterClient(rpn);

        // https://stackoverflow.com/a/19532416
        Scanner scanner = new Scanner(System.in);
        String line = "";

        System.out.println("Enter Reverse Polish notation expression, or type \"exit\":");

        while (true)
        {
            line = scanner.nextLine();

            if (line.equals("exit"))
            {
                break;
            }

            client.interpret(line);
        }
    }
}
