package decoration;

import tree.Tree;

public class BallsBlue extends Decoration
{
	public BallsBlue(Tree tree) {
		super(tree);
	}

	public double getCost()
	{
		return 2.0;
	}
}
