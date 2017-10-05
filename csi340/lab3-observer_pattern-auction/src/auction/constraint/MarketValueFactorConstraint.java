package auction.constraint;

import auction.Bid;
import auction.Item;

public class MarketValueFactorConstraint implements IBidConstraint {

	double factor;
	
	public MarketValueFactorConstraint(double factor) {
		this.factor = factor;
	}
	
	@Override
	public boolean getResult(Bid largestBid, Bid myBid, Item item) {
		boolean result = true;
		
		if (myBid.amount > (item.marketValue * factor))
		{
			result = false;
		}
		
		return result;
	}

}
