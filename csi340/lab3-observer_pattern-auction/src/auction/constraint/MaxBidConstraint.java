package auction.constraint;

import auction.Bid;
import auction.Item;

public class MaxBidConstraint implements IBidConstraint {

	double max;
	
	public MaxBidConstraint(double max) {
		this.max = max;
	}
	
	@Override
	public boolean getResult(Bid largestBid, Bid myBid, Item item) {
		boolean result = true;
		
		if (myBid.amount > this.max) {
			result = false;
		}

		return result;
	}

}
