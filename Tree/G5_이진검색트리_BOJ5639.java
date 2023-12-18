import java.io.*;
import java.util.*;

class Node{
    int data;
    Node leftChild;
    Node rightChild;

    public Node(int data){
        this.data = data;
    }
    public Node(int data, Node leftChild, Node rightChild) {
        this.data = data;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    public void insert(int element) {
        if (element < this.data) {
            // leaf node 인지 확인, 왼쪽 자식에 insert
            if (this.leftChild == null) {
                this.leftChild = new Node(element);
            } else {
                // leaf node가 아니면 타고 leaf node 까지 타고 내려감
                this.leftChild.insert(element);
            }
        }

        else if (element > this.data) {
            // leaf node 인지 확인, 오른쪽 자식에 insert
            if (this.rightChild == null) {
                this.rightChild = new Node(element);
            } else {
                // leaf node가 아니면 타고 leaf node 까지 타고 내려감
                this.rightChild.insert(element);
            }
        }
    }
}



public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void postOrder(Node node){
        if(node==null) return;
        postOrder(node.leftChild);
        postOrder(node.rightChild);
        System.out.println(node.data);

    }
    public static void main(String[] args) throws IOException {
        int rootData = Integer.parseInt(br.readLine());
        Node root = new Node(rootData);

        String input;
        while(true){
            input = br.readLine();
            if(input == null || input.isEmpty())
                break;

            root.insert(Integer.parseInt(input));
        }
        postOrder(root);
    }
}
