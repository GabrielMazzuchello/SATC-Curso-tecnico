<?php
// capturar os dados
$valor = $_POST['valor'];

$result = ((($valor * 0.25) + $valor) * 0.35) + $valor;


echo 'O aluno'.$nome.'A nota é de: '.$result;
?>