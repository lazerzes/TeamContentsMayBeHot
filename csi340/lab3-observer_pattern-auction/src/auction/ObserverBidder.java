package auction;

import auction.stratergy.IBidStratergy;
import observer.IObserver;
import subject.ISubject;

public class ObserverBidder implements IObserver {

    public Bid largestBid;
    public Item item;
    public IBidStratergy bidStratergy;

    public ObserverBidder(IBidStratergy bidStratergy){
        this.bidStratergy = bidStratergy;
    }

    @Override
    public void update(ISubject subject){

        if(subject instanceof SubjectAuction){
            this.item = ((SubjectAuction) subject).item;
            this.largestBid = ((SubjectAuction) subject).bid;
        }else{
            System.out.println("ERROR: UNABLE TO UNPACK THE PASSED SUBJECT. QUITTING...");
            System.exit(1);
        }

    }

    public void makeBid(ISubject subject){
        if(subject instanceof SubjectAuction){
            if(!largestBid.bidder.equals(this)){
                if(bidStratergy.shouldBid()){
                    Bid bid = new Bid(this, this.bidStratergy.getBid(largestBid.ammount));
                    ((SubjectAuction) subject).revieveBid(bid);
                }
            }else{
                System.out.println(this + "could not bid, it is already the largest Bidder");
            }
        }else{
            System.out.println("ERROR: UNABLE TO UNPACK THE PASSED SUBJECT. QUITTING...");
            System.exit(1);
        }
    }

}
