// Concrete nonterminal expression (internal node)

package rpn;

public class OperatorExpression extends AbstractExpression
{
    private char operator;

    public OperatorExpression(String sym)
    {
        this.operator = sym.charAt(0);
    }

    public double interpret()
    {
        double result = Double.POSITIVE_INFINITY;
        switch (operator)
        {
            case '+':
                result = lhs.interpret() + rhs.interpret();
                break;
            case '-':
                result = lhs.interpret() - rhs.interpret();
                break;
            case '*':
                result = lhs.interpret() * rhs.interpret();
                break;
            case '/':
                result = lhs.interpret() / rhs.interpret();
                break;
        }
        return result;
    }
}
