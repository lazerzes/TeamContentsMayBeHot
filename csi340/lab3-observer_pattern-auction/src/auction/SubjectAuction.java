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

import observer.IObserver;
import subject.ISubject;

import java.util.ArrayList;

import auction.constraint.IBidConstraint;

public class SubjectAuction implements ISubject {

    public Bid bid;
    public Item item;
    public int timer;

    ArrayList<ObserverBidder> observers;

    public SubjectAuction(Item item, int timer){
        this.item = item;
        this.bid = new Bid(null, item.basePrice);
        this.observers = new ArrayList<ObserverBidder>();
        this.timer = timer;
        
    	System.out.println("Starting auction for: " + this.item + ". Base price: " + this.bid.amount);
    }
    
    @Override
    public void registerObserver(IObserver observer) {
        if(observer instanceof ObserverBidder){
            this.observers.add((ObserverBidder) observer);
        }else{
            System.out.println("Unable to register Observer(" + observer + "). Incorrect observer type. \n Exiting program...");
            System.exit(1);
        }
    }

    @Override
    public void removerObserver(IObserver observer) {
        if(observer instanceof ObserverBidder) {
            this.observers.remove(observer);
        }
        else {
            System.out.println("Unable to remove Observer(" + observer + "). Incorrect observer type. \n Exiting program...");
            System.exit(1);
        }
    }

    @Override
    public void notifyObservers() {

        this.timer -= 1;
    	System.out.println("Timer:" + this.timer);
        if (this.timer == 0 && !this.observers.isEmpty()) {
        	System.out.println("Winner: " + this.bid.bidder + ". Final bid: " + this.bid.amount);
        }
        else {
            for (ObserverBidder bidder : this.observers) {
        		if (this.bid.bidder != bidder && this.timer > 0) {
                    bidder.update(this);
        		}
            }
        }
    }

    public void receiveBid(Bid bid) {

        if(bid.amount < this.bid.amount || this.bid.equals(null)) {
            return;
        }

        this.bid = bid;
        this.notifyObservers();

    }


}
