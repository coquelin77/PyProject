#include<stdio.h>
void main()
{
	int s[12]={1,2,3,4,4,3,2,1,1,1,2,3};
	int c[5]={0};
	for (int i = 0; i < 12; i++)
	{
		c[s[i]]++;
	}
	for (int i = 1; i < 5; i++)
	{
		printf("%d",c[i] );
	}
	printf("\n");
}