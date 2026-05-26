# 🍔 Sistema de Gerenciamento para Lanchonete

Sistema web desenvolvido com **Python + Django + PostgreSQL** para gerenciamento de clientes, produtos, pedidos e relatórios interativos de uma lanchonete.

O projeto foi desenvolvido com foco acadêmico utilizando:
- CRUD completo
- Relacionamentos entre tabelas
- Controle de estoque
- VIEW SQL
- TRIGGER PostgreSQL
- Relatórios dinâmicos

---

# 📚 Tecnologias Utilizadas

## Backend
- Python 3
- Django

## Banco de Dados
- PostgreSQL

## Frontend
- HTML5
- Bootstrap 5

## Banco / SQL
- Views SQL
- Triggers PostgreSQL
- JOINs
- Queries dinâmicas

---

# ⚙️ Funcionalidades do Sistema

## 👤 Clientes
- Cadastro de clientes
- Edição
- Exclusão
- Listagem

---

## 🍔 Produtos
- Cadastro de produtos
- Controle de estoque
- Categorias
- Ativação/Inativação

---

## 📦 Pedidos
- Criação de pedidos
- Adição de produtos
- Cálculo automático de subtotal
- Cálculo automático de total
- Controle de status

---

## 📊 Relatórios
- Relatório completo de vendas
- Pesquisa interativa
- Filtros por:
  - cliente
  - produto
  - status

---

## 🛒 Controle de Estoque
- Validação de estoque
- Redução automática de estoque
- Proteção contra estoque negativo

---

# 🗂️ Estrutura do Projeto

```bash
projeto_lanchonete/
│
├── clientes/
├── produtos/
├── pedidos/
├── config/
├── manage.py
└── requirements.txt
🧱 Modelagem do Sistema
Relacionamentos
Cliente
   │
   └── Pedido
            │
            └── ItemPedido
                         │
                         └── Produto
                                      │
                                      └── Categoria
🚀 Como Rodar o Projeto
1️⃣ Clonar o repositório
git clone URL_DO_REPOSITORIO
2️⃣ Entrar na pasta do projeto
cd projeto_lanchonete
3️⃣ Criar ambiente virtual
Windows
python -m venv venv
4️⃣ Ativar ambiente virtual
Windows
venv\Scripts\activate
5️⃣ Instalar dependências
pip install django
pip install psycopg2
6️⃣ Criar banco PostgreSQL

Criar banco chamado:

lanchonete_db
7️⃣ Configurar banco no Django
Arquivo:
config/settings.py
Configuração:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lanchonete_db',
        'USER': 'postgres',
        'PASSWORD': 'SUA_SENHA',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
8️⃣ Rodar migrations
python manage.py makemigrations
python manage.py migrate
9️⃣ Criar superusuário
python manage.py createsuperuser
🔟 Rodar servidor
python manage.py runserver
🌐 Acessar sistema
Sistema
http://127.0.0.1:8000/
Admin Django
http://127.0.0.1:8000/admin
🧠 Onde foi utilizada VIEW
VIEW SQL criada:
CREATE OR REPLACE VIEW vw_relatorio_vendas AS

SELECT

    ped.id AS pedido_id,

    c.nome AS cliente,

    pr.nome AS produto,

    ip.quantidade,

    ip.subtotal,

    ped.data_pedido,

    ped.status

FROM pedidos_itempedido ip

JOIN pedidos_pedido ped
ON ped.id = ip.pedido_id

JOIN clientes_cliente c
ON c.id = ped.cliente_id

JOIN produtos_produto pr
ON pr.id = ip.produto_id;
🎯 Objetivo da VIEW

A VIEW foi utilizada para:

gerar relatório consolidado
realizar JOINs entre tabelas
facilitar consultas analíticas
criar relatórios interativos
⚡ Onde foi utilizada TRIGGER
Função PostgreSQL:
CREATE OR REPLACE FUNCTION atualizar_estoque()
RETURNS TRIGGER AS
$$

DECLARE

    estoque_atual INTEGER;

BEGIN

    SELECT estoque
    INTO estoque_atual
    FROM produtos_produto
    WHERE id = NEW.produto_id;

    IF estoque_atual < NEW.quantidade THEN

        RAISE EXCEPTION
        'Estoque insuficiente!';

    END IF;

    UPDATE produtos_produto
    SET estoque = estoque - NEW.quantidade
    WHERE id = NEW.produto_id;

    RETURN NEW;

END;

$$ LANGUAGE plpgsql;
Trigger
CREATE TRIGGER trg_atualizar_estoque

BEFORE INSERT
ON pedidos_itempedido

FOR EACH ROW

EXECUTE FUNCTION atualizar_estoque();
🎯 Objetivo da TRIGGER

A trigger foi utilizada para:

atualizar estoque automaticamente
impedir estoque negativo
garantir integridade dos dados
automatizar regras de negócio
📈 Pesquisa Interativa

O sistema possui:

pesquisa dinâmica
filtros personalizados
relatórios interativos
Filtros disponíveis:
Cliente
Produto
Status
📌 Melhorias Futuras
Login e autenticação
Exportação CSV/Excel
Dashboard administrativo
API REST
Docker
Deploy online
Gráficos analíticos
Sistema de comandas
Área de caixa
👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos utilizando:

Django
PostgreSQL
SQL avançado
Bootstrap
📄 Licença

Projeto de uso acadêmico.
