# 🚀 School AI Platform

Plataforma educacional inteligente com IA para auxiliar professores na criação de aulas, avaliações e gestão de desempenho dos alunos.

---

## 📌 Sobre o Projeto

O **School AI Platform** é um sistema que integra:

- 📊 Gestão de notas e avaliações
- 🤖 Geração automática de conteúdos com IA
- 📝 Criação de provas com gabarito
- 🎯 Estrutura pensada para evolução em SaaS educacional

---

## 🧠 Problema que resolve

Professores gastam muito tempo com:

- Planejamento de aulas
- Criação de avaliações
- Organização de notas

👉 Este sistema automatiza e otimiza esse processo.

---

## ⚙️ Tecnologias Utilizadas

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Frontend (Básico, apenas para visualização)
- HTML
- JavaScript

### IA
- OpenAI API (com fallback offline)

---

## 🏗️ Arquitetura

app/  
├── ai/ # Lógica de IA (Tutor + Provas)  
├── core/ # Configuração de banco  
├── models/ # Estrutura de dados  
├── routes/ # Endpoints da API  
├── schemas/ # Validação (Pydantic)  
├── services/ # Regras de negócio


---

## 🔥 Funcionalidades

### 📚 Tutor com IA
Geração automática de conteúdo didático com base em:

- Matéria
- Série
- Nível
- Tema
- Subtópicos

---

### 📝 Gerador de Provas
Criação de avaliações com:

- Questões contextualizadas
- Controle de dificuldade
- Gabarito automático

---

### 📊 Sistema de Notas
- Avaliações com peso
- Pontos positivos e negativos
- Cálculo automático da média

---

## ⚠️ Modo Offline (Importante)

Caso a API da OpenAI não esteja disponível:

👉 O sistema entra automaticamente em modo offline  
👉 Gera conteúdo básico sem quebrar a aplicação

---

## 🚀 Como Rodar o Projeto

### 1. Clonar repositório

```bash
git clone https://github.com/seu-usuario/school-ai-platform.git
cd school-ai-platform

```
### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows

```
### 3. Instalar dependências

```bash
pip install -r requirements.txt

```
### 4. Rodar backend

```bash
uvicorn app.main:app --reload

```
Acesse:

```bash
http://127.0.0.1:8000/docs

```

### 5. Rodar frontend

```bash
cd frontend
python -m http.server 5500

```
Acesse:

```bash
http://localhost:5500

```

## 🔗 Endpoints principais

📚 Gerar Aula
```
POST /ai/lesson
```
📝 Gerar Prova
```
POST /exam/
```
📊 Calcular Nota
```
POST /grades/calculate
```
### 💡 Possíveis Evoluções  
🔐 Autenticação de professores (JWT)  
📊 Dashboard com gráficos  
🏫 Multi-escolas (SaaS)  
📚 Integração com BNCC  
🤖 IA adaptativa baseada no desempenho do aluno  

### 🎯 Objetivo do Projeto

Demonstrar:

Arquitetura de backend sólida  
Integração com IA  
Pensamento de produto  
Aplicação prática na educação  

### 👨‍💻 Autor

Anderson Nunes  
Engenhario de Software + Professor


