/*
Author:              Rei Armenia & Matthew Harrison
Class:               CSI-340-01
Assignment:          Lab 4 - Decorator Pattern - Holiday Tree
Date Assigned:       October  5th
Due Date:            October 19th
 
Description:
Program for adding ornaments to a holiday tree using decorator design pattern.
 
Certification of Authenticity:    
I certify that this is entirely my own work, except where I have been provided
code by the instructor, or given fully-documented references to the work of 
others. I understand the definition and consequences of plagiarism and 
acknowledge that the assessor of this assignment may, for the purpose of 
assessing this assignment:
    Reproduce this assignment and provide a copy to another member of academic
    staff; and/or Communicate a copy of this assignment to a plagiarism checking
    service (which may then retain a copy of this assignment on its database for 
    the purpose of future plagiarism checking) 
*/

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
