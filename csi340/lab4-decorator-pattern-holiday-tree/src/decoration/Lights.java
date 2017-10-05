package decoration;

import tree.Tree;

public class Lights extends Decoration
{
	public Lights(Tree tree) {
		super(tree);
	}

	public double getCost()
	{
		return 5.0;
	}
}
