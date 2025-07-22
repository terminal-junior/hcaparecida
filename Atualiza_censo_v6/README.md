# Configuração do Sistema de Automação - `config.ini`

Este arquivo `config.ini` é usado para configurar a automação de dois sistemas distintos: o **Fathos** (um sistema de gestão hospitalar) e o navegador **Edge** (para acesso a um site interno). Este guia explica, de forma simples e clara, o propósito de cada seção e cada chave, para que até iniciantes possam entender e personalizar conforme suas necessidades.

---

## 🗂 Seções do Arquivo

O arquivo está dividido em 3 seções principais:

- `[Fathos]`: configurações relacionadas ao sistema Fathos.
- `[edge]`: configurações de login automático no navegador Edge.
- `[Execucao]`: define quais ações devem ser executadas ou não.

---

## 🔧 [Fathos]

Essa seção configura a execução do programa Fathos.

```ini
[Fathos]
executable = C:\AGFA_Exe_22\Fathos.exe
params = agfaprod, %profile%
username = user.name
encrypted_password = password
save_path = C:\teste\censo_test.xls
```

| Chave                | Explicação                                                                |
|----------------------|---------------------------------------------------------------------------|
| `executable`         | Caminho completo para o executável do Fathos (`.exe`).                    |
| `params`             | Parâmetros passados para o programa ao iniciar. `%profile%` será substituído automaticamente pelo nome do perfil desejado. |
| `username`           | Nome de usuário utilizado para login no Fathos.                           |
| `encrypted_password` | Senha do usuário.                                                         |
| `save_path`          | Caminho onde o arquivo gerado pelo sistema será salvo.                    |

---

## 🌐 [edge]

Essa seção configura o acesso automatizado ao site do hospital via navegador Microsoft Edge.

```ini
[edge]
site = http://hosp.hcaparecida.com.br/mapa/login.asp
username = user.name
encrypted_password = password
```

| Chave                | Explicação                                                                 |
|----------------------|---------------------------------------------------------------------------|
| `site`               | URL do site onde será feito o login automático.                           |
| `username`           | Nome de usuário usado no formulário do site.                              |
| `encrypted_password` | Senha do usuário para o site.                               |

---

## ⚙️ [Execucao]

Define o comportamento da automação para cada sistema.

```ini
[Execucao]
run_fathos = true
run_edge = false
fathos_background = false
edge_background = false
```

| Chave              | Explicação                                                                                 |
|--------------------|------------------------------------------------------------------------------------------- |
| `run_fathos`       | Se for `true`, o script executará o programa Fathos. Se for `false`, não executará.        |
| `run_edge`         | Se for `true`, o script abrirá o site no Edge e fará login automático.                     |
| `fathos_background`| Se for `true`, o Fathos será executado em segundo plano (sem abrir janela visível).        |
| `edge_background`  | Se for `true`, o navegador Edge será executado em segundo plano (sem abrir janela visível).|

> ⚠️ Importante: Executar em segundo plano pode exigir permissões especiais ou configurações adicionais, dependendo do sistema operacional.

---

## ✅ Exemplo de Uso

Suponha que você queira:
- Executar apenas o Fathos com login automático.
- Deixar o Edge desativado.
- Salvar o resultado do Fathos em um arquivo Excel.
- Ver a interface do Fathos ao rodar.

Você deve configurar assim:

```ini
[Execucao]
run_fathos = true
run_edge = false
fathos_background = false
edge_background = false
```

---

## 🔐 Segurança

- Os campos `encrypted_password` devem conter senhas.
- Nunca compartilhe o conteúdo desse arquivo sem antes remover os dados sensíveis.

---

## 📝 Dicas Finais

- Edite o arquivo com um editor de texto simples como o **Notepad++** ou **Visual Studio Code**.
- Verifique se os caminhos apontam para locais válidos no seu sistema.
- Use `true` ou `false` (sem aspas) para as opções booleanas.

---

Se tiver dúvidas ou quiser expandir esse sistema com mais funcionalidades, entre em contato com o desenvolvedor responsável, e-mail: josi.junior@hcaparecida.com.br.
