package utils;

import decorator.BaseDecoration;
import decorator.decorationtypes.Star;
import tree.BaseTree;

import java.util.ArrayList;

public class TreeHelper {

    public static String printHelper(BaseTree tree){

        ArrayList<String> decorationsList = new ArrayList<String>();
        String printFormatting = "";
        double totalCost = 0.0D;

        if(tree instanceof BaseDecoration){
            String tmp = ((BaseDecoration) tree).getDecorationName() + " +(" + ((BaseDecoration) tree).getDecorationCost() + ")";
            totalCost += ((BaseDecoration) tree).getDecorationCost();
            decorationsList.add(tmp);

            BaseTree nxt = ((BaseDecoration) tree).getPreviousTree();
            while(nxt instanceof BaseDecoration){
                tmp = ((BaseDecoration) nxt).getDecorationName() + " +(" + ((BaseDecoration) nxt).getDecorationCost() + ")";
                totalCost += ((BaseDecoration) nxt).getDecorationCost();
                decorationsList.add(tmp);
                nxt = ((BaseDecoration) nxt).getPreviousTree();
            }
            printFormatting = nxt.getTreeName() + " Tree ($" + nxt.getTreeCost() + "):\n";
            totalCost += nxt.getTreeCost();
        }else{
            printFormatting = tree.getTreeName() + " Tree ($" + tree.getTreeCost() + "):\n";
            totalCost += tree.getTreeCost();
        }

        if(decorationsList.size() > 0){
            for(String d : decorationsList){
                printFormatting += ("\t" + d + "\n");
            }
        }else{
            printFormatting += "\t No Decorations +$0.00";
        }

        printFormatting += ("\n--------------------\n Total Cost: $" + totalCost + "\n");
        return printFormatting;

    }

    public static boolean hasStar(BaseTree tree){
        if(tree instanceof BaseDecoration){
            BaseTree tmp = ((BaseDecoration) tree).getPreviousTree();
            while(tmp instanceof BaseDecoration){
                if(tmp instanceof Star){
                    return true;
                }
            }
        }
        return false;
    }

}
