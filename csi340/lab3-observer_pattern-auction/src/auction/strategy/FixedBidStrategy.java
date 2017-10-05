package auction.strategy;

import auction.Bid;
import auction.Item;

public class FixedBidStrategy implements IBidStrategy {
	
	double amount;
	
	public FixedBidStrategy(double amount) {
		this.amount = amount;
	}
	
	@Override
	public double getBid(Bid largestBid, Item item) {
		return largestBid.amount + this.amount;
	}

}
