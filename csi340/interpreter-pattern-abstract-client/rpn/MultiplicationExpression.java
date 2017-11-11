package rpn;

import interpreter.AbstractExpression;
import interpreter.AbstractContext;

class MultiplicationExpression extends AbstractExpression<RPN>
{
    public void interpret(RPN context)
    {
        Double rhs = context.pop();
        Double lhs = context.pop();
        context.push(lhs * rhs);
    }

    public static boolean evaluate(String sym)
    {
        return (sym.equals("*"));
    }
}
