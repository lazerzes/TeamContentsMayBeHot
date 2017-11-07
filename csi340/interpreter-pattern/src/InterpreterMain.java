import rpn.*;

public class InterpreterMain
{
    public static void main(String [] args)
    {
        RPNClient client = new RPNClient();
        client.interpret("1 2 +");
    }
}
