package rpn;

import interpreter.AbstractExpression;
import interpreter.AbstractContext;

public class OperatorExpression extends AbstractExpression<RPN>
{
    private char mOperator;
    private static String[] OPERATORS = {"+", "-", "*", "/"};

    public OperatorExpression(String sym)
    {
        this.mOperator = sym.indexOf(0);
    }

    public void interpret(RPN context)
    {
        Double rhs = context.pop();
        Double lhs = context.pop();
        Double result = Double.POSITIVE_INFINITY;

        switch (this.mOperator)
        {
            case '+':
                result = rhs + lhs;
                break;
            case '-':
                result = rhs - lhs;
                break;
            case '*':
                result = rhs * lhs;
                break;
            case '/':
                result = rhs / lhs;
        }
        context.push(result);
    }

    public static boolean evaluate(String sym)
    {
        return (OperatorExpression.OPERATORS.contains(sym));
    }
}
