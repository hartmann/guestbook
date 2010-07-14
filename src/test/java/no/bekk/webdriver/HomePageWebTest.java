package no.bekk.webdriver;

import junit.framework.TestCase;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;

/**
 * Created by IntelliJ IDEA.
 * User: Vegard Hartmann
 * Date: 03.jul.2010
 * Time: 17:44:02
 * To change this template use File | Settings | File Templates.
 */
public class HomePageWebTest extends TestCase {


    @Test
    public void testThatApplicationIsUpAndRunning() {
        WebDriver driver = new HtmlUnitDriver();
        driver.get("http://localhost:8080/guestbook/");
        driver.quit();
    }

    @Test
    public void test2() {
        System.out.println("This is test 2");
    }
}
