package decorator;


import tree.BaseTree;

public class BaseDecoration extends BaseTree {

    protected String decorationName;
    protected double decorationCost;
    protected BaseTree previousTree;

    protected BaseDecoration(){
        this.treeName = "default";
        this.treeCost = 0.00D;
        this.previousTree = null;
    }

    public String getDecorationName(){
        return this.decorationName;
    }

    public double getDecorationCost() {
        return this.decorationCost;
    }

    public BaseTree getPreviousTree(){
        return this.previousTree;
    }

}
