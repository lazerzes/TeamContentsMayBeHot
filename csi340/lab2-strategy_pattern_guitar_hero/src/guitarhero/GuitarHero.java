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
