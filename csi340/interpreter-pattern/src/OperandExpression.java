// Concrete terminal expression (external node)

package rpn;

public class OperandExpression extends AbstractExpression
{
    private double operand;

    public OperandExpression(String sym)
    {
        this.operand = Double.parseDouble(sym);
    }

    public OperandExpression(double number)
    {
        this.operand = number;
    }

    public double interpret()
    {
        return this.operand;
    }
}
