package decoration;

import tree.Tree;

public class Ribbons extends Decoration
{
	private String name = "Ribbons";
	private double cost = 2.0;
	
	public Ribbons(Tree tree) {
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
