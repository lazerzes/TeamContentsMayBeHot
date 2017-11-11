package interpreter;

import java.util.ArrayList;

public abstract class AbstractContext
{
    public abstract ArrayList<AbstractExpression> parse(String symbols);
    public abstract void displayResult();
}
