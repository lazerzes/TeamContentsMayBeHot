package decoration;

import tree.Tree;

public class BallsRed extends Decoration
{
	public BallsRed(Tree tree) {
		super(tree);
	}

	public double getCost()
	{
		return 1.0;
	}
}
