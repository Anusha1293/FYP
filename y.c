#include<stdio.h>
void display(int b[10][10],int m, int n);
void add(int a[10][10],int b[10][10],int r[10][10],int m,int n);
void read(int a[10][10],int m,int n);


void display(int b[10][10],int m, int n)
{
int i,j;
for(i=0;i<m;i++)


{
for(j=0;j<n;j++)
printf("%d\t",b[i][j]);
printf("\n");
}
}


void add(int a[10][10],int b[10][10],int r[10][10],int m,int n)
{
int i,j;
for(i=0;i<m;i++)
     for(j=0;j<n;j++)
     r[i][j]=a[i][j]+b[i][j];

}
void read(int a[10][10],int m,int n)
{
   int i,j;
   for(i=0;i<m;i++)
     for(j=0;j<n;j++)
     scanf("%d",&a[i][j]);



}

int main()
{
int m=2,n=2,p=2,q=2,res[10][10],i,j,mat1[10][10],mat2[10][10];
mat1[0][0]=2;
mat1[0][1]=3;
mat1[1][0]=4;
mat1[1][1]=5;
mat2[0][0]=6;
mat2[0][1]=7;
mat2[1][0]=8;
mat2[1][1]=9;
//printf("enter order of mat 1\n");
//scanf("%d%d",&m,&n);
//printf("entr order of mat2 \n");
//scanf("%d%d",&p,&q);
//if(m!=p || n!=q)
//return 0;
//read(mat1,m,n);
//read(mat2,p,q);
add(mat1,mat2,res,m,n);
display(res,m,n);
}

