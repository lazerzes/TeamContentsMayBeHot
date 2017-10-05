package auction.constraint;

import auction.Bid;
import auction.Item;

public class RandomConstraint implements IBidConstraint {

	@Override
	public boolean getResult(Bid largestBid, Bid myBid, Item item) {
		boolean result = true;
		
		if (Math.random() >= 0.5):
			result = false;
		
		return result;
	}

}
