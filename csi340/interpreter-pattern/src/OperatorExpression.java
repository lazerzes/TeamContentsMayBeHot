// Concrete nonterminal expression (internal node)

public class OperatorExpression extends AbstractExpression
{
    private char operator;
    private AbstractExpression lhs;
    private AbstractExpression rhs;

    public OperatorExpression(String sym, AbstractExpression lhs, AbstractExpression rhs)
    {
        this.operator = sym.charAt(0);
        this.lhs = lhs;
        this.rhs = rhs;
    }

    public double interpret()
    {
        double result = Double.POSITIVE_INFINITY;
        switch (operator)
        {
            case '+':
                result = this.lhs.interpret() + this.rhs.interpret();
                break;
            case '-':
                result = this.lhs.interpret() - this.rhs.interpret();
                break;
            case '*':
                result = this.lhs.interpret() * this.rhs.interpret();
                break;
            case '/':
                result = this.lhs.interpret() / this.rhs.interpret();
                break;
        }
        return result;
    }
}
