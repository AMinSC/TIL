package linearDataStructure;

class Node {
	int data;
	Node next;
	
	public Node(int data) {
		this.data = data;
		this.next = null;
	}
}

public class LinkedListExample {
	Node head;

	public void insert(int data) {
		Node newNode = new Node(data);
		if (head == null) {
			head = newNode;
		} else {
			Node temp = head;
			while (temp.next != null) {
				temp = temp.next;
			}
			temp.next = newNode;
		}
	}
	
	public void display() {
		Node temp = head;
		while (temp != null) {
			System.out.println(temp.data + " ");
			temp = temp.next;
		}
	}
	
	public static void main(String[] args) {
		LinkedListExample list = new LinkedListExample();
		list.insert(1);
		list.insert(2);
		list.insert(3);
		list.insert(4);
		
		list.display();

	}

}
