package decorator.decorationtypes;

import decorator.BaseDecoration;
import tree.BaseTree;

public class BallsSilver extends BaseDecoration{

    private static final String specialName = "Balls Silver";
    private static final double specialCost = 3.0D;

    public BallsSilver(BaseTree previousTree){

        this.previousTree = previousTree;

        this.decorationName = specialName;
        this.decorationCost = specialCost;

    }

}
