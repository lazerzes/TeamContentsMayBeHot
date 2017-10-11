package decorator.decorationtypes;

import decorator.BaseDecoration;
import tree.BaseTree;

public class Ruffles extends BaseDecoration{

    private static final String specialName = "Ruffles";
    private static final double specialCost = 4.0D;

    public Ruffles(BaseTree previousTree){

        this.previousTree = previousTree;

        this.decorationName = specialName;
        this.decorationCost = specialCost;

    }
    
}
