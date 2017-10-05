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

package auction.strategy;

import auction.Bid;
import auction.Item;

public interface IBidStrategy {

    double getBid(Bid largestBid, Item item);

}
