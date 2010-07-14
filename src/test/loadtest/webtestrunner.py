from net.grinder.script.Grinder import grinder
from net.grinder.script import Test

from no.bekk.webdriver import HomePageWebTest

class TestRunner:

    def __init__(self):
        self.originalWebtest = HomePageWebTest()

    def __call__(self):
        # Turn off automatic reporting for the current worker thread.
        # Having done this, the script can modify or set the statistics
        # before they are sent to the log and the console.
        grinder.statistics.delayReports = 1

        log = grinder.logger.output
        out = grinder.logger.TERMINAL

        testMethods = ["testThatApplicationIsUpAndRunning", "test2", ]

        testNumber = 0
        for test in testMethods:
            log(test, out)
            testNumber += 1
            testCase = Test(testNumber, test).wrap(self.originalWebtest)
            getattr(testCase, test)()


