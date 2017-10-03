package auction.stratergy;

public interface IBidStratergy {

    double getBid(double current);
    boolean shouldBid();

}
