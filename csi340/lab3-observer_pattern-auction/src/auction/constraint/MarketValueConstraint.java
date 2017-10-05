package auction.constraint;

import auction.Bid;
import auction.Item;

public class MarketValueConstraint implements IBidConstraint {

	@Override
	public boolean getResult(Bid largestBid, Bid myBid, Item item) {
		boolean result = true;
		
		if (myBid.amount > item.marketValue)
		{
			result = false;
		}
		
		return result;
	}

}
