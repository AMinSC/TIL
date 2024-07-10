package linearDataStructure;

public class ArrayExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] intArray = new int[5];
		intArray[0] = 1;
		intArray[1] = 2;
		intArray[2] = 3;
		intArray[3] = 4;
		intArray[4] = 5;
		
		for (int i = 0; i < intArray.length; i++) {
			System.out.println("Element at index" + i + ": " + intArray[i]);
		}
	}
}
