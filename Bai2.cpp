#include <stdio.h>
#include <math.h>

// Hàm kiểm tra số chính phương
int isPerfectSquare(int num) {
    int squareRoot = sqrt(num);
    return (squareRoot * squareRoot == num);
}

// Hàm đếm và in ra các số chính phương nhỏ hơn n
void countAndPrintPerfectSquares(int n) {
    printf("Cac so chinh phuong nho hon %d la:\n", n);
    int count = 0;
    for (int i = n - 1; i > 0; i--) {
        if (isPerfectSquare(i)) {
            printf("%d ", i);
            count++;
        }
    }
    printf("\nTong so chinh phuong: %d\n", count);
}

int main() {
    int n;
    printf("Nhap vao mot so nguyen duong: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Nhap khong hop le. Vui long nhap lai so nguyen duong.\n");
        return 1;
    }

    countAndPrintPerfectSquares(n);

    return 0;
}

