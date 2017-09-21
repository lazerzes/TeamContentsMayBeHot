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
