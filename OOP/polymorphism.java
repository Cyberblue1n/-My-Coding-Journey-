class person{
    void role(){
        System.out.println("person");
    }
    void extra(){
        System.out.println("hehe");
    }
}
class lover extends person{

    void role(){
        System.out.println("Lover");
    }
    public static void main(String args[]){
        person p = new person();
        p.role();
        lover l = new lover();
        l.role();
        l.extra();
    }
}