package decoration;

import tree.Tree;

public class LEDs extends Decoration
{
	private String name = "LEDs";
	private double cost = 10.0;
	
	public LEDs(Tree tree) {
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
