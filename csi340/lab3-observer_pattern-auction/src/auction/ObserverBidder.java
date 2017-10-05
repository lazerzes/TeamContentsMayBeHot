package auction;

import auction.strategy.IBidStrategy;
import observer.IObserver;
import subject.ISubject;

public class ObserverBidder implements IObserver {

    public Bid largestBid;
    public Item item;
    public IBidStrategy bidStrategy;

    public ObserverBidder(IBidStrategy bidStrategy) {
        this.bidStrategy = bidStrategy;
    }

    @Override
    public void update(ISubject subject) {

        if(subject instanceof SubjectAuction) {
            this.item = ((SubjectAuction) subject).item;
            this.largestBid = ((SubjectAuction) subject).bid;
        }else {
            System.out.println("ERROR: UNABLE TO UNPACK THE PASSED SUBJECT. QUITTING...");
            System.exit(1);
        }

    }

    public void makeBid(ISubject subject){
        if(subject instanceof SubjectAuction) {
        	// If I am NOT the largest bidder
            if(!largestBid.bidder.equals(this) ){
                if(bidStrategy.shouldBid()){
                    Bid bid = new Bid(this, this.bidStrategy.getBid(largestBid.ammount));
                    ((SubjectAuction) subject).revieveBid(bid);
                }
            }
            // If I AM the largest bidder
            else {
                System.out.println(this + "could not bid, it is already the largest Bidder");
            }
        }
        else {
            System.out.println("ERROR: UNABLE TO UNPACK THE PASSED SUBJECT. QUITTING...");
            System.exit(1);
        }
    }

}
