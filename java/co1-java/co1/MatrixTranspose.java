import java.util.*;

public class MatrixTranspose{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.print("Number of Columns :");
		int a = sc.nextInt();
		System.out.print("Number of Rows :");
		int b = sc.nextInt();
		System.out.println("Enter the matrix :");
		int mat1[][] = new int[25][25];
		int mat2[][] = new int[25][25];
		for(int i = 0; i < b; i++){
			for(int j = 0; j < a; j++){
				System.out.print(":-");
				mat1[i][j] = sc.nextInt();
			}
		}
		// Transposing
		for(int i = 0; i < b; i++){
			for(int j = 0; j < a; j++){
				mat2[i][j] = mat1[j][i];
			}
		}
		// Printing Matrix
		System.out.println("Matrix :-");
		for(int i = 0; i < b; i++){
			for(int j = 0; j < a; j++){
				System.out.print(mat1[i][j]+" ");
			}
			System.out.println("");
		}
		// Printing Transpose
		System.out.println("Transpose of Matrix 2:-");
		for(int i = 0; i < b; i++){
			for(int j = 0; j < a; j++){
				System.out.print(mat2[i][j]+" ");
			}
			System.out.println("");
		}
	}
}