<?php
require_once dirname(__FILE__) . '/config.php';

function listarOpcoes($tipo)
{
    $tabelasPermitidas = array(
        'autor' => 'autor',
        'categoria' => 'categoria',
        'editora' => 'editora',
    );

    if (!isset($tabelasPermitidas[$tipo])) {
        echo "<!-- Tipo inválido: $tipo -->";
        return;
    }

    global $conectar;
    $tabela = $tabelasPermitidas[$tipo];
    $sql = "SELECT codigo, nome FROM $tabela";
    $resultado = mysqli_query($conectar, $sql);

    if (!$resultado) {
        echo "<!-- Erro ao buscar dados da tabela $tabela -->";
        return;
    }

    while ($linha = mysqli_fetch_assoc($resultado)) {
        echo "<option value='" . $linha['codigo'] . "'>" . htmlspecialchars($linha['nome']) . "</option>";
    }
}
