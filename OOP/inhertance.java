class food{
    void eat(){
        System.out.println("We can eat chicken");
    }
}
class chicken extends food{

}
class inheritance{
    public static void main(String[] args) {
        chicken ch = new chicken();
        ch.eat();
    }
}