#include <stdio.h>

int main()
{
    int arr[100],a,i;
   
for(i=0;i>=0;i++)
{
        scanf("%d",&a);
        if(a>0)
{
arr[i]=a;
a=0;
}
else
{
break;
}
}

for(int j=0;j<i;j++)
{
a=0;
if(arr[j]<100 && arr[j]>a)
{
a=arr[j];
}
}

printf("%d",a);


    return 0;
}