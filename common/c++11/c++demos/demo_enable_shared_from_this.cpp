#include <memory>
#include <iostream>

struct Good :std::enable_shared_from_this<Good>
{
    ~Good() { std::cout << "Good::~Good() calld" << std::endl; }
};

int main(int argc, char **argv) {
    {
        std::shared_ptr<Good> gp1(new Good());
        std::shared_ptr<Good> gp2 = gp1->shared_from_this();

        std::cout << "gp1.use_count()=" << gp1.use_count() << std::endl;
        std::cout << "gp2.use_count()=" << gp2.use_count() << std::endl;
    }
    system("pause");
}