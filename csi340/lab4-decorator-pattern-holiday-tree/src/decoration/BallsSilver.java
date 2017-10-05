package decoration;

import tree.Tree;

public class BallsSilver extends Decoration
{
	private String name = "Balls Silver";
	private double cost = 3.0;
	
	public BallsSilver(Tree tree) {
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
