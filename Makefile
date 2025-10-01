all:
	g++ -std=c++17 -o refabbr main.cpp -O3 -static-libstdc++

clean:
	rm -f refabbr
	rm -f *.o
