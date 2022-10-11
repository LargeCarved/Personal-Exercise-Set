<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>九九乘法表</title>
    <style>
        body {
            background: url(九九.jpg) no-repeat;
        }

        table {
            border-spacing: 2px;
            width: 950px;
            margin-top: 330px;
        }

        .bordered tr,
        td {
            border: solid #CcC 1px;
            padding: 5px;
            text-align: center;
            background-color: #FEFEFE;
            opacity: 0.8;
        }
    </style>

</head>

<body>
    <table class="bordered">
        <?php
        for ($i = 1; $i < 10; $i++) {
            echo '<tr>';
            for ($j = 1; $j <= $i; $j++) {
                echo "<td>{$j}x{$i}=" . $j * $i . '</td>';
            }
            echo '</tr>';
        }
        ?>
    </table>

</body>

</html>
