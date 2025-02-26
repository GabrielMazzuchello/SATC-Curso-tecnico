# Guia de Configuração do Prettier para PHP e Java

Este guia vai te ajudar a configurar o **Prettier** para formatar arquivos PHP e Java no seu ambiente de desenvolvimento. Siga os passos abaixo para configurar corretamente.

## 1. Inicialize um Projeto Node (se necessário)

Se você ainda não tem um `package.json` no seu repositório, crie um com o comando abaixo. Ele irá gerar automaticamente o arquivo `package.json` na raiz do seu projeto:

```bash
npm init -y  # Cria o arquivo package.json se não existir
```

2. (Na pasta do projeto) Instale o Prettier e os Plugins para PHP e Java Execute o comando:

```
npm install --save-dev prettier @prettier/plugin-php prettier-plugin-java
```

Isso vai instalar o Prettier e os plugins que permitem a formatação de código PHP e Java.

3. Crie o Arquivo de Configuração do Prettier
   Agora, crie o arquivo de configuração do Prettier, chamado `.prettierrc.json` ou .prettier.json, e adicione as configurações necessárias. Se você preferir, pode salvar esse arquivo na pasta .vscode do seu projeto para garantir que as configurações sejam aplicadas ao seu ambiente de desenvolvimento.

```
{
"plugins": ["@prettier/plugin-php", "prettier-plugin-java"]
}
```

Esse arquivo de configuração garante que o Prettier use os plugins que você instalou para PHP e Java.

4. (Opcional) Configuração no VS Code
   Se você deseja garantir que o VS Code use essas configurações de formatação, adicione no arquivo settings.json do VS Code a seguinte linha:

```
{
"prettier.prettierPath": "C:/caminho/para/seu/projeto/node_modules/prettier",
"editor.defaultFormatter": "esbenp.prettier-vscode",
"editor.formatOnSave": true
}
```

Isso irá garantir que o Prettier seja utilizado como formatter padrão e formate seu código automaticamente ao salvar.

🔧 Dicas Adicionais
Verifique se o Prettier está funcionando: Se o Prettier não estiver formatando os arquivos corretamente, use o comando:

```
npx prettier --write .
```

iso irá formatar todos os arquivos suportados no seu projeto.

Verifique o caminho do Prettier: Se você tiver problemas com o VS Code encontrando o Prettier, verifique se o caminho do executável está correto (veja o passo opcional acima para ajustar isso).

Instale extensões no VS Code: Para facilitar, instale a extensão Prettier - Code formatter do marketplace do VS Code.

⚡ Resumo dos Comandos
Inicialize o projeto (se necessário):

```
npm init -y
```

Instale Prettier e os plugins:

```
npm install --save-dev prettier @prettier/plugin-php prettier-plugin-java
```

Crie o arquivo .prettierrc ou .prettier.json com a configuração dos plugins.

---

Esse código pode ser copiado diretamente para um arquivo `.md` (como `README.md` ou qualquer outro arquivo de documentação) para documentar a configuração do Prettier no seu projeto.
