C := g++
vector:
	g++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` _vector.cpp -o _vector`python3-config --extension-suffix`
clean:
	$(RM) _vector*.so
	rm -r __pycache__
test:
	pytest
