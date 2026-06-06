# 📊 Sistema de Gestão Empresarial - Asserti

> Uma plataforma inteligente para gerenciar empresas, acompanhar indicadores estratégicos e gerar relatórios analíticos em tempo real.

---

## 🎯 Sobre o Projeto

**Sistema de Gestão Empresarial** é uma aplicação web desenvolvida em Python com foco em facilitar o gerenciamento de dados empresariais, análise de KPIs (Indicadores-Chave de Desempenho) e geração de relatórios estruturados em PDF.

O projeto combina uma arquitetura em camadas bem definida com boas práticas de programação orientada a objetos, garantindo código limpo, manutenível e escalável.

---

## ✨ Características Principais

- 🔐 **Autenticação Segura**: Login e cadastro de usuários com senhas criptografadas
- 🏢 **CRUD de Empresas**: Criar, consultar, editar e deletar informações de empresas
- 📈 **Dashboard de KPIs**: Visualização em tempo real de 8 indicadores estratégicos
- 📄 **Geração de Relatórios**: Exportação de análises em PDF com um clique
- 🔍 **Busca Avançada**: Filtro por razão social, nome fantasia ou CNPJ
- 📊 **Análise de Dados**: Cálculos de mediana, faturamento total, setores líderes
- ♻️ **Práticas ESG/ODS**: Rastreamento de empresas com práticas sustentáveis

---

## 🛠️ Stack Tecnológico

| Componente | Tecnologia | Versão |
|-----------|-----------|--------|
| **Frontend** | Streamlit | 1.57.0 |
| **Backend** | Python | 3.14.4 |
| **Banco de Dados** | SQLite | 3 |
| **ORM/Queries** | SQL Puro | - |
| **Manipulação de Dados** | Pandas | 3.0.3 |
| **Geração de PDF** | ReportLab | 4.5.1 |
| **Criptografia** | bcrypt | 5.0.0 |
| **Formatação** | Babel | 2.18.0 |

---

## 🏗️ Arquitetura do Projeto

O sistema segue o padrão de **arquitetura em camadas**, permitindo separação de responsabilidades e facilita testes e manutenção:

```
sistema-gestao-asserti/
│
├── 📁 database/              # Camada de dados
│   ├── conexao.py            # Gerenciamento de conexão SQLite
│   └── tabelas.py            # Script de criação das tabelas
│
├── 📁 models/                # Camada de modelos (Dataclasses)
│   ├── empresa.py            # Modelo: Empresa
│   └── usuario.py            # Modelo: Usuario
│
├── 📁 repositories/          # Camada de acesso a dados
│   ├── empresa_repository.py # Operações CRUD de empresas
│   └── usuario_repository.py # Operações de usuário
│
├── 📁 services/              # Camada de negócios
│   └── relatorio.py          # Geração de relatórios PDF
│
├── 📁 utils/                 # Utilitários
│   ├── calcular_kpis.py      # Cálculo de indicadores
│   ├── catalogos.py          # Dados estáticos (estados, setores)
│   ├── criptografia.py       # Funções de hash e validação
│   ├── estilo.py             # CSS/Styling para UI
│   ├── formatacao.py         # Formatação de dados (moeda, CNPJ)
│   ├── navegacao.py          # Controle de páginas
│   ├── validacao.py          # Validação de entradas
│   └── formulario.py         # Gerenciamento de formulários
│
├── 📁 ui/                    # Camada de apresentação (Streamlit)
│   ├── 📁 auth/              # Autenticação
│   │   ├── entrada.py        # Página inicial
│   │   ├── login_usuario.py  # Login
│   │   └── cadastro_usuario.py # Cadastro
│   │
│   └── 📁 system/            # Sistema principal
│       ├── dashboard.py      # Dashboard principal
│       ├── barra_acoes.py    # Barra de ações (CRUD)
│       ├── listar_empresas.py # Tabela de empresas
│       ├── cadastro_empresa.py # Formulário de cadastro
│       ├── editar_empresa.py # Formulário de edição
│       ├── deletar_empresas.py # Confirmação de deleção
│       ├── formulario_empresa.py # Componentes do formulário
│       └── kpis.py           # Painel de indicadores
│
├── main.py                   # Ponto de entrada
└── requirements.txt          # Dependências do projeto
```

