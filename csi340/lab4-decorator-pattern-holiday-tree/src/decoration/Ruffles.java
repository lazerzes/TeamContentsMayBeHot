package decoration;

import tree.Tree;

public class Ruffles extends Decoration
{
	public Ruffles(Tree tree) {
		super(tree);
	}

	public double getCost()
	{
		return 4.0;
	}
}
