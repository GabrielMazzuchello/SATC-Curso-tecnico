<?php
require_once 'config.php';
require_once 'alerta.php';

function salvarImagem($campo)
{
    if (isset($_FILES[$campo]) && $_FILES[$campo]['error'] === UPLOAD_ERR_OK) {
        $ext = pathinfo($_FILES[$campo]['name'], PATHINFO_EXTENSION);
        $nomeCriptografado = uniqid('', true) . '.' . strtolower($ext);

        // Caminho absoluto a partir da raiz do projeto
        $pastaDestino = __DIR__ . '/../assets/img/';
        $caminhoAbsoluto = $pastaDestino . $nomeCriptografado;
        $caminhoRelativo = 'assets/img/' . $nomeCriptografado;

        if (!is_dir($pastaDestino)) {
            mkdir($pastaDestino, 0755, true);
        }

        if (move_uploaded_file($_FILES[$campo]['tmp_name'], $caminhoAbsoluto)) {
            return $caminhoRelativo; // caminho salvo no banco
        }
    }
    return null;
}


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $titulo = isset($_POST['titulo']) ? $_POST['titulo'] : '';
    $nrpaginas = isset($_POST['nrpaginas']) ? intval($_POST['nrpaginas']) : 0;
    $ano = isset($_POST['ano']) ? intval($_POST['ano']) : 0;
    $codautor = isset($_POST['codautor']) ? intval($_POST['codautor']) : 0;
    $codcategoria = isset($_POST['codcategoria']) ? intval($_POST['codcategoria']) : 0;
    $codeditora = isset($_POST['codeditora']) ? intval($_POST['codeditora']) : 0;
    $resenha = isset($_POST['resenha']) ? $_POST['resenha'] : '';
    $preco = isset($_POST['preco']) ? floatval($_POST['preco']) : 0.0;

    $fotoCapa1 = salvarImagem('fotocapa1');
    $fotoCapa2 = salvarImagem('fotocapa2');


    if ($titulo && $codautor && $codcategoria && $codeditora && $fotoCapa1) {
        if (!isset($conectar)) {
            alerta("Erro de conexão com o banco de dados.");
            exit;
        }
        $stmt = mysqli_prepare($conectar, "INSERT INTO livro (titulo, nrpaginas, ano, codautor, codcategoria, codeditora, resenha, preco, fotocapa1, fotocapa2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        if ($stmt) {
            mysqli_stmt_bind_param($stmt, "siiiiisdss", $titulo, $nrpaginas, $ano, $codautor, $codcategoria, $codeditora, $resenha, $preco, $fotoCapa1, $fotoCapa2);
            mysqli_stmt_execute($stmt);
            mysqli_stmt_close($stmt);
            alerta("Livro cadastrado com sucesso!", "/pages/homeCadastros.php");
        } else {
            alerta("Erro ao preparar a query: " . mysqli_error($conectar));
        }
    } else {
        alerta("Por favor, preencha todos os campos obrigatórios e envie uma imagem.");
    }
} else {
    alerta("Requisição inválida.");
}
