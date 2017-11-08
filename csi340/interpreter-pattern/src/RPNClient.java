import java.util.Stack;
import java.util.*;

public class RPNClient
{
    private ArrayList<String> OPERATORS = new ArrayList<String>(Arrays.asList("+", "-", "*", "/"));

    public boolean verbose = false;

    public void interpret(String expression)
    {
        Stack<AbstractExpression> stack = new Stack<AbstractExpression>();
        String[] symbols = expression.split(" ");

        if (this.verbose) { System.out.println("Interpreting expression: " + expression); }

        for (String sym : symbols)
        {
            if (this.verbose) { System.out.println("Interpreting symbol: " + sym); }
            if (this.isOperator(sym))
            {
                if (this.verbose) { System.out.println("Symbol identified as operator"); }
                AbstractExpression rhs = stack.pop();
                AbstractExpression lhs = stack.pop();
                AbstractExpression operator = new OperatorExpression(sym, lhs, rhs);
                Double result = operator.interpret();
                AbstractExpression operand = new OperandExpression(result);
                stack.push(operand);
            }
            else if (this.isOperand(sym))
            {
                if (this.verbose) { System.out.println("Symbol identified as operand"); }
                AbstractExpression operand = new OperandExpression(sym);
                stack.push(operand);
            }
        }

        double result = stack.pop().interpret();

        if (this.verbose) { System.out.println("Result: " + result); }
        else
        {
            System.out.println(expression + " = " + result);
        }
    }

    private boolean isOperator(String sym)
    {
        boolean result = true;

        if (sym.length() != 1 || !OPERATORS.contains(sym))
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
