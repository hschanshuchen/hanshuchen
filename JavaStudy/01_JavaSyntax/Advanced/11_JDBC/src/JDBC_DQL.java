import java.sql.*;

public class JDBC_DQL {
    /*
    执行DQL语句，返回执行结果，返回类型为int
    url:数据库url，如"jdbc:mysql://localhost:3306/db3"
    usernam:数据库账号
    password:数据库密码
    sql：sql语句，查询语句
    */
    public static void connetDbAndExeuteDQL(String url, String username, String password, String sql){
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection(url, username, password);
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            rs = stmt.executeQuery(sql);
            //6.处理结果
            //6.1 让游标向下移动一行
            rs.next();
            //6.2 获取数据
            int id = rs.getInt(1);
            String name = rs.getString("name");
            double balance = rs.getDouble(3);
            System.out.println(id + "---" + name + "---" + balance);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
