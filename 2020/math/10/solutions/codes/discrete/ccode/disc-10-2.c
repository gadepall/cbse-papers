#include <stdio.h>


long int f(int m,int n)
{
	if (n > 0)
	{
		return f(m,n-1);
	}
	else
		return 1;


}



int main()
{
int m = 12, n = 2, x, d = 10;

x = f(m,n);


printf("%d, %d, %ld, %ld,%ld",m,n,x, x/d, x%d );

return 0;
}


