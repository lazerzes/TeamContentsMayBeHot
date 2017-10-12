import decorator.decorationtypes.*;
import tree.BaseTree;
import tree.treetypes.BlueSpruce;
import utils.TreeHelper;

public class HolidayTreeMain {
    public static void main(String[] args) {

        BaseTree myTree = new BlueSpruce();


        myTree = TreeHelper.buildTree(myTree, new Star(myTree));
        myTree = TreeHelper.buildTree(myTree, new Ruffles(myTree));
        myTree = TreeHelper.buildTree(myTree, new Star(myTree));
        myTree = TreeHelper.buildTree(myTree, new Ruffles(myTree));
        myTree = TreeHelper.buildTree(myTree, new LEDs(myTree));
        myTree = TreeHelper.buildTree(myTree, new BallsBlue(myTree));
        myTree = TreeHelper.buildTree(myTree, new BallsRed(myTree));
        myTree = TreeHelper.buildTree(myTree, new BallsSilver(myTree));
        myTree = TreeHelper.buildTree(myTree, new Lights(myTree));
        myTree = TreeHelper.buildTree(myTree, new Ribbons(myTree));


        myTree.print();

    }
}
