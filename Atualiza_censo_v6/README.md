# ⚙️ Configuração do Sistema de Automação

Documentação do arquivo `config.ini` utilizado pelo sistema de automação do projeto **Hospital Central**.

O arquivo centraliza as configurações necessárias para executar diferentes etapas da automação, incluindo a inicialização do **Fathos**, a automação de acesso ao **Microsoft Edge** e o controle do comportamento geral da execução.

> **⚠️ Segurança:** este arquivo pode conter credenciais, caminhos internos e outras informações sensíveis. Não publique uma configuração real em repositórios públicos ou compartilhe o arquivo sem remover os dados confidenciais.

---

## 📋 Visão geral

O `config.ini` é organizado em três seções principais:

| Seção        | Finalidade                                                                 |
| ------------ | -------------------------------------------------------------------------- |
| `[Fathos]`   | Configura o executável, parâmetros e credenciais do Fathos                 |
| `[edge]`     | Configura o acesso automatizado pelo Microsoft Edge                        |
| `[Execucao]` | Controla quais etapas serão executadas e como a automação deverá funcionar |

A estrutura geral é:

```text
config.ini
├── [Fathos]
│   ├── executable
│   ├── params
│   ├── username
│   ├── encrypted_password
│   └── save_path
│
├── [edge]
│   ├── site
│   ├── username
│   └── encrypted_password
│
└── [Execucao]
    ├── run_fathos
    ├── run_edge
    ├── fathos_background
    ├── edge_background
    ├── max_tentativas
    ├── Group
    ├── Group_1
    └── Group_2
```

---

# 🏥 `[Fathos]`

A seção `[Fathos]` contém as informações necessárias para localizar e executar o sistema Fathos, além dos parâmetros utilizados durante sua inicialização.

### Exemplo

```ini
[Fathos]
executable = C:\CAMINHO\Fathos.exe
params = agfaprod, %profile%
username = SEU_USUARIO
encrypted_password = SUA_SENHA
save_path = C:\CAMINHO\resultado.xls
```

### Parâmetros

| Chave                | Descrição                                                                               |
| -------------------- | --------------------------------------------------------------------------------------- |
| `executable`         | Caminho completo para o executável `Fathos.exe`.                                        |
| `params`             | Parâmetros utilizados na inicialização do Fathos.                                       |
| `username`           | Usuário utilizado para autenticação no sistema.                                         |
| `encrypted_password` | Valor de senha utilizado pela automação conforme o mecanismo implementado pelo projeto. |
| `save_path`          | Caminho onde o arquivo gerado pela automação deverá ser salvo.                          |

### `executable`

Define a localização do executável do Fathos:

```ini
executable = C:\AGFA_Exe_22\Fathos.exe
```

O caminho deve apontar para um arquivo existente no computador onde a automação será executada.

Para verificar manualmente, confirme se o arquivo existe no caminho configurado.

---

### `params`

Define os argumentos enviados ao Fathos durante sua inicialização.

Exemplo:

```ini
params = agfaprod, %profile%
```

O marcador `%profile%` é utilizado pela automação para representar o perfil correspondente à execução.

> **Nota:** não altere a estrutura dos parâmetros sem verificar primeiro como o script utiliza esse valor.

---

### `username`

Define o usuário utilizado no processo de autenticação:

```ini
username = SEU_USUARIO
```

Não utilize contas pessoais ou credenciais reais em exemplos publicados no GitHub.

---

### `encrypted_password`

Representa o valor de senha utilizado pelo sistema:

```ini
encrypted_password = SEU_VALOR_SEGURO
```

Apesar do nome da chave indicar uma senha criptografada, **não se deve assumir que o valor esteja efetivamente criptografado sem verificar a implementação do sistema**.

Para ambientes de produção, recomenda-se evitar credenciais diretamente no arquivo de configuração sempre que o projeto permitir.

---

### `save_path`

Define o local onde o resultado produzido pela automação será salvo:

```ini
save_path = C:\CAMINHO\resultado.xls
```

Certifique-se de que:

* o diretório exista;
* o usuário que executa a automação tenha permissão de escrita;
* o caminho seja acessível pelo processo;
* arquivos importantes não sejam sobrescritos acidentalmente.

