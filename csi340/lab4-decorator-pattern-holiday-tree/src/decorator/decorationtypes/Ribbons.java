package decorator.decorationtypes;

import decorator.BaseDecoration;
import tree.BaseTree;

public class Ribbons extends BaseDecoration{

    private static final String specialName = "Ribbons";
    private static final double specialCost = 2.0D;

    public Ribbons(BaseTree previousTree){

        this.previousTree = previousTree;

        this.decorationName = specialName;
        this.decorationCost = specialCost;

    }

}
