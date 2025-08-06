public class ex02 {
    public static void main(String[] args){
        System.out.print("\n");
        for(int i = 0; i <= 100; i++){
            if(i == 0){
                System.out.print("  0 ");
            }
            else if(i % 2 == 0){
                System.out.print(" " +i+ " ");
            }
            if(i % 10 == 0 && i != 0){
                System.out.print("\n");
            }
        }
    }
}
