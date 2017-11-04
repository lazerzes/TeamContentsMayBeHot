import Context, AbstractExpression;

public class Client
{
    private Context mContext;
    private ArrayList<AbstractExpression> mExpressions;

    public Client(Context context)
    {
        this.mContext = context;
    }

    public addExpression(AbstractExpression expression)
    {
        this.mExpressions.add(expression);
    }

    public interpret()
    {
        for (AbstractExpression expression : this.mExpressions)
        {
            expression.interpret(this.context);
        }
    }
}
