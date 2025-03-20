<?php

$conectar = new mysqli('localhost', 'root', '', 'loja');
if ($conectar->connect_error) {
    die("Connection failed: " . $conectar->connect_error);
}

if (isset($_POST['gravar']))
{
    $codigo            = $_POST['codigo'];
    $descricao         = $_POST['descricao'];
    $cor               = $_POST['cor'];
    $tamanho           = $_POST['tamanho'];
    $preco             = $_POST['preco'];
    $codmarca          = $_POST['codmarca'];
    $codcategoria      = $_POST['codcategoria'];
    $codtipo           = $_POST['codtipo'];

    $foto1             = $_FILES['foto1'];
    $foto2             = $_FILES['foto2'];


    $diretorio = "fotos/";

    $extensao1 = strtolower(substr($_FILES['foto1']['name'], -4));
    $novo_nome1 = md5(time().$extensao1);
    move_uploaded_file($_FILES['foto1']['tmp_name'], $diretorio.$novo_nome1);


    $extensao2 = strtolower(substr($_FILES['foto2']['name'], -6));
    $novo_nome2 = md5(time().$extensao2);
   $sql = "INSERT INTO produto (codigo, descricao, cor, tamanho, preco, codmarca, codcategoria, codtipo, foto1, foto2)
           VALUES ('$codigo', '$descricao', '$cor', '$tamanho', '$preco', '$codmarca', '$codcategoria', '$codtipo', '$novo_nome1', '$novo_nome2')";

   $resultado = $conectar->query($sql);

   $resultado = mysql_query($sql);

   if ($resultado)
        {echo " Falha ao gravar os dados informados";}
   else
        {echo " Dados informados cadastrados com sucesso";}
}

if (isset($_POST['excluir']))
{
    $codigo            = $_POST['codigo'];
    $descricao         = $_POST['descricao'];
    $cor               = $_POST['cor'];
    $tamanho           = $_POST['tamanho'];
    $preco             = $_POST['preco'];
    $codmarca          = $_POST['codmarca'];
    $codcategoria      = $_POST['codcategoria'];
    $codtipo           = $_POST['codtipo'];
    $foto1             = $_POST['foto1'];
    $foto2             = $_POST['foto2'];

  $sql = "DELETE FROM produto WHERE codigo = '$codigo'";

  $resultado = mysql_query($sql);

  if ($resultado === TRUE)
  {
     echo 'Exclusao realizada com Sucesso';
  }
  else
  {
     echo 'Erro ao excluir dados.';
  }
}

if (isset($_POST['alterar']))
{
    $codigo            = $_POST['codigo'];
    $descricao         = $_POST['descricao'];
    $cor               = $_POST['cor'];
    $tamanho           = $_POST['tamanho'];
    $preco             = $_POST['preco'];
    $codmarca          = $_POST['codmarca'];
    $codcategoria      = $_POST['codcategoria'];
    $codtipo           = $_POST['codtipo'];
    $foto1             = $_POST['foto1'];
    $foto2             = $_POST['foto2'];

  $sql = "UPDATE produto SET descricao='$descricao',preco='$preco'
          WHERE codigo = '$codigo'";
  $resultado = mysql_query($sql);

  if ($resultado === TRUE)
  {
     echo 'Dados alterados com Sucesso';
  }
  else
  {
     echo 'Erro ao alterar dados.';
  }
}

   $sql = "SELECT codigo, descricao, cor, tamanho, preco, codmarca, codcategoria, codtipo, foto1, foto2 FROM produto";
   $result = $conectar->query($sql);

   if ($result->num_rows == 0)

   if (mysql_num_rows($sql) == 0)
         {echo "Desculpe, mas sua pesquisa nao retornou resultados.";}
        while ($resultado = $result->fetch_assoc())
        {
        echo "<b>Produtos Cadastrados:</b><br><br>";
        while ($resultado = mysql_fetch_array($sql))
 	        {
                echo "Codigo         : ".$dados->codigo." ";
                echo "Descricao      : ".$dados->descricao."<br>";
                echo "Cor            : ".$dados->cor."<br>";
                echo "Tamanho        : ".$dados->tamanho." ";
                echo "Preco          : ".$dados->preco."<br>";
                echo "Marca          : ".$dados->codmarca."";
                echo "Categoria      : ".$dados->codcategoria." ";
                echo "Tipo           : ".$dados->codtipo." ";
                echo '<img src="fotos/'.$dados->foto1.'"height="200" width="200" />'."  ";
                echo '<img src="fotos/'.$dados->foto2.'"height="200" width="200" />'."<br><br>  ";
            }
        }
}

//------- alterar  ??

// ------- excluir  ??


if (isset($_POST['pesquisar']))
{
   $sql = mysql_query("SELECT codigo,descricao,cor,tamanho,preco,codmarca,codcategoria,codtipo,foto1,foto2 FROM produto");
   
   if (mysql_num_rows($sql) == 0)
         {echo "Desculpe, mas sua pesquisa nao encontrou resultados.";}
        while ($dados = $result->fetch_object())
        {
        echo "<b>Produtos Cadastrados:</b><br><br>";
        while ($dados = mysql_fetch_object($sql))
     	{
               echo "Codigo    : ".$dados->codigo."  ";
               echo "Desricao  : ".$dados->descricao." ";
               echo "Cor       : ".$dados->cor." ";
               echo "Tamanho   : ".$dados->tamanho." ";
               echo "Preco     : ".$dados->preco."<br>";
               echo "Marca     : ".$dados->codmarca."";
               echo "Categoria : ".$dados->codcategoria." ";
               echo "Tipo      : ".$dados->codtipo."<br>";
               echo '<img src="fotos/'.$dados->foto1.'"height="200" width="200" />'."  ";
               echo '<img src="fotos/'.$dados->foto2.'"height="200" width="200" />'."<br><br>  ";
	    }
     }
}

?>
