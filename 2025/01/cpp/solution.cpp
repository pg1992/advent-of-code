#include <fstream>
#include <iostream>

int main()
{
    std::ifstream fin("../input");
    char dir {};
    int num {};
    int pos { 50 };
    int count { 0 };
    int count_cross { 0 };

    while (fin >> dir >> num)
    {
        int old_pos { pos };
        int revs { num / 100 };
        int rem { num % 100 };

        count_cross += revs;

        if (dir == 'R')
        {
            if (pos + rem >= 100)
                count_cross++;
            pos = (pos + rem) % 100;
        }
        else
        {
            if (pos - rem <= 0)
                count_cross++;
            pos = ((pos - rem) % 100 + 100) % 100;  // positive modulo
        }
        if (pos == 0)
            count++;
    }

    fin.close();

    std::cout << count << '\n';
    std::cout << count_cross << '\n';

    return 0;
}
