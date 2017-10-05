package decoration;

import tree.Tree;

public class Ruffles extends Decoration
{
	private String name = "Ruffles";
	private double cost = 4.0;
	
	public Ruffles(Tree tree) {
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
