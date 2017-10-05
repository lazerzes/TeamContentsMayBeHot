package auction;

public class Item {
	public String name;
	public double basePrice;
	public double marketValue;
	
	public Item(String name, double basePrice, double marketValue) {
		this.name = name;
		this.basePrice = basePrice;
		this.marketValue = marketValue;
	}
}