---

## 🔐 Autenticação e Segurança

### Login e Cadastro
- **Registro de usuários** com validação de nome (8-12 caracteres, apenas letras) e senha (mínimo 8 caracteres)
- **Senhas criptografadas** usando bcrypt com salt automático
- **Persistência de sessão** para manter o usuário autenticado
- **Proteção contra força bruta** através de validações rígidas

### Fluxo de Autenticação
```
Entrada (Portal) → Login / Cadastro → Dashboard (Autenticado)
```

---

## 📋 Funcionalidades Principais

### 1. 🏢 Gestão de Empresas (CRUD)

#### Criar
- Formulário com campos: razão social, nome fantasia, CNPJ, setor TI, localização, faturamento, número de colaboradores
- Validação de dados obrigatórios
- Verificação de duplicatas (razão social + CNPJ únicos)

#### Ler/Listar
- Visualização em tabela interativa
- Busca em tempo real por razão social, nome fantasia ou CNPJ
- Seleção múltipla de empresas

#### Editar
- Edição individual de empresas
- Validação de unicidade ao alterar razão social ou CNPJ
- Persistência automática das alterações

#### Deletar
- Deleção múltipla com confirmação
- Feedback visual de sucesso

### 2. 📊 Dashboard de KPIs

Acompanhe 8 indicadores essenciais em tempo real:

| KPI | Descrição | Valor Padrão |
|-----|-----------|--------------|
| 🏢 **Total de Empresas** | Quantidade total cadastrada | 0 |
| 💰 **Faturamento Total** | Soma de faturamento anual | R$ 0,00 |
| 📊 **Mediana de Faturamento** | Valor central de faturamento | R$ 0,00 |
| 🚀 **Maior Faturamento** | Maior valor anual registrado | R$ 0,00 |
| 🌎 **Estado Líder** | Estado com maior faturamento | Nenhum |
| 🧭 **Setor Líder** | Setor TI com maior faturamento | Nenhum |
| 🏭 **Setor Mais Comum** | Setor com mais empresas | Nenhum |
| ♻️ **Empresas com ESG/ODS** | Percentual com práticas sustentáveis | 0% |

### 3. 📄 Relatórios em PDF

- Geração automatizada de relatórios estruturados
- Consolidação de todos os KPIs em um documento
- Download direto pela interface
- Formatação profissional com título e dados tabulados

---

## 🧬 Programação Orientada a Objetos

### Modelos (Dataclasses)

#### Classe `Empresa`
```python
@dataclass
class Empresa:
    razao_social: str          # Identificação legal
    nome_fantasia: str         # Nome comercial
    cnpj: str                  # CNPJ (14 dígitos)
    setor_ti: str              # Setor de TI
    cidade: str                # Localização
    estado: str                # UF
    faturamento_anual: float   # Faturamento em R$
    colaboradores: int         # Número de funcionários
    exporta: bool              # Flag exportação
    praticas_esg_ods: bool     # Flag ESG/ODS
```

#### Classe `Usuario`
```python
@dataclass
class Usuario:
    nome: str                  # Nome de usuário
    senha: str                 # Senha criptografada (hash)
```

### Repositories (Padrão Repository)

#### `EmpresaRepository`
Responsável por todas operações com empresas no banco:
- `cadastrar_empresa(empresa)` - Insert
- `buscar_empresa(termo)` - Select com filtro
- `listar_empresas()` - Select all
- `verificar_existencia(razao_social, cnpj)` - Check duplicatas
- `editar_empresa(id, empresa)` - Update
- `deletar_empresas(ids)` - Delete múltiplo

