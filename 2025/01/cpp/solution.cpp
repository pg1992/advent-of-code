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
        if (dir == 'R')
        {
            // for loop is the worst solution... but solves part 2
            for (int i = 0; i < num; i++)
            {
                pos = (pos + 1) % 100;
                if (pos == 0)
                    count_cross++;
            }
        }
        else
        {
            for (int i = 0; i < num; i++)
            {
                pos = ((pos - 1) % 100 + 100) % 100;
                if (pos == 0)
                    count_cross++;
            }
        }
        if (pos == 0)
            count++;
    }

    fin.close();

    std::cout << count << '\n';
    std::cout << count_cross << '\n';

    return 0;
}
