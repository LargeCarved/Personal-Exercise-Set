<?php
$link = @mysqli_connect('localhost', 'root', 'a1592648', 'student01', '3306');
if (!$link) {
    exit(mysqli_connect_error());
}
//设置字符集
if (!mysqli_set_charset($link, 'utf8')) {
    exit(mysqli_error($link));
}
$sql = 'select * from `student`';
$result = mysqli_query($link, $sql);
if (!$result) {
    exit(mysqli_error($link));
}
$list = [];
while ($row = mysqli_fetch_assoc($result)) {
    $list[] = $row;
}
mysqli_free_result($result);
mysqli_close($link);
echo '<table>
        <tr>
            <th>id</th>
            <th>姓名</th>
            <th>年龄</th>
        </tr>';
foreach ($list as $val) {
    echo "<tr>
            <td>{$val['id']}</td>
            <td>{$val['name']}</td>
            <td>{$val['age']}</td>
        </tr>";
}
echo '</table>';
