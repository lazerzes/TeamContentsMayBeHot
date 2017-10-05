package tree;

public class DouglasFir extends Tree
{
	private double cost = 15.0;
	private String name = "Douglas Fir";
	
	public double getCost()
	{
		return this.cost;
	}
	
	public void print()
	{
		System.out.print(this.name + " tree decorated with: ");
	}
}
