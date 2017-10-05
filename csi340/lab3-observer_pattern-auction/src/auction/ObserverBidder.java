/*
Author:              Rei Armenia & Matthew Harrison
Class:               CSI-340-01
Assignment:          Lab 3 - Observer Pattern - Auction
Date Assigned:       September 28th
Due Date:            October    4th
 
Description:
Online auction program using observer design pattern.
 
Certification of Authenticity:    
I certify that this is entirely my own work, except where I have been provided
code by the instructor, or given fully-documented references to the work of 
others. I understand the definition and consequences of plagiarism and 
acknowledge that the assessor of this assignment may, for the purpose of 
assessing this assignment:
    Reproduce this assignment and provide a copy to another member of academic
    staff; and/or Communicate a copy of this assignment to a plagiarism checking
    service (which may then retain a copy of this assignment on its database for 
    the purpose of future plagiarism checking) 
*/

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
            this.makeBid(subject);
        }
        else {
            System.out.println("ERROR: UNABLE TO UNPACK THE PASSED SUBJECT. QUITTING...");
            System.exit(1);
        }

    }
    
    public void addConstraint(IBidConstraint constraint) {
    	this.bidConstraints.add(constraint);
    }

    public void makeBid(ISubject subject){
    	if (!(subject instanceof SubjectAuction)) {
            System.out.println("ERROR: UNABLE TO UNPACK THE PASSED SUBJECT. QUITTING...");
            System.exit(1);
        }
    	
    	if (this == largestBid.bidder) {
    		return;
    	}
    	
    	// Compute my bid amount
    	Bid myBid = new Bid(this, this.bidStrategy.getBid(largestBid, item));
    	
    	// Check if my bid is sufficient
    	if (myBid.amount <= largestBid.amount) {
    		return;
    	}
    	
    	// Check if my bid violates any of my constraints
    	for (IBidConstraint constraint : this.bidConstraints) {
    		if (!constraint.getResult(largestBid, myBid, item)) {
    			return;
    		}
    	}
    	
    	// Finalize my bid if it passes constraints
        if(myBid.amount > 0) {
        	System.out.println(this + " is bidding " + myBid.amount);
            ((SubjectAuction) subject).revieveBid(myBid);
        }
    }
}
