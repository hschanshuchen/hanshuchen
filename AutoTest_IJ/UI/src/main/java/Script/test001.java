package Script;
import Common.BasicAction;
import Common.Login;
import Common.ReadFile;
import org.testng.annotations.*;

import java.io.IOException;
import java.util.logging.Logger;

/**
 * @ClassName test001
 * @Description  testCaseName ="正确导入文件",testCaseName ="Test002";
 * @date 2021/7/18 21:41
 * @Version 1.0
 */
public class test001 {

    public static Logger logger = Logger.getLogger(String.valueOf(test001.class));

    @BeforeMethod
    public void beforeMethod() {

        logger.info("开始执行用例预置条件");
        System.out.print(ReadFile.getConf("URL"));
        Login.login();
        BasicAction.sleep(10);
    }

    @Test
    public void run() {

        logger.info("开始执行用例步骤");
//        BasicAction.click("//input[@name='file']");
    }

    @AfterMethod
    public void afterMethod() {

        logger.info("开始清理环境");

        BasicAction.close();
    }
}
