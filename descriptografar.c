#include <stdio.h>

int modInverse(int a, int m) //Função para encontrar o segundo numero da Chave Privada(inverso modular).
{ 
    a = a%m; 
    for (int x=1; x<m; x++) 
       if ((a*x) % m == 1) 
          return x;
}

int descriptografar(int d, int k) //Função que recebe a Chave Privada e o Codigo criptografado e descriptografa.
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
    char alfabeto[28] = " abcdefghijklmnopqrstuvwxyz "; //Alfabeto que o professor pediu. A = 2, B = 3... Z = 27, espaço = 28.
    scanf("%d %d", &p, &q);
    scanf("%d", &e);
    d = p*q; // d = primeiro numero da chave privada.
    k = modInverse(e, ((p-1)*(q-1))); // k = segundo numero da chave privada.
    for(int i = 1; i < 50; i++)//for final pra receber e descriptografar todos os numeros.
    {
        res = descriptografar(d, k);
        printf("%c", alfabeto[res-1]); //recebe o numero inteiro da função, e busca no alfabeto da linha 35 o numero correspondente.
    }
    printf("\n");
    return 0;
}
//formato de entrada por arquivo:
// p q e
// codigo criptografado
