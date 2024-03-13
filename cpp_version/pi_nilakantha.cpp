#include <iostream>
#include <iomanip>
#include <boost/multiprecision/cpp_dec_float.hpp>

const unsigned int DECIMALES = 100;
typedef boost::multiprecision::cpp_dec_float<DECIMALES> veryLong;

int main() {
    std::cout << std::fixed << std::setprecision(DECIMALES);
    veryLong myFloat = veryLong("0.123456789123456789123456789123456789123456789");
    std::cout << myFloat.str(DECIMALES, std::ios_base::dec) << std::endl;
}