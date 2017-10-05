package decoration;

import tree.Tree;

public class LEDs extends Decoration
{
	public LEDs(Tree tree) {
		super(tree);
	}

	public double getCost()
	{
		return 10.0;
	}
}
