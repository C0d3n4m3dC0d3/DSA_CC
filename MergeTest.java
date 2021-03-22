class MergeTest {
	private int[] merge(int[] arr1, int[] arr2) {
		int l1 = arr1.length;
		int l2 = arr2.length;

		int l3 = l1+l2;
		int[] arr3 = new int[l3];

		int i = 0, j = 0, k = 0;

		while(i < l1 && j < l2) {
			if(arr1[i] <= arr2[j]) {
				arr3[k] = arr1[i];
				i++;
			} else {
				arr3[k] = arr2[j];
				j++;
			}
			k++;
		}

		while(i < l1) {
			arr3[k] = arr1[i];
			i++;
			k++;
		}

		while(j < l2) {
			arr3[k] = arr2[j];
			j++;
			k++;
		}
		return arr3;
	}

	public void print(int[] x) {
		for(int val : x ) {
			System.out.print(val + " ");
		}
		System.out.println();
	}

	public static void main(String[] args) {
		MergeTest mt = new MergeTest();

		//size - 1, 1
		int[] a11 = {3};
		int[] a12 = {1};
		int[] a1 = mt.merge(a11, a12);
		mt.print(a1);

		//size - 2, 5
		int[] a21 = {2, 4};
		int[] a22 = {1, 5, 9, 12, 14};
		int[] a2 = mt.merge(a21, a22);
		mt.print(a2);

		//size - 3, 2
		int[] a31 = {4, 5, 6};
		int[] a32 = {2, 3, 5};
		int[] a3 = mt.merge(a31, a32);
		mt.print(a3);

		//size - 6,6
		int[] a41 = {1, 3, 5, 7, 7, 9};
		int[] a42 = {2, 4, 5, 6, 8, 9};
		int[] a4 = mt.merge(a41, a42);
		mt.print(a4);

		//size - 10, 5
		int[] a51 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		int[] a52 = {2, 4, 6, 8, 10};
		int[] a5 = mt.merge(a51, a52);
		mt.print(a5);
	}
}
