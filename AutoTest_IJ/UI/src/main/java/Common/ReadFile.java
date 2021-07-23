package Common;

import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;

import java.io.*;
import java.util.Iterator;
import java.util.Properties;

/**
 * @ClassName ReadFile
 * @Description TODO
 * @date 2021/7/20 5:29
 * @Version 1.0
 */
public class ReadFile {

    /**
     * @param key
     * @return String
     * @Description 获取config.properties中的值
     * @author hanshuchen
     * @date 2021/7/20 1:28
     */
    public static String getConf(String key) {
        Properties p = new Properties();
        try {
            InputStream in = new BufferedInputStream(new FileInputStream(System.getProperty("user.dir") + "\\src\\config.properties"));
            p.load(in);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return p.getProperty(key);
    }

    /**
     * @param key
     * @return String
     * @Description 获取xml文件中节点值
     * @author hanshuchen
     * @date 2021/7/20 9:31
     */
    public static String getXml(String key) throws DocumentException {
        //1.创建SAXReader对象用于读取xml文件
        SAXReader reader = new SAXReader();
        //2.读取xml文件，获得Document对象
        Document doc = reader.read(new File(System.getProperty("user.dir") + "\\UI\\src\\main\\resources\\fromData\\a.xml"));
        //3.获取根元素
        Element root = doc.getRootElement();
        //4.获取根元素下的所有子元素（通过迭代器）
        Iterator<Element> it = root.elementIterator();
        String xmlValue = null;
        while (it.hasNext()) {
            Element e = it.next();
            //获取标签名
            String tagName = e.getName();
            if (tagName.equals(key.split("\\.", 2)[0])) {
                Element value = e.element(key.split("\\.", 2)[1]);
                xmlValue = value.getStringValue();
            }
        }
        return xmlValue;
    }

    /**
     * @param sheetName
     * @param rowName
     * @param rolName
     * @return String
     * @Description 获取excel中指定单元格的值
     * @author hanshuchen
     * @date 2021/7/20 9:32
     */
    public static String getExcel(String sheetName, String rowName, String rolName) {
        String cellValue = null;
        try {
            //创建工作簿
            XSSFWorkbook xssfWorkbook = new XSSFWorkbook(new FileInputStream("D:\\AutoTest_IJ\\UI\\src\\main\\resources\\fromData\\test.xlsx"));
            //读取指定工作表
            XSSFSheet sheet = xssfWorkbook.getSheet(sheetName);
            // 计算需要求得单元格在第几列
            int rolNum = 0;
            int maxRol = sheet.getRow(0).getLastCellNum();
            for (int i = 0; i < maxRol; i++) {
                if ((sheet.getRow(0).getCell(i)).toString().equals(rolName)) {
                    rolNum = i;
                }
            }
            //获取最后一行的num，即总行数。此处从0开始计数
            int maxRow = sheet.getLastRowNum();
            for (int row = 0; row <= maxRow; row++) {
                if (sheet.getRow(row).getCell(0).toString().equals(rowName)) {
                    cellValue = sheet.getRow(row).getCell(rolNum).toString();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return cellValue;
    }
}

