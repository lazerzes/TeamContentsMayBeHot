import java.util.Stack;
import java.util.*;

public class RPNClient
{
    private ArrayList<String> OPERATORS = new ArrayList<String>(Arrays.asList("+", "-", "*", "/"));

    public void interpret(String expression)
    {
        Stack<AbstractExpression> stack = new Stack<AbstractExpression>();
        String[] symbols = expression.split(" ");

        System.out.println(expression);

        for (String sym : symbols)
        {
            if (this.isOperator(sym))
            {
                AbstractExpression rhs = stack.pop();
                AbstractExpression lhs = stack.pop();
                AbstractExpression operator = new OperatorExpression(sym, lhs, rhs);
                Double result = operator.interpret();
                AbstractExpression operand = new OperandExpression(result);
            }
            else if (this.isOperand(sym))
            {
                AbstractExpression operand = new OperandExpression(sym);
                stack.push(operand);
            }
        }
        System.out.println(stack.pop().interpret());
    }

    private boolean isOperator(String sym)
    {
        boolean result = true;

        if (sym.length() != 1 || !OPERATORS.contains(sym.charAt(0)))
        {
            result = false;
        }

        return result;
    }

    private boolean isOperand(String sym)
    {
        boolean result = true;

        try
        {
            Double.parseDouble(sym);
        }
        catch (NumberFormatException exception)
        {
            result = false;
        }

        return result;
    }
}
