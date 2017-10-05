package auction.constraint;

import auction.Bid;
import auction.Item;

public interface IBidConstraint {

	boolean getResult(Bid largestBid, Bid myBid, Item item);
	
}
