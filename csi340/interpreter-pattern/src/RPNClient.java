package rpn;

import java.util.Stack;

public class RPNClient
{
    private char[] NUMBERS = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'};
    private char[] OPERATORS = {'+', '-', '*', '/'};

    public void addExpression(AbstractExpression expression)
    {
        this.mExpressions.add(expression);
    }

    public void interpret(String expression)
    {
        Stack stack = new Stack();
        String[] symbols = expression.split(' ');

        for (String sym : symbols)
        {
            if (this.isOperator(sym))
            {
                AbstractExpression operator = new OperatorExpression(sym);
                AbstractExpression rhs = stack.pop();
                AbstractExpression lhs = stack.pop();
                Double result = operator.interpret(lhs, rhs);
                AbstractExpression operand = new OperandExpression(result);
            }
            else if (this.isOperand(sym))
            {
                AbstractExpression operand = new OperandExpression(sym);
                stack.push(operand);
            }
        }

        for (AbstractExpression expression : this.mExpressions)
        {
            expression.interpret(this.context);
        }
    }

    private boolean isOperator(String sym)
    {
        result = true;

        if (sym.length != 1 || !OPERATORS.contains(sym[0]))
        {
            result = false;
        }

        return result;
    }

    private boolean isOperand(String sym)
    {
        result = true;

        for (int i = 0; i < sym.length(); i++)
        {
            if (!NUMBERS.contains(sym[i]))
            {
                result = false;
                break;
            }
        }

        return result;
    }
}
