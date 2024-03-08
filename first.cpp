#include <iostream>
#include <chrono>
#include <ctime>

using namespace std;

static bool isEven(int value)
{
    return not (value % 2);
}

static bool isEven_v2(int value)
{
    return not (1 & value);
}


static void test_isEven() 
{
    auto start = chrono::system_clock::now();

    for (int i = 0; i < 100000000; i++) {
        isEven(i);
    }

    auto end = chrono::system_clock::now();
    chrono::duration<double> sec = end - start; cout << "time with %: " << sec.count() << "\n";


    start = chrono::system_clock::now();

    for (int i = 0; i < 100000000; i++) {
        isEven_v2(i);
    }

    end = chrono::system_clock::now();
    sec = end - start; cout << "time with &: " << sec.count();
}


int main()
{
    test_isEven();

    return 0;
}
