objects= a1.o main.o
a : $(objects)
	g++ -o a $(objects) 

%.o:%.c %.h
	g++ -c -o $@ $<
.PHONY : clean
clean :
	-rm -rf  a $(objects) 
