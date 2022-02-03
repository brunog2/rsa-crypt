#include <stdio.h>

int modInverse(int a, int m) 
{ 
    a = a%m; 
    for (int x=1; x<m; x++) 
       if ((a*x) % m == 1) 
          return x;
}

int descriptografar(int d, int k)
{
    int n;
    int resultado, pot;
    scanf("%d", &n);
    pot = n % d;
    resultado = 1;
    for( ; k > 0; k /= 2)
    {
        if (k % 2 == 1)
        {
            resultado = (resultado * pot) % d;
        }
            pot = (pot * pot) % d;
        
    }
    return resultado;
}

int main()
{
    int k, d;
    int p, q, e;
    int res;
    char alfabeto[28] = " abcdefghijklmnopqrstuvwxyz ";
    scanf("%d %d", &p, &q);
    scanf("%d", &e);
    d = p*q;
    k = modInverse(e, ((p-1)*(q-1)));
    for(int i = 1; i < 50; i++)
    {
        res = descriptografar(d, k);
        printf("%c", alfabeto[res-1]);
    }
    printf("\n");
    return 0;
}
