package auction.stratergy;

public interface IBidStrategy {

    double getBid(double current);
    boolean shouldBid();

}
