//Access array elements using pointers

#include <stdio.h>
int arr[5];
int main(){
    for(int i=0;i<5;i++){
        scanf("%d",(arr+i));
    }

    printf("The elements of the array: \n");
    for(int i=0;i<5;i++){
        printf("%d\n",*(arr+i));
    }

    return 0;

}
