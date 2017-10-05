package tree;

public class BalsamFir extends Tree
{
	private double cost = 20.0;
	private String name = "Balsam Fir";
	
	public double getCost()
	{
		return this.cost;
	}
	
	public void print()
	{
		System.out.print(this.name + " tree decorated with: ");
	}
}
