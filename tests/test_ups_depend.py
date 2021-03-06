#!/usr/bin/env python
'''
Test ups.depend
'''


root_dep = '''\
root v5_34_18d -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q e5:nu:prof
|__geant4 v4_9_6_p03b -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q e5:prof
|  |__clhep v2_1_4_1 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q e5:prof
|  |  |__gcc v4_8_2 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products
|  |__xerces_c v3_1_1a -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q e5:prof
|  |__g4emlow v6_32 -f NULL -z /afs/rhic.bnl.gov/lbne/software/products
|  |__g4neutron v4_2 -f NULL -z /afs/rhic.bnl.gov/lbne/software/products
|  |__g4neutronxs v1_2 -f NULL -z /afs/rhic.bnl.gov/lbne/software/products
|  |__g4nucleonxs v1_1 -f NULL -z /afs/rhic.bnl.gov/lbne/software/products
|  |__g4photon v3_0 -f NULL -z /afs/rhic.bnl.gov/lbne/software/products
|  |__g4pii v1_3 -f NULL -z /afs/rhic.bnl.gov/lbne/software/products
|  |__g4radiative v4_0 -f NULL -z /afs/rhic.bnl.gov/lbne/software/products
|  |__g4surface v1_0 -f NULL -z /afs/rhic.bnl.gov/lbne/software/products
|__fftw v3_3_3 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q prof
|__gsl v1_16 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q prof
|__pythia v6_4_28a -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q gcc482:prof
|__postgresql v9_1_12 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products
|  |__python v2_7_6 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products
|     |__sqlite v3_08_03_00 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products
|__mysql_client v5_5_36 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q e5
|__libxml2 v2_9_1 -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q prof
|__xrootd v3_3_4a -f Linux64bit+2.6-2.12 -z /afs/rhic.bnl.gov/lbne/software/products -q e5:prof
'''

from ups.depend import parse

def test_parse_root():
    graph = parse(root_dep)
    assert 22 == len(graph.nodes())
    assert 21 == len(graph.edges())

def test_correct():
    graph = parse(root_dep)

    for n in graph.nodes():
        if n.name == 'root':
            assert n.version == 'v5_34_18d'
            deps = graph[n]
            assert 8 == len(deps)



