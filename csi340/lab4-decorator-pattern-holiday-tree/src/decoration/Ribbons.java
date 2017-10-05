package decoration;

import tree.Tree;

public class Ribbons extends Decoration
{
	public Ribbons(Tree tree) {
		super(tree);
	}

	public double getCost()
	{
		return 2.0;
	}
}
