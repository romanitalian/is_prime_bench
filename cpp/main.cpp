#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

bool isPrime(int num)
{
    if (num == 2) {
        return true;
    }
    if (num <= 1 || num % 2 == 0) {
        return false;
    }

    double sqrt_num = sqrt(double(num));
    for (int div = 3; div <= sqrt_num; div +=2)
    {
        if (num % div == 0) {
            return false;
        }
    }
    return true;
}

// g++ cpp/main.cpp -o cpp/is_prime && ./cpp/is_prime
// 2.59483 sec
int main()
{
    int N = 10000000;
    clock_t start, end;
    start = clock();
    for (int i ; i < N; i++) {
        // printf("%d - %d\n", i, isPrime(i));
        isPrime(i);
    }
    end = clock();
    cout << (end - start) / ((double) CLOCKS_PER_SEC);
    cout << " sec \n";
    return 0;
}
