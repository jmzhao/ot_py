import tableau as tb
import cd
import fred
import os.path

t = tb.tableau()

def test(fname) :
    print('-----test for "%s"------'%fname)
    try :
        t.readFile(fname)
        ercs = fred.erc.get_ERClist(t)
        print('ERCs:', *ercs, sep='\n')
        fredans = fred.FRed(ercs)
        print('MIB:', *fredans.MIB, sep='\n')
        print('SKB:', *fredans.SKB, sep='\n')
        root, ext = os.path.splitext(fname)
        fred.hasse.hasse(t, fredans.SKB).write(root+'.png', format='png')
        print(cd.toString(cd.ConstraintsDemotion(t)))
    except tb.InputError as e :
        print('Error when reading file:', e)
    except (cd.UnsatisfiableError, fred.UnsatisfiableError) as e :
        print('Error when processing:', e)

test('''.\InputFiles\Ilokano.txt''')
test('''.\InputFiles\contradiction.txt''')
test('''.\InputFiles\HarmonicallyBounded.txt''')
test('''.\InputFiles\Hebrew.txt''')