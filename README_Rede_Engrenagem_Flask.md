# 🛠️ Rede Engrenagem - Projeto Flask

Sistema web simples para **registro de atividades de manutenção**, com upload de fotos, peças utilizadas, cálculo automático de custo e exibição em formato de feed.

## 🚀 Funcionalidades

- Formulário de relatos com:
  - Título, executor, descrição
  - Estrutura de Área, Subárea, Equipamento
  - Upload de **múltiplas fotos**
  - Registro de até 10 peças por relato (catálogo, descrição, quantidade)
  - Cálculo automático do custo com base no catálogo
- Página inicial estilo **rede social**:
  - Cards com relatos, fotos, peças usadas e custo total
  - Comentários abertos (sem login)
  - Visual escuro elegante com **Bootstrap 5**
- Exportação dos relatos para **Excel**

## 🧠 Foco

Este sistema é o primeiro passo para construção de um **repositório estruturado de dados de manutenção**, com potencial de ser utilizado para treinar modelos de IA no futuro.

---

## 🗂️ Estrutura de pastas

```
rede_engrenagem_flask/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── relatar.html
├── static/
│   └── uploads/
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10+
- Flask
- Pandas
- openpyxl

Instale os requisitos com:

```bash
pip install flask pandas openpyxl
```

---

## ▶️ Como rodar

1. Extraia o zip:
   ```bash
   unzip rede_engrenagem_flask.zip
   cd rede_engrenagem_flask
   ```

2. Inicie o servidor Flask:
   ```bash
   python app.py
   ```

3. Acesse pelo navegador:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📤 Exportação

Use o botão `Exportar Relatos` na tela inicial para gerar um arquivo `relatos_exportados.xlsx` com todos os dados.

---

## ✍️ Comentários

Qualquer visitante pode deixar comentários nos relatos apenas informando **nome** e **mensagem**. Ideal para feedback de técnicos e gestores.

---

## 📸 Uploads

As fotos ficam salvas na pasta `static/uploads/` automaticamente.

---

## 📌 Observação

O sistema não requer login, sendo ideal para uso em rede local (intranet) de manutenção. A segurança pode ser adicionada em futuras versões.

---

Feito com ❤️ por Hendel.
