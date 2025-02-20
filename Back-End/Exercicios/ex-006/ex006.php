<?php
// capturar os dados
$nome = $_POST['nome'];
$salario = $_POST['salario'];
$vendas = $_POST['vendas'];

$result = (vendas * 0.05) + $vendas;


echo 'O vendedor '.$nome.'Tem o salario total de: '.$result;
?>