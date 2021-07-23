package FileUpload;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;
public class Server {
    public static void main(String[] args) throws IOException {
        // 创建一个服务器ServerSocket对象，和系统要指定的端口号
        ServerSocket server = new ServerSocket(8888);
        while (true){
            // 使用ServerSocket对象中的accept方法，获取到请求客户端的Socket对象
            Socket socket = server.accept();
            new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        // 使用socket对象中的方法getInputStream()，获取网络字节输入流InputStream
                        InputStream is = socket.getInputStream();
                        File file = new File("d://upload");
                        if (!file.exists()){
                            file.mkdir();
                        }
                        String filename = "itcast"+System.currentTimeMillis()+new Random().nextInt(9999999)+".zip";
                        //
                        FileOutputStream fos = new FileOutputStream("d://upload//"+filename);
                        int len=0;
                        byte[] bytes = new byte[1024];
                        while ((len = is.read(bytes))!=-1){
                            fos.write(bytes,0,len);
                        }
                        socket.getOutputStream().write("上传成功".getBytes());
                        fos.close();
                        socket.close();
                    }
                    catch (IOException e){
                        System.out.println(e);
                    }
                }
            }).start();
        }
    }
}
