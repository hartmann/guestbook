from net.grinder.script.Grinder import grinder
from net.grinder.script import Test

from no.bekk.webdriver import HomePageWebTest

class TestRunner:
    def __call__(self):
        test1 = Test(1, "HomePage Grinder Test")
        jWebUnitTests = test1.wrap(HomePageWebTest())

        jWebUnitTests.testThatApplicationIsUpAndRunning()

        test2 = Test(2, "HomePage Grinder Test 2")
        webtest2 = test2.wrap(HomePageWebTest())
        webtest2.test2()
