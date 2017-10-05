package auction.strategy;

import auction.Bid;
import auction.Item;

public interface IBidStrategy {

    double getBid(Bid largestBid, Item item);

}
