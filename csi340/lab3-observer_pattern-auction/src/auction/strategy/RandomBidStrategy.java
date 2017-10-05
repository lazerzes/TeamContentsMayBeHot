package auction.strategy;

import auction.Bid;
import auction.Item;

public class RandomBidStrategy implements IBidStrategy {

	@Override
	public double getBid(Bid largestBid, Item item) {
		return largestBid.amount + (largestBid.amount * Math.random());
	}

}
