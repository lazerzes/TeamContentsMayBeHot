package decorator.decorationtypes;

import decorator.BaseDecoration;
import tree.BaseTree;

public class Lights extends BaseDecoration{

    private static final String specialName = "Lights";
    private static final double specialCost = 5.0D;

    public Lights(BaseTree previousTree){

        this.previousTree = previousTree;

        this.decorationName = specialName;
        this.decorationCost = specialCost;

    }

}
