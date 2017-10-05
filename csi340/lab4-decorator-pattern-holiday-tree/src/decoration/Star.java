package decoration;

import tree.Tree;

public class Star extends Decoration
{
	private String name = "Star";
	private double cost = 1.0;
	
	public Star(Tree tree) {
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
