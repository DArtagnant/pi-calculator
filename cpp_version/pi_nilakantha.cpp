#include <iostream>
#include <iomanip>
#include <boost/multiprecision/cpp_dec_float.hpp>

const unsigned int DECIMALES = 10000;
using VeryLong = boost::multiprecision::number<boost::multiprecision::cpp_dec_float<DECIMALES>>;

VeryLong pi_nilakantha(VeryLong reps) {
    VeryLong approx = 3;
    int sign = 1;
    for (VeryLong n = 2; n * 2 <= reps; n += 2) {
        approx += sign * 4 / (n * (n + 1) * (n + 2));
        sign *= -1;
    }
    return approx;
}

int main() {
    std::cout << std::fixed << std::setprecision(DECIMALES);
    VeryLong approx_pi = pi_nilakantha(VeryLong("100000"));
    std::cout << approx_pi.str(DECIMALES, std::ios_base::dec) << std::endl;
}