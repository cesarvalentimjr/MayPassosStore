# May Passos Store - Catálogo Digital

Um aplicativo Streamlit elegante para exibir o catálogo de roupas femininas da May Passos Store, seguindo a identidade visual minimalista da marca.

## Características

- **Design Minimalista**: Seguindo a identidade visual da May Passos Store com esquema de cores preto e branco
- **Catálogo Responsivo**: Visualização de produtos em grid responsivo
- **Filtros Inteligentes**: Filtros por categoria e faixa de preço
- **Interface Intuitiva**: Navegação simples e elegante
- **Botão de Interesse**: Funcionalidade para demonstrar interesse nos produtos

## Estrutura do Projeto

```
may-passos-store/
├── app.py                 # Aplicativo principal do Streamlit
├── products.json          # Dados dos produtos
├── requirements.txt       # Dependências do projeto
├── images/               # Pasta com imagens dos produtos
│   ├── vestido_midi_elegance.png
│   ├── blusa_seda_classica.png
│   └── calca_pantalona_conforto.png
├── design_guidelines.md   # Diretrizes de design
└── README.md             # Este arquivo
```

## Como Executar Localmente

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o aplicativo:
   ```bash
   streamlit run app.py
   ```
4. Acesse `http://localhost:8501` no seu navegador

## Deploy no Streamlit Cloud

1. Faça upload dos arquivos para um repositório GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte sua conta GitHub
4. Selecione o repositório e o arquivo `app.py`
5. Clique em "Deploy"

## Personalização

### Adicionando Novos Produtos

Edite o arquivo `products.json` seguindo a estrutura:

```json
{
  "id": "4",
  "name": "Nome do Produto",
  "price": "R$ 000,00",
  "description": "Descrição detalhada do produto",
  "image_url": "images/nome_da_imagem.png"
}
```

### Modificando Cores e Estilos

As cores e estilos podem ser modificados no arquivo `app.py` na seção de CSS customizado.

## Tecnologias Utilizadas

- **Streamlit**: Framework para aplicações web em Python
- **Pillow**: Processamento de imagens
- **JSON**: Armazenamento de dados dos produtos

## Identidade Visual

O aplicativo segue rigorosamente a identidade visual da May Passos Store:
- **Cores**: Preto (#000000) e Branco (#FFFFFF)
- **Tipografia**: Montserrat (sans-serif moderna)
- **Estilo**: Minimalista, elegante e limpo

## Contato

Para mais informações sobre a May Passos Store, entre em contato através dos canais oficiais da loja.

