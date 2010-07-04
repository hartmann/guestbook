from net.grinder.script.Grinder import grinder
from net.grinder.script import Test

from no.bekk.webdriver import HomePageWebTest

class TestRunner:
    def __call__(self):
        grinder.statistics.delayReports = 1
        myTest = Test(1, "HomePage Grinder Test")
        jWebUnitTests = myTest.wrap(HomePageWebTest())

        jWebUnitTests.testThatApplicationIsUpAndRunning()
