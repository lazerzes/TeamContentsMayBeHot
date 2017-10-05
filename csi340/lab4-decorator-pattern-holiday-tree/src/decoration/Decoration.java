package decoration;

import tree.Tree;

public abstract class Decoration extends Tree
{
	public Tree tree;
	
	public Decoration(Tree tree)
	{
		this.tree = tree;
	}
}
