package decorator.decorationtypes;

import decorator.BaseDecoration;
import tree.BaseTree;

public class BallsBlue extends BaseDecoration{

    private static final String specialName = "Balls Blue";
    private static final double specialCost = 2.0D;

    public BallsBlue(BaseTree previousTree){

        this.previousTree = previousTree;

        this.decorationName = specialName;
        this.decorationCost = specialCost;

    }

}