---

# 🌐 `[edge]`

A seção `[edge]` contém as configurações utilizadas para a automação de acesso através do **Microsoft Edge**.

### Exemplo

```ini
[edge]
site = https://SEU-SISTEMA-INTERNO.exemplo/login
username = SEU_USUARIO
encrypted_password = SUA_SENHA
```

### Parâmetros

| Chave                | Descrição                                             |
| -------------------- | ----------------------------------------------------- |
| `site`               | Endereço do sistema que será acessado pelo navegador. |
| `username`           | Usuário utilizado no formulário de autenticação.      |
| `encrypted_password` | Valor de senha utilizado pela automação.              |

---

### `site`

Define o endereço que será aberto pelo navegador:

```ini
site = https://SEU-SISTEMA-INTERNO.exemplo/login
```

Em ambientes corporativos, esse endereço normalmente pode depender de:

* rede interna;
* VPN;
* DNS corporativo;
* disponibilidade do sistema;
* permissões de acesso.

> **🔒 Atenção:** URLs internas de sistemas hospitalares ou corporativos não devem ser expostas desnecessariamente em documentação pública.

---

### `username`

Usuário utilizado no processo de login:

```ini
username = SEU_USUARIO
```

Utilize uma conta apropriada para automação e siga as políticas de acesso da organização.

---

### `encrypted_password`

Valor utilizado para autenticação:

```ini
encrypted_password = SEU_VALOR_SEGURO
```

Não compartilhe esse campo contendo credenciais reais.

---

# ⚙️ `[Execucao]`

A seção `[Execucao]` controla o comportamento geral da automação.

### Exemplo

```ini
[Execucao]
run_fathos = true
run_edge = false
fathos_background = false
edge_background = false
max_tentativas = 3
Group = off
Group_1 = true
Group_2 = false
```

### Parâmetros

| Chave               | Tipo     | Descrição                                                                              |
| ------------------- | -------- | -------------------------------------------------------------------------------------- |
| `run_fathos`        | Booleano | Define se a etapa relacionada ao Fathos será executada.                                |
| `run_edge`          | Booleano | Define se a etapa relacionada ao Edge será executada.                                  |
| `fathos_background` | Booleano | Controla a execução do Fathos em segundo plano, conforme suportado pela implementação. |
| `edge_background`   | Booleano | Controla o modo de execução do navegador.                                              |
| `max_tentativas`    | Número   | Define o limite de tentativas utilizado pela automação.                                |
| `Group`             | `on/off` | Controla o agrupamento geral.                                                          |
| `Group_1`           | Booleano | Ativa ou desativa o grupo 1.                                                           |
| `Group_2`           | Booleano | Ativa ou desativa o grupo 2.                                                           |

---

## 🔄 Opções booleanas

As opções booleanas devem utilizar:

```ini
true
```

ou:

```ini
false
```

Exemplo:

```ini
run_fathos = true
run_edge = false
```

Isso significa que o fluxo relacionado ao Fathos está habilitado e o fluxo relacionado ao Edge está desabilitado.

---

## 🔁 Número de tentativas

A configuração:

```ini
max_tentativas = 3
```

define o número máximo de tentativas utilizado pelo mecanismo de automação em situações de falha.

Por exemplo:

```ini
max_tentativas = 5
```

aumenta o limite para cinco tentativas.

> O comportamento exato de uma nova tentativa depende da implementação do script responsável pela automação.

---

# 🧩 Configurações de grupos

O arquivo também possui configurações relacionadas a grupos:

```ini
Group = off
Group_1 = true
Group_2 = false
```

De forma geral:

* `Group` controla o estado geral do agrupamento;
* `Group_1` controla o primeiro grupo;
* `Group_2` controla o segundo grupo.

Exemplo:

```ini
Group = on
Group_1 = true
Group_2 = false
```

O significado operacional de cada grupo depende da lógica implementada na versão da automação.

> **Importante:** os nomes das configurações devem ser mantidos exatamente como esperados pelo programa. Alterações como `group_1`, `GROUP_1` ou `Grupo_1` podem não ser reconhecidas dependendo da implementação.

