package Common;

import Script.test001;
import org.dom4j.Attribute;
import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.*;
import java.util.Iterator;
import java.util.Properties;
import java.util.logging.Logger;


/**
 * @ClassName basicAction
 * @Description 页面元素操作相关方法，读取配置文件相关方法
 * @date 2021/7/18 4:57
 * @Version 1.0
 */
public class BasicAction {
    public static Logger logger = Logger.getLogger(String.valueOf(test001.class));
    public static WebDriver driver = new FirefoxDriver();

    /**
     * @param
     * @return WebDriver
     * @Description
     * @author hanshuchen
     * @date 2021/7/18 5:42
     */
    public static WebDriver getDiver() {
        return driver;
    }

    /**
     * @param
     * @return WebDriver
     * @Description
     * @author hanshuchen
     * @date 2021/7/18 21:55
     */
    public static WebDriver sleep(int n) {
        try {
            Thread.sleep(1000 * n);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return driver;
    }

    /**
     * @param
     * @return void
     * @Description
     * @author hanshuchen
     * @date 2021/7/18 22:12
     */
    public static void close() {
        driver.close();
    }

    /**
     * @param
     * @return void
     * @Description
     * @author hanshuchen
     * @date 2021/7/18 22:12
     */
    public static void quit() {
        driver.quit();
    }

    /**
     * @param url
     * @return void
     * @Description
     * @author hanshuchen
     * @date 2021/7/18 5:43
     */
    public static void openUrl(String url) {
        driver.manage().window().maximize();
        driver.get(url);

    }

    /**
     * @param xpath
     * @return WebElement
     * @Description 动态等待定位元素
     * @author hanshuchen
     * @date 2021/7/18 3:46
     */
    public static WebElement find(String xpath) {
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement ele = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(xpath)));
        return ele;
    }

    /**
     * @param xpath
     * @param value
     * @return void
     * @Description 输入框输入
     * @author hanshuchen
     * @date 2021/7/18 3:47
     */
    public static void send(String xpath, String value) {
        find(xpath).sendKeys(value);
    }

    /**
     * @param xpath
     * @return void
     * @Description 点击元素
     * @author hanshuchen
     * @date 2021/7/18 3:47
     */
    public static void click(String xpath) {
        find(xpath).click();
    }

    /**
     * @param xpath
     * @return void
     * @Description 获取元素文本值
     * @author hanshuchen
     * @date 2021/7/18 3:47
     */
    public static void getText(String xpath) {
        find(xpath).getText();
    }

    /**
     * @param xpath
     * @param attribute
     * @return void
     * @Description 获取元素属性值
     * @author hanshuchen
     * @date 2021/7/18 3:47
     */
    public static void getAttribute(String xpath, String attribute) {
        find(xpath).getAttribute(attribute);
    }
}
