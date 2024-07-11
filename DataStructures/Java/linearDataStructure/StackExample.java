package linearDataStructure;

import java.util.Stack;

public class StackExample {

	public static void main(String[] args) {
		Stack<Integer> stack = new Stack<>();
		stack.push(1);
		stack.push(2);
		stack.push(3);
		stack.push(4);
		
		System.out.println("Top element: " + stack.peek());
		System.out.println("Stack size: " + stack.size());
		
		while (!stack.isEmpty()) {
			System.out.println("Popped element: " + stack.pop());
		}

	}

}