---

# ▶️ Exemplos de configuração

## Executar somente o Fathos

Para executar somente a etapa do Fathos:

```ini
[Execucao]
run_fathos = true
run_edge = false
fathos_background = false
edge_background = false
max_tentativas = 3
Group = off
Group_1 = true
Group_2 = false
```

Nesse cenário, o Fathos permanece habilitado e o fluxo do Edge permanece desabilitado.

---

## Executar Fathos e Edge

Caso as duas etapas estejam habilitadas:

```ini
[Execucao]
run_fathos = true
run_edge = true
fathos_background = false
edge_background = false
max_tentativas = 3
Group = off
Group_1 = true
Group_2 = false
```

A execução seguirá a lógica definida pelo programa para cada uma das etapas.

---

## Execução em segundo plano

Quando suportado pela implementação:

```ini
[Execucao]
run_fathos = true
run_edge = true
fathos_background = true
edge_background = true
max_tentativas = 3
Group = off
Group_1 = true
Group_2 = false
```

> ⚠️ A execução em segundo plano pode apresentar limitações dependendo do aplicativo, da sessão do Windows, das permissões e da forma como a automação interage com interfaces gráficas.

---

# 🔐 Segurança

Este é um dos pontos mais importantes na utilização do `config.ini`.

O arquivo pode conter informações como:

* usuários;
* senhas;
* caminhos internos;
* URLs de sistemas corporativos;
* informações relacionadas à infraestrutura;
* locais de armazenamento de arquivos gerados.

### ❌ Nunca faça commit de credenciais reais

Evite:

```ini
username = joao.silva
encrypted_password = senha-real
```

Prefira um arquivo de exemplo:

```ini
username = SEU_USUARIO
encrypted_password = SEU_VALOR_SEGURO
```

### 📄 Recomendação

Mantenha um arquivo:

```text
config.example.ini
```

com valores fictícios para documentação e distribuição.

O arquivo real:

```text
config.ini
```

deve ser tratado como configuração potencialmente sensível.

Se possível, adicione o arquivo real ao `.gitignore`:

```gitignore
config.ini
```

---

# 🛡️ Boas práticas

### 1. Não versionar credenciais

Nunca coloque senhas reais diretamente no Git.

### 2. Não publicar sistemas internos

Evite documentar publicamente:

* URLs internas;
* endereços IP privados;
* nomes de servidores;
* caminhos de rede;
* usuários reais.

### 3. Utilizar menor privilégio

A conta utilizada pela automação deve possuir somente as permissões necessárias para realizar suas tarefas.

### 4. Validar caminhos

Antes de executar a automação, confirme se:

```text
Fathos.exe
```

e os diretórios de saída realmente existem.

### 5. Cuidado com arquivos gerados

Se `save_path` apontar para um arquivo existente, confirme se a automação poderá sobrescrevê-lo.

---

# 🧪 Checklist antes da execução

Antes de executar a automação, verifique:

```text
[ ] Fathos.exe existe no caminho configurado
[ ] O usuário possui acesso ao Fathos
[ ] As credenciais estão corretas
[ ] O endereço do sistema está acessível
[ ] Microsoft Edge está instalado
[ ] O WebDriver utilizado pelo projeto é compatível
[ ] O diretório de saída existe
[ ] O usuário possui permissão de escrita
[ ] run_fathos está configurado corretamente
[ ] run_edge está configurado corretamente
[ ] max_tentativas possui um valor adequado
[ ] Nenhuma credencial real será publicada no Git
```

---

# 🔧 Solução de problemas

## Fathos não inicia

Verifique:

```ini
executable = C:\CAMINHO\Fathos.exe
```

Confirme se:

* o arquivo existe;
* o caminho está correto;
* o usuário possui permissão para executá-lo;
* os parâmetros configurados são válidos.

---

## Arquivo não é salvo

Verifique:

```ini
save_path = C:\CAMINHO\resultado.xls
```

Confirme se o diretório existe e se o processo possui permissão de escrita.

---

## Edge não acessa o sistema

Verifique:

```ini
site = https://SEU-SISTEMA-INTERNO.exemplo/login
```

