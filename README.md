# 🏥 Hospital Central Automation Suite

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)](#)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows\&logoColor=white)](#)
[![Automation](https://img.shields.io/badge/Focus-Automation-orange)](#)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-terminal--junior-181717?logo=github\&logoColor=white)](#)

> Coleção de aplicações e automações desenvolvidas para **simplificar tarefas operacionais, atualizar censos, automatizar processos e disponibilizar pequenos utilitários de suporte ao ambiente hospitalar**.

---

## 📑 Sumário

* [🎯 Sobre o projeto](#-sobre-o-projeto)
* [✨ Objetivos](#-objetivos)
* [🧩 Projetos](#-projetos)
* [🏗️ Arquitetura](#️-arquitetura)
* [📂 Estrutura do repositório](#-estrutura-do-repositório)
* [🐍 Tecnologias](#-tecnologias)
* [💻 Plataforma](#-plataforma)
* [🚀 Como começar](#-como-começar)
* [📊 Atualização de censos](#-atualização-de-censos)
* [🌐 Automação Fathos + Edge](#-automação-fathos--edge)
* [🖥️ Meu IP](#️-meu-ip)
* [🛠️ Suporte remoto](#️-suporte-remoto)
* [🔐 Segurança](#-segurança)
* [🧪 Validação](#-validação)
* [📋 Boas práticas](#-boas-práticas)
* [🛣️ Roadmap](#️-roadmap)
* [🤝 Contribuindo](#-contribuindo)
* [📄 Licença](#-licença)
* [⚠️ Aviso](#️-aviso)

---

# 🎯 Sobre o projeto

O **Hospital Central Automation Suite** é uma coleção de ferramentas e automações desenvolvidas para facilitar tarefas recorrentes relacionadas a operação, suporte e processamento de informações.

O repositório atualmente reúne projetos independentes, incluindo:

* 📊 automação de atualização de censos;
* 🏥 integração com o sistema Fathos;
* 🌐 automação do navegador Microsoft Edge;
* 🖥️ identificação de hostname e endereço IP;
* 🛠️ ferramentas auxiliares para suporte remoto.

A proposta é transformar tarefas repetitivas em processos mais rápidos, consistentes e documentados.

---

# ✨ Objetivos

Os principais objetivos do projeto são:

* ⚙️ automatizar tarefas repetitivas;
* 📊 reduzir operações manuais;
* 🏥 facilitar processos relacionados ao ambiente hospitalar;
* 🖥️ auxiliar equipes de suporte;
* 🔄 padronizar rotinas operacionais;
* 📚 manter ferramentas e configurações documentadas;
* 🧩 centralizar pequenos utilitários em um único repositório.

---

# 🧩 Projetos

O repositório possui atualmente quatro áreas principais:

| Projeto             | Finalidade                                           |
| ------------------- | ---------------------------------------------------- |
| `Atualiza_censo_v6` | Automação para atualização/processamento de censos   |
| `Atualize_Censo`    | Versões anteriores da automação de censo             |
| `Meu_IP`            | Exibição de hostname e endereço IP da máquina        |
| `UltraVNC_Remote`   | Recursos relacionados ao suporte remoto via UltraVNC |

---

## 📊 `Atualiza_censo_v6`

Projeto principal de automação de censo.

A estrutura atual inclui diferentes versões do programa, arquivo de configuração, dependências, recursos gráficos e componentes necessários para automação.

```text
Atualiza_censo_v6/
├── Inno_Setup_Compiler/
├── icons/
├── README.md
├── atualiza_censo_v6.0.py
├── atualiza_censo_v6.1.py
├── atualiza_censo_v6.2.py
├── atualiza_censo_v6.3.py
├── config.ini
├── config_backup.ini
├── icon.ico
├── msedgedriver.exe
└── requirements.txt
```

O sistema possui configuração para:

* Fathos;
* Microsoft Edge;
* execução em primeiro ou segundo plano;
* número máximo de tentativas;
* grupos de execução;
* caminhos de arquivos;
* credenciais utilizadas pela automação.

---

## 📦 `Atualize_Censo`

Contém versões anteriores da automação de atualização de censo.

Atualmente inclui versões `v5.7` e `v5.8`, além de um utilitário para coordenadas de tela, recursos gráficos, WebDriver e arquivo de dependências.

```text
Atualize_Censo/
├── atualize_censo_v5.7.py
├── atualize_censo_v5.8.py
├── coordenadas_tela.py
├── hc.ico
├── msedgedriver.exe
└── requeriments.txt
```

Essa área pode ser considerada um histórico de versões e experimentações anteriores da automação.

---

## 🖥️ `Meu_IP`

Pequeno utilitário Python com interface gráfica para exibir:

* hostname;
* endereço IP identificado pela máquina.

A implementação utiliza `socket` para obter as informações de rede e `tkinter` para apresentar os dados em uma janela gráfica.

```text
Meu_IP/
├── ip.ico
├── meu_ip.py
└── requirements.txt
```

---

## 🛠️ `UltraVNC_Remote`

Área destinada aos recursos relacionados ao suporte remoto utilizando **UltraVNC**.

A finalidade é centralizar componentes associados ao atendimento e suporte remoto das máquinas.

---

# 🏗️ Arquitetura

O repositório não representa uma única aplicação monolítica.

Cada diretório possui uma finalidade específica:

```text
                         ┌─────────────────────────┐
                         │     hcaparecida         │
                         │   Automation Suite      │
                         └────────────┬────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
              ▼                       ▼                       ▼
     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
     │ Atualiza Censo  │     │    Meu IP       │     │  Suporte Remoto │
     │                 │     │                 │     │                 │
     │ Fathos + Edge   │     │ Hostname + IP   │     │    UltraVNC     │
     └────────┬────────┘     └─────────────────┘     └─────────────────┘
              │
              ▼
     ┌─────────────────┐
     │ Dados / Censo   │
     │      XLS        │
     └─────────────────┘
```

---

# 📂 Estrutura do repositório

A estrutura atual do projeto é:

```text
.
├── Atualiza_censo_v6/
│   ├── Inno_Setup_Compiler/
│   ├── icons/
│   ├── README.md
│   ├── atualiza_censo_v6.0.py
│   ├── atualiza_censo_v6.1.py
│   ├── atualiza_censo_v6.2.py
│   ├── atualiza_censo_v6.3.py
│   ├── config.ini
│   ├── config_backup.ini
│   ├── icon.ico
│   ├── msedgedriver.exe
│   └── requirements.txt
│
├── Atualize_Censo/
│   ├── atualize_censo_v5.7.py
│   ├── atualize_censo_v5.8.py
│   ├── coordenadas_tela.py
│   ├── hc.ico
│   ├── msedgedriver.exe
│   └── requeriments.txt
│
├── Meu_IP/
│   ├── ip.ico
│   ├── meu_ip.py
│   └── requirements.txt
│
├── UltraVNC_Remote/
│
├── LICENSE
└── README.md
```

A estrutura acima representa o estado atual do repositório consultado.

---

# 🐍 Tecnologias

O projeto utiliza principalmente:

| Tecnologia         | Uso                                          |
| ------------------ | -------------------------------------------- |
| Python             | Desenvolvimento das automações e utilitários |
| Tkinter            | Interfaces gráficas                          |
| Selenium/WebDriver | Automação de navegador                       |
| Microsoft Edge     | Navegação automatizada                       |
| Edge WebDriver     | Controle automatizado do navegador           |
| Fathos             | Sistema integrado à automação de censo       |
| Excel/XLS          | Arquivos de saída/processamento              |
| UltraVNC           | Suporte remoto                               |

---

# 💻 Plataforma

O projeto possui forte dependência de ambiente **Windows**, especialmente nos módulos que utilizam:

* executáveis `.exe`;
* Microsoft Edge;
* Edge WebDriver;
* caminhos `C:\...`;
* aplicações Windows;
* Fathos.

A configuração documentada do `Atualiza_censo_v6`, por exemplo, utiliza um executável do Fathos localizado em `C:\teste\Fathos.exe` e configura o acesso a um site interno através do Edge.

> **Compatibilidade:** os componentes não devem ser considerados portáveis para Linux/macOS sem adaptações.

---

# 🚀 Como começar

## 1. Clonar o repositório

```bash
git clone https://github.com/terminal-junior/hcaparecida.git
```

Entrar no projeto:

```bash
cd hcaparecida
```

---

## 2. Escolher o projeto

Por exemplo:

```text
Atualiza_censo_v6
Atualize_Censo
Meu_IP
UltraVNC_Remote
```

Cada projeto deve ser tratado de forma independente.

---

# 📊 Atualização de censos

O projeto `Atualiza_censo_v6` utiliza uma configuração centralizada através de:

```text
config.ini
```

A configuração é dividida em três grupos principais:

```text
[Fathos]
[edge]
[Execucao]
```

---

## `[Fathos]`

Configura a execução do sistema Fathos.

Exemplo conceitual:

```ini
[Fathos]
executable = C:\teste\Fathos.exe
params = agfaprod, %profile%
username = user.name
encrypted_password = password
save_path = C:\teste\censo_test.xls
```

Principais parâmetros:

| Parâmetro            | Função                              |
| -------------------- | ----------------------------------- |
| `executable`         | Caminho do executável               |
| `params`             | Parâmetros de inicialização         |
| `username`           | Usuário utilizado na autenticação   |
| `encrypted_password` | Credencial utilizada pela automação |
| `save_path`          | Caminho do arquivo gerado           |

---

## `[edge]`

Configura o acesso automatizado pelo Microsoft Edge.

```ini
[edge]
site = http://site.com.br/login.asp
username = user.name
encrypted_password = password
```

A automação utiliza o navegador para acessar o endereço configurado e realizar o processo de autenticação.

---

## `[Execucao]`

Controla quais componentes devem ser executados:

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

Essas opções permitem ativar/desativar componentes e definir o comportamento da execução.

---

# ⚙️ Fluxo de automação

O fluxo conceitual é:

```text
┌──────────────────────┐
│    Início da rotina  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Ler config.ini       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Validar configurações│
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Executar Fathos      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Processar informações│
│       do censo       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Gerar arquivo        │
│       Excel/XLS      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Executar Edge        │
│    quando habilitado │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       Concluído      │
└──────────────────────┘
```

---

# 🖥️ Meu IP

O utilitário `Meu_IP` fornece uma interface gráfica simples.

O programa utiliza:

```python
socket.gethostname()
socket.gethostbyname(hostname)
```

para obter:

* hostname;
* endereço IP associado ao hostname.

Depois, apresenta essas informações em uma janela Tkinter.

Exemplo de saída:

```text
Hostname: COMPUTADOR-01
IP: 192.168.1.100
```

> O endereço retornado depende da resolução de hostname configurada no sistema. Em máquinas com múltiplas interfaces ou configurações de rede mais complexas, o resultado pode não representar todos os endereços IP disponíveis.

---

# 🛠️ Suporte remoto

O diretório:

```text
UltraVNC_Remote/
```

é destinado aos recursos relacionados a suporte remoto.

A organização desse componente permite manter ferramentas de suporte separadas das automações de processamento de dados.

---

# 🔐 Segurança

Este projeto merece atenção especial porque algumas automações trabalham com **credenciais, sistemas internos e dados operacionais**.

## 🔴 Nunca publique credenciais reais

O arquivo de configuração utiliza campos como:

```ini
username = user.name
encrypted_password = password
```

Esses campos podem representar informações sensíveis.

Nunca faça commit de:

* senhas reais;
* tokens;
* credenciais;
* chaves privadas;
* cookies de autenticação;
* arquivos de configuração contendo segredos;
* dados pessoais ou hospitalares.

---

## 🔒 Recomendação

Utilize um arquivo local:

```text
config.ini
```

e mantenha um modelo versionável:

```text
config.example.ini
```

Exemplo:

```ini
[Fathos]
executable = C:\CAMINHO\Fathos.exe
params = agfaprod, %profile%
username = SEU_USUARIO
encrypted_password = SUA_CREDENCIAL
save_path = C:\CAMINHO\resultado.xls
```

O arquivo real deve permanecer fora do controle de versão quando contiver informações sensíveis.

---

# 🏥 Dados sensíveis

Como o projeto está relacionado a um ambiente hospitalar, deve-se ter atenção adicional com:

* dados de pacientes;
* informações administrativas;
* arquivos de censo;
* credenciais;
* URLs internas;
* identificadores de funcionários;
* arquivos Excel gerados;
* logs;
* capturas de tela.

> **Nunca utilize dados reais em exemplos públicos sem anonimização adequada.**

---

# 🌐 Segurança de automação web

As automações que utilizam navegador devem considerar:

* credenciais armazenadas;
* sessões autenticadas;
* cookies;
* WebDriver;
* URLs internas;
* certificados;
* permissões do usuário;
* exposição de informações no navegador.

Também é recomendável manter o navegador e o WebDriver compatíveis e atualizados conforme a política do ambiente.

---

# 🧪 Validação

Antes de executar uma automação:

### Python

```bash
python --version
```

### Verificar sintaxe

```bash
python -m py_compile arquivo.py
```

### Dependências

Quando existir `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

---

## Validação de configuração

Antes de executar:

* confirme os caminhos;
* confirme os executáveis;
* confirme as dependências;
* confirme as credenciais;
* confirme as opções de execução;
* confirme o diretório de saída.

---

# 🐛 Troubleshooting

## Fathos não inicia

Verifique:

```text
[Fathos]
executable = C:\CAMINHO\Fathos.exe
```

Confirme se:

* o arquivo existe;
* o caminho está correto;
* o usuário possui permissão;
* os parâmetros estão corretos.

---

## Edge não inicia

Verifique:

* Microsoft Edge instalado;
* Edge WebDriver disponível;
* compatibilidade entre navegador e WebDriver;
* caminho do driver;
* permissões;
* configuração `[edge]`.

---

## Arquivo XLS não é gerado

Verifique:

```ini
save_path = C:\CAMINHO\arquivo.xls
```

Confirme:

* diretório existente;
* permissão de escrita;
* espaço em disco;
* execução correta do Fathos;
* comportamento da versão utilizada.

---

## IP não encontrado

O utilitário `Meu_IP` utiliza resolução de hostname.

Se ocorrer:

```text
IP não encontrado
```

verifique:

```bash
hostname
```

e a configuração de rede/DNS da máquina.

---

# 📦 Dependências

As dependências variam por projeto.

### `Atualiza_censo_v6`

Possui:

```text
requirements.txt
```

### `Atualize_Censo`

Possui:

```text
requeriments.txt
```

> Recomenda-se padronizar futuramente o nome para `requirements.txt`.

### `Meu_IP`

Possui:

```text
requirements.txt
```

O utilitário utiliza módulos da biblioteca padrão Python, incluindo `socket` e `tkinter`.

---

# 📋 Boas práticas

## Organização

Cada automação deve possuir:

```text
projeto/
├── README.md
├── requirements.txt
├── src/
└── config.example.ini
```

quando a complexidade justificar essa estrutura.

---

## Versionamento

Evite manter várias versões sem identificação clara.

Em vez de:

```text
script_v5.7.py
script_v5.8.py
script_v6.0.py
script_v6.1.py
```

uma evolução futura poderia utilizar:

```text
git tag v5.8.0
git tag v6.0.0
```

mantendo o histórico no Git.

---

## Dependências

Sempre que possível:

```bash
python -m venv .venv
```

Ativar no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar:

```bash
python -m pip install -r requirements.txt
```

---

<!-- # 🛣️ Roadmap

* [ ] Padronizar estrutura dos projetos
* [ ] Padronizar `requirements.txt`
* [ ] Criar `config.example.ini`
* [ ] Remover credenciais de arquivos versionados
* [ ] Adicionar `.gitignore` adequado
* [ ] Centralizar documentação de instalação
* [ ] Criar ambientes virtuais Python
* [ ] Adicionar logging estruturado
* [ ] Melhorar tratamento de exceções
* [ ] Adicionar testes automatizados
* [ ] Adicionar linting Python
* [ ] Padronizar versões
* [ ] Criar releases
* [ ] Adicionar GitHub Actions
* [ ] Documentar instalação do WebDriver
* [ ] Melhorar automação de execução diária
* [ ] Criar configuração externa para ambientes diferentes
* [ ] Adicionar mecanismos mais seguros para gerenciamento de credenciais
-->

---

# 🤝 Contribuindo

Contribuições são bem-vindas.

Antes de enviar um Pull Request:

1. leia a documentação do projeto alterado;
2. não inclua credenciais;
3. não inclua dados hospitalares reais;
4. teste a automação;
5. valide as dependências;
6. documente alterações de configuração;
7. mantenha compatibilidade com o ambiente suportado.

### Fluxo recomendado

```bash
git checkout -b feat/nova-automacao
```

Depois:

```bash
git add .
git commit -m "feat: adiciona nova automação"
git push origin feat/nova-automacao
```

---

# 📄 Licença

Este projeto está distribuído sob a licença **Apache License 2.0**.

Consulte o arquivo [`LICENSE`](LICENSE) para obter os termos completos.

---

# ⚠️ Aviso

> **Este projeto foi desenvolvido para um ambiente específico e pode depender de sistemas, caminhos, credenciais, aplicações e infraestrutura interna.**

Antes de reutilizar qualquer automação:

* revise o código;
* revise as configurações;
* substitua caminhos específicos do ambiente;
* remova credenciais;
* valide dependências;
* teste em ambiente controlado.

Não execute automações em ambientes de produção sem compreender completamente seus efeitos.

---

# ⭐ Contribua

Se este projeto for útil para seus estudos de:

* Python;
* automação;
* suporte técnico;
* administração de sistemas;
* Selenium;
* infraestrutura;
* desenvolvimento de ferramentas internas;

considere deixar uma ⭐ no repositório.

---

<p align="center">
  <strong>Automação • Suporte • Infraestrutura • Python</strong>
  <br>
  <sub>Automatizar tarefas • Reduzir trabalho manual • Documentar processos</sub>
</p>
