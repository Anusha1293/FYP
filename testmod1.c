#include<stdio.h>
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
int i,j,k;
for(i=0;i<m i++)
     for(j=0;j<n;j++)
     r[i][j]=a[i][j]+b[i][j];

}
void read(int a[10][10],int m,int n)
{
   int g,h;
   for(g=0;g<m;g++)
     for(h=0;h<n;h++)
     scanf("%d",&a[g][h]);
   
}


int main()
{
int m,n,p,q,mat1[10][10],mat2[10][10],res[10][10];
printf("enter order of mat 1 inte\n");
scanf("%d%d",&m,&n);
printf("entr order of mat2 \n");
scanf("%d%d",&p,&q);
if(m!=p || n!=q)
return 0;
read(mat1,m,n);
read(mat2,p,q);
add(mat1,mat2,res,m,n);
display(res,m,n);
}



