package decoration;

import tree.Tree;

public class BallsBlue extends Decoration
{
	private String name = "Balls Blue";
	private double cost = 2.0;
	
	public BallsBlue(Tree tree)
	{
		super(tree);
	}

	public double getCost()
	{
		return tree.getCost() + this.cost;
	}

	public void print()
	{
		tree.print();
		System.out.println("\t" + name + "($" + cost + ")");
	}
}
