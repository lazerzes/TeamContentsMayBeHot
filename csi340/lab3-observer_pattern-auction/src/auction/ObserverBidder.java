package auction;

import java.util.ArrayList;

import auction.strategy.IBidStrategy;
import auction.constraint.IBidConstraint;
import observer.IObserver;
import subject.ISubject;

public class ObserverBidder implements IObserver {

    public Bid largestBid;
    public Item item;
    public IBidStrategy bidStrategy;
    public ArrayList<IBidConstraint> bidConstraints;

    public ObserverBidder(IBidStrategy bidStrategy) {
    	this.bidConstraints = new ArrayList<IBidConstraint>();
        this.bidStrategy = (bidStrategy);
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
    
    public void addConstraint(IBidConstraint constraint) {
    	this.bidConstraints.add(constraint);
    }

    public void makeBid(ISubject subject){
        if(subject instanceof SubjectAuction) {
        	// If I am NOT the largest bidder
            if(!largestBid.bidder.equals(this) ) {
            	// Compute my bid amount
            	Bid myBid = new Bid(this, this.bidStrategy.getBid(largestBid, item));
            	
            	// Check if my bid is sufficient
            	if (myBid.amount <= largestBid.amount) {
            		myBid.amount = 0;
            	}
            	
            	// Check if my bid violates any of my constraints
            	for (IBidConstraint constraint : this.bidConstraints) {
            		if (!constraint.getResult(largestBid, myBid, item)) {
            			myBid.amount = 0;
            		}
            	}
            	
            	// Finalize my bid if it passes constraints
                if(myBid.amount > 0) {
                	System.out.println(this + "is bidding" + myBid.amount);
                    ((SubjectAuction) subject).revieveBid(myBid);
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
