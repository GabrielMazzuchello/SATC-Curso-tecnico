<?php
// capturar os dados
$nome1 = $_POST['nome1'];
$nome2 = $_POST['nome2'];
$nome3 = $_POST['nome3'];

$result = $nome1.$nome2.$nome3;

echo 'O nome ficou: '.$result;
?>