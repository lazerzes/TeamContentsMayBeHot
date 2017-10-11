package decorator.decorationtypes;

import decorator.BaseDecoration;
import tree.BaseTree;

public class LEDs extends BaseDecoration{

    private static final String specialName = "LEDs";
    private static final double specialCost = 10.0D;

    public LEDs(BaseTree previousTree){

        this.previousTree = previousTree;

        this.decorationName = specialName;
        this.decorationCost = specialCost;

    }

}
