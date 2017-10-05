import tree.*;
import decoration.*;

public class HolidayTreeMain {

	public static void main(String[] args) {
		Tree myTree = new BlueSpruce();
		myTree = new Star(myTree);
		myTree = new Ruffles(myTree);
		myTree = new Star(myTree);
		myTree = new Ruffles(myTree);
	}
}
