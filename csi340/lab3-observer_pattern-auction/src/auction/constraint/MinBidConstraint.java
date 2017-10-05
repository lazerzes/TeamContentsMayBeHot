package auction.constraint;

import auction.Bid;
import auction.Item;

public class MinBidConstraint implements IBidConstraint {

	double min;
	
	public MinBidConstraint(double min) {
		this.min = min;
	}
	
	@Override
	public boolean getResult(Bid largestBid, Bid myBid, Item item) {
		boolean result = true;
		
		if (myBid.amount < this.min) {
			result = false;
		}

		return result;
	}

}
