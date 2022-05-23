import unittest
from package1.TC_LoginTest import LoginTest
from package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import paymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnTest

# Get all the tests from LoginTest,SignUpTest,PaymentTest and PaymentReturnTest
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

#creating test suite
sanitytestsuite=unittest.TestSuite([tc1,tc2])   # sanity test suite
functionalTestSuite=unittest.TestSuite([tc3,tc4])
masterTestsuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(sanitytestsuite)
# unittest.TextTestRunner(verbosity=2).run(functionalTestSuite)
# unittest.TextTestRunner(verbosity=2).run(masterTestsuite)


