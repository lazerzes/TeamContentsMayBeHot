import java.util.Stack;
import java.util.*;

public class RPNClient
{
    private ArrayList<String> OPERATORS = new ArrayList<String>(Arrays.asList("+", "-", "*", "/"));

    public void interpret(String expression)
    {
        Stack<AbstractExpression> stack = new Stack<AbstractExpression>();
        String[] symbols = expression.split(" ");

        System.out.println("Interpreting expression: " + expression);

        for (String sym : symbols)
        {
            System.out.println("Interpreting symbol: " + sym);
            if (this.isOperator(sym))
            {
                System.out.println("Symbol identified as operator");
                AbstractExpression rhs = stack.pop();
                AbstractExpression lhs = stack.pop();
                AbstractExpression operator = new OperatorExpression(sym, lhs, rhs);
                Double result = operator.interpret();
                AbstractExpression operand = new OperandExpression(result);
                stack.push(operand);
            }
            else if (this.isOperand(sym))
            {
                System.out.println("Symbol identified as operand");
                AbstractExpression operand = new OperandExpression(sym);
                stack.push(operand);
            }
        }
        System.out.println("Result: " + stack.pop().interpret());
    }

    private boolean isOperator(String sym)
    {
        boolean result = true;

        if (sym.length() != 1 || !OPERATORS.contains(sym))
        {
            System.out.println("returning false on " + sym);
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
