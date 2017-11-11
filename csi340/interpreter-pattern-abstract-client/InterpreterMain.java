import java.util.Scanner;
import interpreter.*;
import rpn.*;

public class InterpreterMain
{
    public static void main(String [] args)
    {
        AbstractContext context = new RPN();
        InterpreterClient client = new InterpreterClient(context);

        // https://stackoverflow.com/a/19532416
        Scanner scanner = new Scanner(System.in);
        String line = "";

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
