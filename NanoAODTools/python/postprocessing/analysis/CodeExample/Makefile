include Makefile.arch

ROOTCFLAGS    = $(shell $(ROOTSYS)/bin/root-config --cflags)
ROOTLIBS      = $(shell $(ROOTSYS)/bin/root-config --libs)
ROOTGLIBS     = $(shell $(ROOTSYS)/bin/root-config --glibs)

#######################################
# -- DEFINE ARCH to something sensible!
#######################################
 
#
CXX           = g++
CXXFLAGS      = -g -Wall -fPIC
LD            = g++
LDFLAGS       = -g
SOFLAGS       = -shared


CXXFLAGS      += $(ROOTCFLAGS)
LIBS           = $(ROOTLIBS) 

NGLIBS         = $(ROOTGLIBS) 
NGLIBS        += -lMinuit
GLIBS          = $(filter-out -lNew, $(NGLIBS))

example: example.o mt2w.o mt2w_bisect.o topness.o JetUtil.o
	$(LD) $(LDFLAGS) $(GLIBS) -o example example.o mt2w.o mt2w_bisect.o topness.o JetUtil.o

mt2w.o: mt2w.cc mt2w.h mt2w_bisect.h JetUtil.h
	$(CXX) $(CXXFLAGS) -c mt2w.cc

mt2w_bisect.o:  mt2w_bisect.cpp mt2w_bisect.h 
	$(CXX) $(CXXFLAGS) -c mt2w_bisect.cpp

topness.o: topness.cc topness.h JetUtil.h
	$(CXX) $(CXXFLAGS) -c topness.cc

JetUtil.o: JetUtil.cc JetUtil.h
	$(CXX) $(CXXFLAGS) -c JetUtil.cc

example.o: example.cc example.h mt2w.h mt2w_bisect.h topness.h JetUtil.h 
	$(CXX) $(CXXFLAGS) -c example.cc



.PHONY: clean
clean:  
	rm -v -f \
	*.o *.d *.so; echo "Done"
