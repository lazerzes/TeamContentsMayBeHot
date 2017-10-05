package auction.strategy;

import auction.Bid;
import auction.Item;

public class HalfLifeBidStrategy implements IBidStrategy {
	
	double amount;
	
	public HalfLifeBidStrategy(double initialBid) {
		this.amount = initialBid;
	}
	@Override
	public double getBid(Bid largestBid, Item item) {
		this.amount /= 2;
		
		return largestBid.amount + this.amount;
	}

}
