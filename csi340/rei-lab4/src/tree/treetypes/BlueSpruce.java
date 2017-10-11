package tree.treetypes;


import tree.BaseTree;

public class BlueSpruce extends BaseTree {

    private static final String specialName = "Colorado Blue Spruce";
    private static final double specialCost = 5.00D;

    public BlueSpruce(){
        this.treeName = specialName;
        this.treeCost = specialCost;
    }

}
