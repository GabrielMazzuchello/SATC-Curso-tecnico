<?php
// Configurações do banco de dados
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'loja');

// Conectar ao banco de dados
$conectar = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
if ($conectar->connect_error) {
   die("Falha na conexão: " . $conectar->connect_error);
}
// 

// Função para sanitizar entradas
function sanitizeInput($data)
{
   return htmlspecialchars(strip_tags(trim($data)));
}

// Função para manipulação de arquivos
function handleFileUpload($file, $diretorio)
{
   if ($file['error'] !== UPLOAD_ERR_OK) return null;

   $extensao = pathinfo($file['name'], PATHINFO_EXTENSION);
   $extensoesPermitidas = ['jpg', 'jpeg', 'png', 'gif'];

   if (!in_array(strtolower($extensao), $extensoesPermitidas)) return null;

   $novoNome = uniqid() . '.' . $extensao;
   $caminhoCompleto = $diretorio . $novoNome;

   if (move_uploaded_file($file['tmp_name'], $caminhoCompleto)) {
      return $novoNome;
   }
   return null;
}

// Processar operações
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
   $diretorioFotos = 'fotos/';

   // Operação de Cadastro
   if (isset($_POST['gravar'])) {
      $foto1 = handleFileUpload($_FILES['foto1'], $diretorioFotos);
      $foto2 = handleFileUpload($_FILES['foto2'], $diretorioFotos);

      $stmt = $conectar->prepare("INSERT INTO produto (
            codigo, descricao, cor, tamanho, preco, 
            codmarca, codcategoria, codtipo, foto1, foto2
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");

      $stmt->bind_param(
         "ssssdsiiss",
         sanitizeInput($_POST['codigo']),
         sanitizeInput($_POST['descricao']),
         sanitizeInput($_POST['cor']),
         sanitizeInput($_POST['tamanho']),
         sanitizeInput($_POST['preco']),
         sanitizeInput($_POST['codmarca']),
         sanitizeInput($_POST['codcategoria']),
         sanitizeInput($_POST['codtipo']),
         $foto1,
         $foto2
      );

      if ($stmt->execute()) {
         echo "Produto cadastrado com sucesso!";
      } else {
         echo "Erro ao cadastrar: " . $stmt->error;
      }
   }

   // Operação de Exclusão
   if (isset($_POST['excluir'])) {
      $stmt = $conectar->prepare("DELETE FROM produto WHERE codigo = ?");
      $stmt->bind_param("s", sanitizeInput($_POST['codigo']));

      if ($stmt->execute()) {
         echo "Produto excluído com sucesso!";
      } else {
         echo "Erro ao excluir: " . $stmt->error;
      }
   }

   // Operação de Alteração
   if (isset($_POST['alterar'])) {
      $stmt = $conectar->prepare("UPDATE produto SET 
            descricao = ?,
            cor = ?,
            tamanho = ?,
            preco = ?,
            codmarca = ?,
            codcategoria = ?,
            codtipo = ?
            WHERE codigo = ?
        ");

      $stmt->bind_param(
         "ssssiiis",
         sanitizeInput($_POST['descricao']),
         sanitizeInput($_POST['cor']),
         sanitizeInput($_POST['tamanho']),
         sanitizeInput($_POST['preco']),
         sanitizeInput($_POST['codmarca']),
         sanitizeInput($_POST['codcategoria']),
         sanitizeInput($_POST['codtipo']),
         sanitizeInput($_POST['codigo'])
      );

      if ($stmt->execute()) {
         echo "Produto atualizado com sucesso!";
      } else {
         echo "Erro ao atualizar: " . $stmt->error;
      }
   }
}

// Consulta para exibir produtos
$sql = "SELECT * FROM produto";
$result = $conectar->query($sql);
?>

<!DOCTYPE html>
<html>

<body>

   <!-- Formulário único para todas operações -->
   <form method="post" enctype="multipart/form-data">
      <!-- Campos comuns -->
      <input type="text" name="codigo" placeholder="Código" required>
      <input type="text" name="descricao" placeholder="Descrição">
      <input type="text" name="cor" placeholder="Cor">
      <input type="text" name="tamanho" placeholder="Tamanho">
      <input type="number" name="preco" placeholder="Preço" step="0.01">
      <input type="number" name="codmarca" placeholder="Código Marca">
      <input type="number" name="codcategoria" placeholder="Código Categoria">
      <input type="number" name="codtipo" placeholder="Código Tipo">

      <!-- Upload de fotos -->
      <input type="file" name="foto1">
      <input type="file" name="foto2">

      <!-- Botões de ação -->
      <button type="submit" name="gravar">Cadastrar</button>
      <button type="submit" name="alterar">Atualizar</button>
      <button type="submit" name="excluir">Excluir</button>
   </form>

   <!-- Exibição dos produtos -->
   <?php if ($result->num_rows > 0): ?>
      <h2>Produtos Cadastrados</h2>
      <?php while ($produto = $result->fetch_assoc()): ?>
         <div>
            <p>Código: <?= $produto['codigo'] ?></p>
            <p>Descrição: <?= $produto['descricao'] ?></p>
            <p>Preço: R$ <?= number_format($produto['preco'], 2, ',', '.') ?></p>
            <?php if ($produto['foto1']): ?>
               <img src="fotos/<?= $produto['foto1'] ?>" width="200">
            <?php endif; ?>
            <?php if ($produto['foto2']): ?>
               <img src="fotos/<?= $produto['foto2'] ?>" width="200">
            <?php endif; ?>
            <hr>
         </div>
      <?php endwhile; ?>
   <?php else: ?>
      <p>Nenhum produto encontrado.</p>
   <?php endif; ?>

   <?php $conectar->close(); ?>
</body>

</html>