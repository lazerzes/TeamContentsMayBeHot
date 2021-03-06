/*
Author:              Rei Armenia & Matthew Harrison
Class:               CSI-340-01
Assignment:          Lab 2
Date Assigned:       September 19th
Due Date:            September 28th
 
Description:
Game Character, Base Class. Code was generated by Rei Armenia.
 
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
package guitarhero.containers;

import guitarhero.guitar.IGuitar;
import guitarhero.solo.ISolo;

public abstract class GameCharacter {

    protected String name;
    protected IGuitar playerGuitar;
    protected ISolo playerSolo;

    GameCharacter(String name, IGuitar guitar, ISolo solo){
        this.name = name;
        this.playerGuitar = guitar;
        this.playerSolo = solo;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public IGuitar getPlayerGuitar() {
        return playerGuitar;
    }

    public void setPlayerGuitar(IGuitar playerGuitar) {
        this.playerGuitar = playerGuitar;
    }

    public ISolo getPlayerSolo() {
        return playerSolo;
    }

    public void setPlayerSolo(ISolo playerSolo) {
        this.playerSolo = playerSolo;
    }

    public void playGuitar(){
        playerGuitar.playGuitar(this.name);
    }

    public void playSolo(){
        playerSolo.playSolo(this.name);
    }

    public abstract void display();

}
