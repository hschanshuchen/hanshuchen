package Common;

import java.io.IOException;

/**
 * @ClassName Login
 * @Description TODO
 * @date 2021/7/18 3:56
 * @Version 1.0
 */
public class Login {

    /**
     * @param
     * @return void
     * @Description
     * @author hanshuchen
     * @date 2021/7/18 5:44
    */
    public static void login()  {
        String url= ReadFile.getConf("URL");
        System.out.print(url);
        BasicAction.openUrl(ReadFile.getConf("URL"));
    }
}
