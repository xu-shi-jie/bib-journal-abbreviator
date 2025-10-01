all:
	g++ -std=c++17 -o refabbr main.cpp -O3 -static

clean:
	rm -f refabbr
	rm -f *.o
