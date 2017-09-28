package auction;

import observer.IObserver;
import subject.ISubject;

public class SubjectAuction implements ISubject {

    public Bid bid;
    public Item item;

    @Override
    public void registerObserver(IObserver observer) {

    }

    @Override
    public void removerObserver(IObserver observer) {

    }

    @Override
    public void notifyObservers() {

    }


}