#### `UsuarioRepository`
Responsável por operações de autenticação:
- `cadastrar_usuario(usuario)` - Insert
- `buscar_usuario(nome)` - Select para validação

---

## 🗄️ Banco de Dados

### SQLite3
Database local em arquivo `sistema.db` com estrutura simples e eficiente.

### Tabelas

#### `usuarios`
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
```
- **id**: Identificador único
- **nome**: Username único
- **senha**: Hash bcrypt

#### `empresas`
```sql
CREATE TABLE empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    razao_social TEXT NOT NULL UNIQUE,
    nome_fantasia TEXT,
    cnpj TEXT NOT NULL UNIQUE,
    setor_ti TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    faturamento_anual REAL,
    colaboradores INTEGER DEFAULT 0,
    exporta INTEGER DEFAULT 0,
    praticas_esg_ods INTEGER DEFAULT 0
)
```
- **razao_social** e **cnpj**: Únicos para evitar duplicatas
- **exporta** e **praticas_esg_ods**: Booleans armazenados como INTEGER (0/1)
- **colaboradores**: Padrão 0 se não informado

---

## 📋 Requisitos

- Python 3.9+
- pip (gerenciador de pacotes)

---

## 🚀 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/sistema-gestao-asserti.git
cd sistema-gestao-asserti
```

### 2. Crie um ambiente virtual
```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

**Windows (PowerShell):**
```bash
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação
```bash
streamlit run main.py
```

A aplicação abrirá em `http://localhost:8501`

---

## 📖 Como Usar

### 1. **Primeira Execução**
- Clique em **"📋 Criar novo cadastro"** para registrar um usuário
- Preencha nome (8-12 letras) e senha (mín. 8 caracteres)

### 2. **Login**
- Digite suas credenciais na tela de **"🔐 Acessar conta"**
- Você será redirecionado ao dashboard

### 3. **Gerenciar Empresas**
- **Cadastrar**: Clique em **"➕ CADASTRAR"** e preencha o formulário
- **Listar**: Empresas aparecem em tabela interativa
- **Buscar**: Use o campo de busca para filtrar
- **Editar**: Selecione uma empresa e clique em **"📝 EDITAR"**
- **Deletar**: Selecione uma ou mais e clique em **"❌ DELETAR"**

### 4. **Analisar Indicadores**
- Veja os **8 KPIs** no topo do dashboard
- Acompanhe faturamento, setores e práticas sustentáveis em tempo real

### 5. **Gerar Relatório**
- Clique em **"📄 Baixar relatório PDF"** para exportar análise consolidada

---

## 🧪 Validações Implementadas

| Campo | Regra |
|-------|-------|
| **Nome de usuário** | 8-12 caracteres, apenas letras |
| **Senha** | Mínimo 8 caracteres |
| **CNPJ** | Exatamente 14 dígitos, apenas números |
| **Razão Social** | Obrigatória, máx. 80 caracteres, única |
| **Cidade** | Apenas letras e espaços |
| **Colaboradores** | Mínimo 1 |
| **Faturamento** | Número positivo em R$ |

---

## 📦 Dependências Principais

```
Babel==2.18.0          # Formatação de moedas
bcrypt==5.0.0          # Criptografia de senhas
pandas==3.0.3          # Manipulação de dados
streamlit==1.57.0      # Framework web
reportlab==4.5.1       # Geração de PDF
```

---

## 🎓 Projeto Acadêmico

Este é um projeto desenvolvido como trabalho de faculdade, demonstrando:

✅ Arquitetura em camadas  
✅ Programação orientada a objetos  
✅ Padrão Repository  
✅ Validação de dados  
✅ Criptografia de senhas  
✅ Geração de relatórios  
✅ Interface responsiva  
✅ Boas práticas de código  

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**João Victor Valencio Silva**  
Projeto de Gestão Empresarial - 2026

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Fazer pull requests

---

**Desenvolvido com ❤️ e Python**
