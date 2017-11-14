package rpn;

import interpreter.AbstractExpression;
import interpreter.AbstractContext;

public class OperandExpression extends AbstractExpression<RPN>
{
    private Double mValue;

    public OperandExpression(String sym)
    {
        this.mValue = Double.parseDouble(sym);
    }

    public void interpret(RPN context)
    {
        context.push(this.mValue);
    }

    public static boolean evaluate(String sym)
    {
        try
        {
            Double.parseDouble(sym);
        }
        catch(NumberFormatException nfe)
        {
            return false;
        }
        return true;
    }
}
