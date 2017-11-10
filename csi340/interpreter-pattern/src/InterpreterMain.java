public class InterpreterMain
{
    public static void main(String [] args)
    {
        RPNClient client = new RPNClient();
        client.interpret("1 2 +");
        client.interpret("5 3 -");
        client.interpret("11 2 *");
        client.interpret("9 3 /");
        client.interpret("3 3 * 10 +");
    }
}
