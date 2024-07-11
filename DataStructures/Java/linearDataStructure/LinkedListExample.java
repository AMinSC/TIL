package linearDataStructure;

class Node<T> {
	T data;
	Node<T> next;
	
	public Node(T data) {
		this.data = data;
		this.next = null;
	}
}

public class LinkedListExample<T> {
	Node<T> head;

	public void insert(T data) {
		Node<T> newNode = new Node<>(data);
		if (head == null) {
			head = newNode;
		} else {
			Node<T> temp = head;
			while (temp.next != null) {
				temp = temp.next;
			}
			temp.next = newNode;
		}
	}
	
	public void delete(T data) {
		if (head == null) return;
		
		if (head.data == data) {
			head = head.next;
			return;
		}
		
		Node<T> temp = head;
		while (temp.next != null && temp.next.data != data) {
			temp = temp.next;
		}
		
		if (temp.next != null) {
			temp.next = temp.next.next;
		}
	}
	
	public boolean search(T data) {
		Node<T> temp = head;
		while (temp != null) {
			if (temp.data == data) {
				return true;
			}
			temp = temp.next;
		}
		return false;
	}
	
	public void display() {
		Node<T> temp = head;
		while (temp != null) {
			System.out.println(temp.data + " ");
			temp = temp.next;
		}
	}
	
	public static void main(String[] args) {
		LinkedListExample<Integer> list = new LinkedListExample();
		list.insert(1);
		list.insert(2);
		list.insert(3);
		list.insert(4);
		
		System.out.println("List after insertion: ");
		list.display();
		
		list.delete(3);
		System.out.println("List after deletion of 3: ");
		list.display();
		
		System.out.println("Search for 2: " + list.search(2));
		System.out.println("Search for 3: " + list.search(3));

		LinkedListExample<String> stringList = new LinkedListExample<>();
        stringList.insert("Hello");
        stringList.insert("World");
        stringList.insert("Java");
        stringList.insert("Generics");

        System.out.print("String List after insertion: ");
        stringList.display();

        stringList.delete("Java");
        System.out.print("String List after deletion of Java: ");
        stringList.display();

        System.out.println("Search for World in String List: " + stringList.search("World"));
        System.out.println("Search for Java in String List: " + stringList.search("Java"));
	}

}
