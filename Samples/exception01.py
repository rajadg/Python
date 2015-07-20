

class ForceQuitError(StandardError) :
    '''
        This error is raised when the sync operation is forcibly stopped from outside
    '''
    def __init__(self):
        # No details available for this exception
        print "About to raise a ForceQuitError"
        pass
    

def test01() :
    raise ForceQuitError()

def test02():
    try:
        print "Invoking test01 ..."
        test01()
    except ForceQuitError as e:
        print "caught in test02(): " + str(type(e))
        raise
    return


def test03():
    try:
        print "Invoking test02 ..."
        test02()
    except ForceQuitError, e:
        print "caught in test03(): " + str(type(e))
        pass
    return

test03()
print "End ....\n"
