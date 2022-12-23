<?php
// 连接数据库
function connect($user, $pass, $dbname, &$error, $host = 'localhost', $post = '3306', $charset = 'utf8')
{
    $conn = mysqli_connect($host, $user, $pass, $dbname, $post);
    if (!$conn) {
        $error = mysqli_connect_error();
        return false;
    }
    if (!mysqli_set_charset($conn, $charset)) {
        $error = mysqli_error($conn);
        return false;
    }
    return $conn;
}
//执行语句
function query($conn, $sql, &$error)
{
    $res = mysqli_query($conn, $sql);
    if ($res === false) {
        $error = mysqli_error($conn);
        return false;
    }
    return $res;
}

function read($conn, $sql, &$error, $all = false)
{
    $res = query($conn, $sql, $error);
    if ($res === false) {
        return false;
    }
    $lists = [];
    if ($all) {
        while ($row = mysqli_fetch_assoc($res)) {
            $lists[] = $row;
        }
    } else {
        $lists = mysqli_fetch_assoc($res);
    }
    mysqli_free_result($res);
    return $lists;
}

function auto_update($conn, $data, $table, &$error, $id = 0)
{
    $set = '';
    foreach ($data as $k => $v) {
        $set .= $k . "='{$v}',";
    }
    $set = rtrim($set, ',');    // title='title',content='content'
    $sql = "UPDATE {$table} SET {$set} ";
    if ($id) {
        $sql .= ' WHERE `id` = ' . $id;
    }
    if (query($conn, $sql, $error)) {
        return mysqli_affected_rows($conn);
    } else {
        return false;
    }
}

function auto_read($conn, $table, &$error, $where = [], $all = false)
{
    # 组装查询条件：默认永远为真
    $where_clause = ' where 1 ';    # where 1
    if ($where) {        # 空数组自动转换成布尔false
        # 解析条件
        foreach ($where as $k => $v) {
            $where_clause .= ' and ' . $k . " = '$v' ";
        }  # where 1 and title = 'news' ...
    }

    # 组织完整SQL
    $sql = "select * from {$table} {$where_clause}";
    $res = query($conn, $sql, $error);

    # 判定执行结果
    if ($res === false) return $res;

    # 判定获取一条还是多条
    $lists = [];
    if ($all) {
        # 获取多条，二维数组存储
        while ($row = mysqli_fetch_assoc($res)) {
            $lists[] = $row;
        }
    } else {
        # 获取一条，一维数组存储
        $lists = mysqli_fetch_assoc($res);
    }

    # 释放资源，返回结果
    mysqli_free_result($res);
    return $lists;
}
