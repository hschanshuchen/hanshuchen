package BS;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) throws IOException {
        // 创建一个服务器，指定端口号
        ServerSocket server = new ServerSocket(8888);
        while (true){
            // 获取请求客户端对象
            Socket socket = server.accept();
            new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        InputStream is = socket.getInputStream();
                        // 把is网络字节输入流对象，转换为字符缓冲输入流
                        BufferedReader br = new BufferedReader(new InputStreamReader(is));
                        // 把客户端请求信息的第一行读取出来
                        String line = br.readLine();
                        // 把路径前边的/去掉,进行截取07_Net/web/index.html HTTP/1.1
                        String[] arr = line.split(" ");
                        String htmlpath = arr[1].substring(1);
                        // 创建一个本地字节输入流，构造方法中绑定读取的html路径
                        FileInputStream fis = new FileInputStream(htmlpath);
                        // 使用socket中的方法getOutputStream获取网络字节输出流OutputStream
                        OutputStream os = socket.getOutputStream();
                        // http中的固定写法
                        os.write("HTTP/1.1 200 ok\r\n".getBytes());
                        os.write("Content-Type:text/html\r\n".getBytes());
                        os.write("\r\n".getBytes());

                        int len=0;
                        byte[] bytes = new byte[1024];
                        while ((len = fis.read(bytes))!=-1){
                            os.write(bytes,0,len);
                        }
                        fis.close();
                        socket.close();

                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }).start();
        }
    }
}
