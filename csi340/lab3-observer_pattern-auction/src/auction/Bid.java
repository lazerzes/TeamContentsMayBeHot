package auction;

public class Bid {

    public ObserverBidder bidder;
    public double amount;
    public int id;
    private static int count = 0;

    public Bid(ObserverBidder bidder, double amount){
        this.bidder = bidder;
        this.amount = amount;
        
        id = count;
        count++;
    }
    
    public int getCount()
    {
    	return count;
    }

}
