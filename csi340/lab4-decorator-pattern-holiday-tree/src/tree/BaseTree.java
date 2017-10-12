package tree;

import utils.TreeHelper;

public class BaseTree {

    protected String treeName;
    protected double treeCost;

    protected BaseTree(){
        this.treeName = "default";
        this.treeCost = 0.00D;
    }

    public String getTreeName(){
        return this.treeName;
    }

    public double getTreeCost() {
        return treeCost;
    }

    public void print(){
        System.out.println(TreeHelper.printHelper(this));
    }
}
