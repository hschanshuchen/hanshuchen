import java.sql.*;

public class JDBC_DDM_DDL {
    /*
    执行DDM和DDl语句，返回执行结果，返回类型为int
    url:数据库url，如"jdbc:mysql://localhost:3306/db3"
    usernam:数据库账号
    password:数据库密码
    sql：sql语句，增删改，数据库操作，表操作，如"update a set b=2 where id=1"
    */
    public static void connetDBAndExeuteDMLAndDDl(String url, String username, String password, String sql) {
        Connection conn = null;
        Statement stmt = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            int count = stmt.executeUpdate(sql);
            //6.处理结果
            System.out.println(count);
            if (count > 0) {
                System.out.println("修改成功！");
            } else {
                System.out.println("修改失败");
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源
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
