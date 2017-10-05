package auction.constraint;

import auction.Bid;
import auction.Item;

public class MinBidCountConstraint implements IBidConstraint {

	double min;
	
	public MinBidCountConstraint(double min) {
		this.min = min;
	}
	
	@Override
	public boolean getResult(Bid largestBid, Bid myBid, Item item) {
		boolean result = true;
		
		if (largestBid.getCount() < min) {
			result = false;
		}
		
		return result;
	}

}
