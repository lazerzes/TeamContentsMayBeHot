package interpreter;

// https://stackoverflow.com/a/35684352
// https://stackoverflow.com/a/39903187
public abstract class AbstractExpression<T extends AbstractContext>
{
    public abstract void interpret(T context);
    public static boolean evaluate(String sym)
    {
        // This function should never be called
        return false;
    }
}
