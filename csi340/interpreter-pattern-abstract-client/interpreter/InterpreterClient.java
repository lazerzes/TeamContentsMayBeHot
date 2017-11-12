package interpreter;

import java.util.ArrayList;

public class InterpreterClient
{
    private ArrayList<AbstractExpression> mExpressions;
    private AbstractContext mContext;

    public InterpreterClient(AbstractContext context)
    {
        this.mContext = context;
    }

    public void interpret(String symbols)
    {
        this.mExpressions = this.mContext.parse(symbols);

        for (AbstractExpression expression : this.mExpressions)
        {
            expression.interpret(this.mContext);
        }

        this.mContext.displayResult();
    }
}
