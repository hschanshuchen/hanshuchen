package FileUpload;
import java.io.*;
import java.net.Socket;

public class Client {
    public static void main(String[] args) throws IOException {
        // 创建一个本地字节输入流FileInputStream对象，构造方法中绑定要读取的数据源
        FileInputStream fis = new FileInputStream("D://poi-bin-4.1.2-20200217.zip");
        // 创建一个客户端Socket对象，构造方法中绑定IP和端口号
        Socket socket = new Socket("127.0.0.1",8888);
        // 使用Socket中的getOutputStream方法，获取网络字节输出流OutputStream
        OutputStream os = socket.getOutputStream();
        // 使用本地字节输入流FileInputStream对象中的方法read，读取本地文件
        int len=0;
        byte[] bytes = new byte[1024];
        while ((len = fis.read(bytes))!=-1){
            // 使用OutputStream中的weite方法，把读取到的文件上传到服务器
            os.write(bytes,0,len);
        }
        socket.shutdownOutput();
        // 使用Socket中的getInputStream方法，获取网络字节输入流InputStream
        InputStream is = socket.getInputStream();
        while ((len = is.read(bytes))!=-1){
            System.out.println(new String(bytes,0,len));
        }
        // 释放资源
        fis.close();
        socket.close();
    }
}
