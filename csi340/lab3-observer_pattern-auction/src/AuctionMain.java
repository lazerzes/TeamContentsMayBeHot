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

import auction.*;
import auction.strategy.*;
import auction.constraint.*;

public class AuctionMain {

    public static void main(String[] args) {
    	Item item1 = new Item("2307 Starry Teflon (Non-Stick) CMYK Backlit Mechanakanical KIBORDE", 120, 3400);
    	Item item2 = new Item("Rare Bannanneer (Bannayonet Included)", 80, 680);
    	Item item3 = new Item("Chalky Substance (Up to 4,000,000 PSI)", 400, 10000);
    	
    	// Inexperienced bidder with a budget
    	ObserverBidder bidder1 = new ObserverBidder(new FixedBidStrategy(10));
    	bidder1.addConstraint(new MarketValueConstraint());
    	bidder1.addConstraint(new MaxBidConstraint(500));
    	
    	// Strategic bidder with cash to burn
    	ObserverBidder bidder2 = new ObserverBidder(new HalfLifeBidStrategy(100));
    	bidder2.addConstraint(new MarketValueFactorConstraint(5));
    	bidder2.addConstraint(new MaxBidConstraint(20000));
    	
    	// "Buy it Now" fanatic, will give in to any competition
    	ObserverBidder bidder3 = new ObserverBidder(new MarketValueBidStrategy());
    	bidder3.addConstraint(new MarketValueConstraint());
    	
    	// Bored and rich, interest is difficult to gain but easy to lose
    	ObserverBidder bidder4 = new ObserverBidder(new RandomBidStrategy());
    	bidder4.addConstraint(new MinBidConstraint(1000));
    	bidder4.addConstraint(new MinBidCountConstraint(9));
    	bidder4.addConstraint(new MaxBidCountConstraint(21));
    	bidder4.addConstraint(new RandomConstraint());

    	SubjectAuction auction = new SubjectAuction(item1);
    }

}
