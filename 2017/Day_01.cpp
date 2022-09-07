#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class Solution
{
public:
    string readFile(ifstream &file)
    {
        string data = "";
        getline(file, data);
        return data; 
    }

    int part1(string *s){
        int sum = 0;
        for (int i = 1; i < (*s).length(); i++)
            sum += ((*s)[i] == (*s)[i - 1]) ? (*s)[i] - '0' : 0;

        if ((*s)[0] == (*s).back())
            sum += (*s)[0] - '0';

        return sum;
    }

    int part2(string *s) {
        int stop = (*s).length()/2; 
        int sum = 0; 

        for (int i = 0; i < stop; i++){
            sum += ((*s)[i] == (*s)[i+stop]) ? 2* ((*s)[i] - '0') : 0; 
        }
        return sum; 
    }
};

int main()
{

    Solution solution;

    ifstream MyReadFile("day1.txt");    // Read from the text file
    string Data = solution.readFile(MyReadFile); 

    string *pData = &Data;

    int part1 = solution.part1(pData); 
    cout << "Part 1: " << part1 << endl; 
    
    int part2 = solution.part2(pData);
    cout << "Part 2: " << part2 << endl; 
    return 0;
}