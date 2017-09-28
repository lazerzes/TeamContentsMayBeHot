/*
Author:              Rei Armenia & Matthew Harrison
Class:               CSI-340-01
Assignment:          Lab 2
Date Assigned:       September 19th
Due Date:            September 28th
 
Description:
Main Function, Code was done by Matthew.
 
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

package guitarhero;

import guitarhero.containers.*;
import guitarhero.guitar.*;
import guitarhero.solo.*;

public class GuitarHero {
  
  public void main(String[] args){
	  
	  GameCharacter player1 = new GameCharacterAngus("Player One", new FenderTelecasterGuitar(), new GuitarFireSolo());
	  GameCharacter player2 = new GameCharacterHendrix("Player Two", new GibsonFlyingVGuitar(), new GuitarSmashSolo());
	  GameCharacter player3 = new GameCharacterSlash("Player Three", new GibsonSGGuitar(), new StageJumpSolo());
	  
	  player1.display();
	  player1.playGuitar();
	  player1.playSolo();
	  
	  player2.display();
	  player2.playGuitar();
	  player2.playSolo();
	  
	  player3.display();
	  player3.playGuitar();
	  player3.playSolo();
	  
	  player3.setPlayerGuitar(new FenderTelecasterGuitar());
	  player3.playGuitar();
	  
	  player1.setPlayerSolo(new GuitarSmashSolo());
	  player1.playSolo();
	  
	  
  }
  
}
