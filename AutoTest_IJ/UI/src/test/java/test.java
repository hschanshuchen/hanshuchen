

import Common.ReadFile;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.dom4j.DocumentException;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;


public class test {


	public static void main(String[] args) throws DocumentException {

		System.out.println(ReadFile.getExcel("Sheet2", "test008", "测试数据"));
		;
	}
}




