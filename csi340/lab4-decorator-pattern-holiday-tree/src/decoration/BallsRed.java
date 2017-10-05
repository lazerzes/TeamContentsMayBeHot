package decoration;

import tree.Tree;

public class BallsRed extends Decoration
{
	private String name = "Balls Red";
	private double cost = 1.0;
	
	public BallsRed(Tree tree) {
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
