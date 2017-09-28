package subject;

import observer.IObserver;

public interface ISubject {

    void registerObserver(IObserver observer);

    void removerObserver(IObserver observer);

    void notifyObservers();

}
