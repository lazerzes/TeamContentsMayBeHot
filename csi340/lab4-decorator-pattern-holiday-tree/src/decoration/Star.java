package decoration;

import tree.Tree;

public class Star extends Decoration
{
	public Star(Tree tree) {
		super(tree);
	}

	public double getCost()
	{
		return 1.0;
	}
}
