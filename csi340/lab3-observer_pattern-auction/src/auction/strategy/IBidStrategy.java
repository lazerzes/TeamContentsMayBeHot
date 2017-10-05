package auction.strategy;

public interface IBidStrategy {

    double getBid(double current);
    boolean shouldBid();

}
