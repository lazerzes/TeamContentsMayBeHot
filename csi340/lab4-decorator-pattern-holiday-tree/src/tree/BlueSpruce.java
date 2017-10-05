package tree;

public class BlueSpruce extends Tree
{
	private double cost = 5.0;
	private String name = "Colorado Blue Spruce";
	
	public double getCost()
	{
		return this.cost;
	}
	
	public void print()
	{
		System.out.println(this.name + " tree decorated with: ");
	}
}
