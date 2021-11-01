from Tests.testDomain import testCheltuiala
from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuiala, testModificaCheltuiala
from Tests.testFunctionalitati import testAdaugaLaSuma

def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuiala()
    testModificaCheltuiala()
    testAdaugaLaSuma()