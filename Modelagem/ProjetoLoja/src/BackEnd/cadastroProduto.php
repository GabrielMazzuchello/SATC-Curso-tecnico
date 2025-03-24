<?php

// Conexão com o banco de dados
$conectar = mysqli_connect('localhost', 'root', '', 'loja');
if (!$conectar) {
   die('Conexão falhou: ' . mysqli_connect_error());
}

if (isset($_POST['gravar'])) {
   $codigo = mysqli_real_escape_string($conectar, $_POST['codigo']);
   $descricao = mysqli_real_escape_string($conectar, $_POST['descricao']);
   $cor = mysqli_real_escape_string($conectar, $_POST['cor']);
   $tamanho = mysqli_real_escape_string($conectar, $_POST['tamanho']);
   $preco = mysqli_real_escape_string($conectar, $_POST['preco']);
   $codmarca = mysqli_real_escape_string($conectar, $_POST['codmarca']);
   $codcategoria = mysqli_real_escape_string($conectar, $_POST['codcategoria']);
   $codtipo = mysqli_real_escape_string($conectar, $_POST['codtipo']);

   // Diretório para salvar as imagens
   $diretorio = "../imgs/imagensProdutos/";

   // Verificar a extensão dos arquivos de imagem
   $extensao1 = strtolower(pathinfo($_FILES['foto1']['name'], PATHINFO_EXTENSION));
   $extensao2 = strtolower(pathinfo($_FILES['foto2']['name'], PATHINFO_EXTENSION));

   $tipos_permitidos = array('jpg', 'jpeg', 'png', 'gif');
   
   if (in_array($extensao1, $tipos_permitidos) && in_array($extensao2, $tipos_permitidos)) {
      // Gerar nome único para as imagens
      $novo_nome1 = md5(time() . $_FILES['foto1']['name']) . '.' . $extensao1;
      $novo_nome2 = md5(time() . $_FILES['foto2']['name']) . '.' . $extensao2;

      // Movendo as imagens para o diretório
      move_uploaded_file($_FILES['foto1']['tmp_name'], $diretorio . $novo_nome1);
      move_uploaded_file($_FILES['foto2']['tmp_name'], $diretorio . $novo_nome2);

      // Inserir no banco de dados
      $sql = "INSERT INTO produto (codigo, descricao, cor, tamanho, preco, codmarca, codcategoria, codtipo, foto1, foto2)
                VALUES ('$codigo', '$descricao', '$cor', '$tamanho', '$preco', '$codmarca', '$codcategoria', '$codtipo', '$novo_nome1', '$novo_nome2')";

      if (mysqli_query($conectar, $sql)) {
         echo "Dados informados cadastrados com sucesso";
      } else {
         echo "Erro: " . mysqli_error($conectar);
      }
   } else {
      echo "Por favor, envie imagens com extensões válidas (JPG, JPEG, PNG, GIF).";
   }
}

if (isset($_POST['excluir'])) {
   $codigo = mysqli_real_escape_string($conectar, $_POST['codigo']);

   $sql = "DELETE FROM produto WHERE codigo = '$codigo'";

   if (mysqli_query($conectar, $sql)) {
      echo 'Exclusão realizada com sucesso';
   } else {
      echo 'Erro ao excluir dados: ' . mysqli_error($conectar);
   }
}

if (isset($_POST['alterar'])) {
   $codigo = mysqli_real_escape_string($conectar, $_POST['codigo']);
   $descricao = mysqli_real_escape_string($conectar, $_POST['descricao']);
   $preco = mysqli_real_escape_string($conectar, $_POST['preco']);

   $sql = "UPDATE produto SET descricao='$descricao', preco='$preco' WHERE codigo = '$codigo'";

   if (mysqli_query($conectar, $sql)) {
      echo 'Dados alterados com sucesso';
   } else {
      echo 'Erro ao alterar dados: ' . mysqli_error($conectar);
   }
}

if (isset($_POST['pesquisar'])) {
   $sql = mysqli_query($conectar, "SELECT codigo, descricao, cor, tamanho, preco, codmarca, codcategoria, codtipo, foto1, foto2 FROM produto");

   if (mysqli_num_rows($sql) == 0) {
      echo "Desculpe, mas sua pesquisa não retornou resultados.";
   } else {
      echo "<b>Produtos Cadastrados:</b><br><br>";
      while ($dados = mysqli_fetch_object($sql)) {
         echo "Codigo    : " . $dados->codigo . "  ";
         echo "Descricao : " . $dados->descricao . " ";
         echo "Cor       : " . $dados->cor . " ";
         echo "Tamanho   : " . $dados->tamanho . " ";
         echo "Preco     : " . $dados->preco . "<br>";
         echo "Marca     : " . $dados->codmarca . "";
         echo "Categoria : " . $dados->codcategoria . " ";
         echo "Tipo      : " . $dados->codtipo . "<br>";
         echo '<img src="../imgs/imagensProdutos/' . $dados->foto1 . '" height="200" width="200" />' . "  ";
         echo '<img src="../imgs/imagensProdutos/' . $dados->foto2 . '" height="200" width="200" />' . "<br><br>  ";
      }
   }
}
