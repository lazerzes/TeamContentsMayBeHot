package guitarhero.solo;

public class GuitarSmashSolo implements ISolo{

    @Override
    public void playSolo(String name){
        System.out.println(name + " smashed their Guitar.");
    }

}
