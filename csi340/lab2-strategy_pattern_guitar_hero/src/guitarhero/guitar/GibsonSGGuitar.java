package guitarhero.guitar;

public class GibsonSGGuitar implements IGuitar {

    @Override
    public void playGuitar(String name) {
        System.out.println(name + "is playing on a Gibson SG");
    }
}
