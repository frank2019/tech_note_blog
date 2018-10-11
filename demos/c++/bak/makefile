objects= a1.o main.o
a : $(objects)
	g++ -o a $(objects) 
main.o : main.cpp 
	g++ -c main.cpp
a1.o : a1.cpp 
	g++ -c a1.cpp
.PHONY : clean
clean :
	-rm -rf  a $(objects) 
