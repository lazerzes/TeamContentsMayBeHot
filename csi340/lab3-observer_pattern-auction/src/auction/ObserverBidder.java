package auction;

import observer.IObserver;
import subject.ISubject;

public class ObserverBidder implements IObserver {

    Bid largestBid;
    Item item;

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

            }else{
                System.out.println(this + "could not bid, it is already the largest Bidder");
            }
        }else{
            System.out.println("ERROR: UNABLE TO UNPACK THE PASSED SUBJECT. QUITTING...");
            System.exit(1);
        }
    }

}