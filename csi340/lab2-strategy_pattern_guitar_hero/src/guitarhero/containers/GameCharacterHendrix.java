package guitarhero.containers;

import guitarhero.guitar.IGuitar;
import guitarhero.solo.ISolo;

public class GameCharacterHendrix extends GameCharacter {

    GameCharacterHendrix(String name, IGuitar guitar, ISolo solo){
        super(name, guitar, solo);
    }

    @Override
    public void display(){
        System.out.println(this.getName() + "looks like Jimi Hendrix!");
    }

}