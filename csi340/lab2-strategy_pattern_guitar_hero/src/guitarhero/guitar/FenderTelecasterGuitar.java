package guitarhero.guitar;

public class FenderTelecasterGuitar implements IGuitar {

    @Override
    public void playGuitar(String name) {
        System.out.print(name + "is playing a Fender Telecaster");
    }
}
