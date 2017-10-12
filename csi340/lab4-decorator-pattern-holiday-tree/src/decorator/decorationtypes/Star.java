package decorator.decorationtypes;

import decorator.BaseDecoration;
import tree.BaseTree;
import utils.TreeHelper;

public class Star extends BaseDecoration{

    private static final String specialName = "Star";
    private static final double specialCost = 1.0D;

    public Star(BaseTree previousTree){

        this.previousTree = previousTree;

        this.decorationName = specialName;
        this.decorationCost = specialCost;

    }

}
