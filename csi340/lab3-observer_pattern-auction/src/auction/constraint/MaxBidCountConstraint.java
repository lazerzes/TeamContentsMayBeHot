package auction.constraint;

import auction.Bid;
import auction.Item;

public class MaxBidCountConstraint implements IBidConstraint {

	int max;
	
	public MaxBidCountConstraint(int max) {
		this.max = max;
	}
	
	@Override
	public boolean getResult(Bid largestBid, Bid myBid, Item item) {
		boolean result = true;
		
		if (largestBid.getCount() > max) {
			result = false;
		}
		
		return result;
	}

}
