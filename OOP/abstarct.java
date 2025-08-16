abstract class food{
    abstract void eat();
}
class chicken extends food{
    @Override
    void eat(){
        System.out.println("Chicken kosha");
    }
}
class abstra{
    public static void main(String[] args) {
        chicken ch = new chicken();
        ch.eat();
    }
}