package decorator.decorationtypes;

import decorator.BaseDecoration;
import tree.BaseTree;

public class BallsRed extends BaseDecoration{

    private static final String specialName = "Balls Red";
    private static final double specialCost = 1.0D;

    public BallsRed(BaseTree previousTree){

        this.previousTree = previousTree;

        this.decorationName = specialName;
        this.decorationCost = specialCost;

    }

}
