import decorator.decorationtypes.Ruffles;
import decorator.decorationtypes.Star;
import tree.BaseTree;
import tree.treetypes.BlueSpruce;

public class HolidayTreeMain {
    public static void main(String[] args) {
        BaseTree myTree = new BlueSpruce();
        myTree = new Star(myTree);
        myTree = new Ruffles(myTree);
        myTree = new Star(myTree);
        myTree = new Ruffles(myTree);
        myTree.print();
    }
}
