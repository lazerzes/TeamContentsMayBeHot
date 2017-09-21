package guitarhero.guitar;

public class GibsonFlyingVGuitar implements IGuitar {


    @Override
    public void playGuitar(String name) {
        System.out.println(name + " is playing a Gibson Flying V");
    }
}


