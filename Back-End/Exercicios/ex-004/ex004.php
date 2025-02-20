<?php
// capturar os dados
$nome = $_POST['nome'];
$nota1 = $_POST['nota1'];
$nota2 = $_POST['nota2'];
$nota3 = $_POST['nota3'];


$result = ($nota1 + $nota2 + $nota3) / 3;


echo 'O aluno'.$nome.'A nota é de: '.$result;
?>