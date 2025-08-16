class food3{
    private String name;
    private int cost;
    private String hotel;

    void nonveg(String name, int cost, String hotel){
        this.setname(name);
        this.setcost(cost);
        this.sethotel(hotel);
    }
    //setter method to set the value
    public void setname(String name){
        this.name = name;
    }
    public void setcost(int cost){
        this.cost = cost;
    }
    public void sethotel(String hotel){
        this.hotel = hotel;
    }
    //getter method to get all value
    public String getname(){
        return name;
    }
    public int getcost(){
        return cost;
    }
    public String hotel(){
        return hotel;
    }
}

class encapsulation{
    public static void main(String[] args) {
        food3 fo = new food3();
        fo.nonveg("chicken kosha", 320 ,"Golbari");
        fo.setcost(350);
        System.out.println(fo.getname());
        System.out.println(fo.getcost());
        System.out.println(fo.hotel());
    }
}