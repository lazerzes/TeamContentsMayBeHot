package tree;

public class FraserFir extends Tree
{
	private String name = "Fraser Fir";
	private double cost = 12.0;
	
	public double getCost()
	{
		return this.cost;
	}
	
	public void print()
	{
		System.out.print(this.name + " tree decorated with: ");
	}
}
