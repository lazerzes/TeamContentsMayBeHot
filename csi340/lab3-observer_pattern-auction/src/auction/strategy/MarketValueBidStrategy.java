package auction.strategy;

import auction.Bid;
import auction.Item;

public class MarketValueBidStrategy implements IBidStrategy {

	@Override
	public double getBid(Bid largestBid, Item item) {
		return item.marketValue;
	}

}
