package tree.treetypes;


import tree.BaseTree;

public class DouglasFir extends BaseTree {

    private static final String specialName = "Douglas Fir";
    private static final double specialCost = 15.00D;

    public DouglasFir(){
        this.treeName = specialName;
        this.treeCost = specialCost;
    }

}
