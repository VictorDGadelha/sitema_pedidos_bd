# 🍔 Sistema de Gerenciamento para Lanchonete

> Sistema web acadêmico desenvolvido com **Python + Django + PostgreSQL** para gerenciamento de clientes, produtos, pedidos e relatórios interativos.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-Framework-green?style=flat-square&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=flat-square&logo=postgresql)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=flat-square&logo=bootstrap)

---

## 📚 Tecnologias

| Camada | Tecnologias |
|--------|------------|
| Backend | Python 3, Django |
| Banco de dados | PostgreSQL, Views SQL, Triggers PL/pgSQL |
| Frontend | HTML5, Bootstrap 5 |

---

## ⚙️ Funcionalidades

### 👤 Clientes
- Cadastro, edição, exclusão e listagem

### 🍔 Produtos
- Cadastro por categoria, controle de estoque, ativação/inativação

### 📦 Pedidos
- Criação de pedidos com cálculo automático de subtotal/total e controle de status

### 📊 Relatórios
- Relatório consolidado de vendas com filtros por cliente, produto e status

### 🛒 Estoque
- Validação e redução automática via Trigger, com proteção contra estoque negativo

---

## 🧱 Modelagem
Cliente
└── Pedido
└── ItemPedido
└── Produto
└── Categoria

---

## 🚀 Como rodar

```bash
# 1. Clone e entre na pasta
git clone URL_DO_REPOSITORIO
cd projeto_lanchonete

# 2. Ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 3. Dependências
pip install django psycopg2

# 4. Configure o banco em config/settings.py
# NAME: lanchonete_db | USER: postgres | PASSWORD: SUA_SENHA

# 5. Migrations e superusuário
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 6. Rodar
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000/` — Admin: `http://127.0.0.1:8000/admin`

---

## 🧠 VIEW SQL — Relatório de Vendas

```sql
CREATE OR REPLACE VIEW vw_relatorio_vendas AS
SELECT
    ped.id         AS pedido_id,
    c.nome         AS cliente,
    pr.nome        AS produto,
    ip.quantidade,
    ip.subtotal,
    ped.data_pedido,
    ped.status
FROM pedidos_itempedido ip
JOIN pedidos_pedido  ped ON ped.id = ip.pedido_id
JOIN clientes_cliente  c ON c.id  = ped.cliente_id
JOIN produtos_produto pr ON pr.id = ip.produto_id;
```

> Usada para gerar relatórios consolidados com JOINs entre tabelas, facilitando consultas analíticas.

---

## ⚡ TRIGGER — Controle de Estoque

```sql
CREATE OR REPLACE FUNCTION atualizar_estoque()
RETURNS TRIGGER AS $$
DECLARE
    estoque_atual INTEGER;
BEGIN
    SELECT estoque INTO estoque_atual
    FROM produtos_produto WHERE id = NEW.produto_id;

    IF estoque_atual < NEW.quantidade THEN
        RAISE EXCEPTION 'Estoque insuficiente!';
    END IF;

    UPDATE produtos_produto
    SET estoque = estoque - NEW.quantidade
    WHERE id = NEW.produto_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_atualizar_estoque
BEFORE INSERT ON pedidos_itempedido
FOR EACH ROW EXECUTE FUNCTION atualizar_estoque();
```

> Garante integridade dos dados, impede estoque negativo e automatiza regras de negócio.

---

## 📌 Melhorias Futuras

- [ ] Login e autenticação de usuários
- [ ] Exportação para CSV / Excel
- [ ] Dashboard com gráficos analíticos
- [ ] API REST
- [ ] Docker e deploy online
- [ ] Sistema de comandas e área de caixa

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos com Django, PostgreSQL, SQL avançado e Bootstrap.

> 📄 Licença de uso acadêmico
