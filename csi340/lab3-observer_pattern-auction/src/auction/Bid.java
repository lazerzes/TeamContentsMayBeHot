package auction;

public class Bid {

    public ObserverBidder bidder;
    public double ammount;

    public Bid(ObserverBidder bidder, double amount){
        this.bidder = bidder;
        this.ammount = amount;
    }

}
