package auction;

import observer.IObserver;
import subject.ISubject;

import java.util.ArrayList;

public class SubjectAuction implements ISubject {

    public Bid bid;
    public Item item;

    ArrayList<ObserverBidder> observers;

    public SubjectAuction(Item item ){
        this.item = item;
        this.bid = null;
        this.observers = new ArrayList<ObserverBidder>();
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

        for (ObserverBidder bidder : this.observers) {
            bidder.update(this);
        }

    }

    public void revieveBid(Bid bid) {

        if(bid.ammount < this.bid.ammount || this.bid.equals(null)) {
            this.bid = bid;
        }

        notifyObservers();

    }


}