Depois confirme:

1. conectividade com a rede;
2. acesso ao endereço pelo navegador manualmente;
3. credenciais;
4. compatibilidade do WebDriver;
5. configuração de `run_edge`.

---

## A automação falha repetidamente

Verifique:

```ini
max_tentativas = 3
```

Aumentar o número de tentativas pode ajudar em falhas transitórias, mas **não corrige problemas de configuração**.

Se a mesma falha ocorrer em todas as tentativas, investigue a causa original antes de simplesmente aumentar o limite.

---

# 📁 Estrutura recomendada

Uma organização mais segura para distribuição do projeto seria:

```text
Atualiza_censo_v6/
├── config.example.ini
├── config.ini              # não versionar
├── requirements.txt
├── README.md
├── atualiza_censo_v6.py
└── ...
```

O `config.example.ini` deve conter apenas valores fictícios:

```ini
[Fathos]
executable = C:\CAMINHO\Fathos.exe
params = agfaprod, %profile%
username = SEU_USUARIO
encrypted_password = SEU_VALOR
save_path = C:\CAMINHO\resultado.xls

[edge]
site = https://SEU-SISTEMA.exemplo/login
username = SEU_USUARIO
encrypted_password = SEU_VALOR

[Execucao]
run_fathos = true
run_edge = false
fathos_background = false
edge_background = false
max_tentativas = 3
Group = off
Group_1 = true
Group_2 = false
```

---

<!-- 
# 💡 Recomendações para evolução

Para tornar o sistema mais robusto, algumas melhorias podem ser consideradas:

* [ ] Criar `config.example.ini`.
* [ ] Ignorar `config.ini` no Git.
* [ ] Migrar credenciais para variáveis de ambiente ou mecanismo seguro de secrets.
* [ ] Validar automaticamente caminhos e parâmetros antes da execução.
* [ ] Validar se o `Fathos.exe` existe.
* [ ] Validar conectividade com o sistema web antes de iniciar a automação.
* [ ] Melhorar mensagens de erro.
* [ ] Registrar falhas em log.
* [ ] Padronizar os nomes das configurações.
* [ ] Documentar formalmente o comportamento de `Group`, `Group_1` e `Group_2`.
* [ ] Validar compatibilidade entre Microsoft Edge e WebDriver.
* [ ] Criar testes para validação do arquivo de configuração.
-->

---

# 📚 Referência rápida

| Configuração         | Exemplo                | Função                              |
| -------------------- | ---------------------- | ----------------------------------- |
| `executable`         | `C:\...\Fathos.exe`    | Executável do Fathos                |
| `params`             | `agfaprod, %profile%`  | Parâmetros de inicialização         |
| `username`           | `SEU_USUARIO`          | Usuário de autenticação             |
| `encrypted_password` | `SEU_VALOR`            | Credencial utilizada pela automação |
| `save_path`          | `C:\...\resultado.xls` | Arquivo de saída                    |
| `site`               | `https://...`          | Sistema acessado pelo Edge          |
| `run_fathos`         | `true`                 | Ativa/desativa Fathos               |
| `run_edge`           | `true`                 | Ativa/desativa Edge                 |
| `fathos_background`  | `false`                | Execução do Fathos                  |
| `edge_background`    | `false`                | Execução do Edge                    |
| `max_tentativas`     | `3`                    | Limite de tentativas                |
| `Group`              | `on/off`               | Controle geral de grupos            |
| `Group_1`            | `true`                 | Ativa grupo 1                       |
| `Group_2`            | `false`                | Ativa grupo 2                       |

---

# 📄 Licença

Este arquivo faz parte do projeto **Hospital Central Automation Suite**.

Consulte o arquivo [`LICENSE`](../LICENSE) na raiz do repositório para obter os termos completos da licença aplicável ao projeto.

---

## ⚠️ Aviso

Este arquivo de configuração controla automações que podem interagir com sistemas corporativos e dados potencialmente sensíveis.

Utilize a automação somente em ambientes autorizados e de acordo com as políticas de segurança, privacidade e acesso da organização.

**Nunca publique credenciais, informações internas ou dados em repositórios públicos.**
