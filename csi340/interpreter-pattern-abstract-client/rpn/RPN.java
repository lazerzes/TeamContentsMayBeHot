package rpn;

import interpreter.AbstractExpression;
import interpreter.AbstractContext;
import java.util.Stack;
import java.util.ArrayList;

public class RPN extends AbstractContext
{
    private Stack<Double> mStack;

    public RPN()
    {
        this.mStack = new Stack<Double>();
    }

    public void push(Double value)
    {
        this.mStack.push(value);
    }

    public Double pop()
    {
        return this.mStack.pop();
    }

    public ArrayList<AbstractExpression> parse(String symbols)
    {
        ArrayList<AbstractExpression> expressions = new ArrayList<AbstractExpression>();
        String[] splitSymbols = symbols.split(" ");
        AbstractExpression tmp;

        for (String sym : splitSymbols)
        {
            tmp = null;

            if (AdditionExpression.evaluate(sym))
            {
                tmp = new AdditionExpression();
            }
            else if (SubtractionExpression.evaluate(sym))
            {
                tmp = new SubtractionExpression();
            }
            else if (MultiplicationExpression.evaluate(sym))
            {
                tmp = new MultiplicationExpression();
            }
            else if (DivisionExpression.evaluate(sym))
            {
                tmp = new DivisionExpression();
            }
            else if (OperandExpression.evaluate(sym))
            {
                tmp = new OperandExpression(sym);
            }
            expressions.add(tmp);
        }
        return expressions;
    }

    public void displayResult()
    {
        Double result = this.mStack.pop();
        System.out.println(result);
    }
}
