package decoration;

import tree.Tree;

public class Lights extends Decoration
{
	private String name = "Lights";
	private double cost = 5.0;
	
	public Lights(Tree tree) {
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
