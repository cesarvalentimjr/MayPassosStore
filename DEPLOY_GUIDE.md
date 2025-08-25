# Guia de Deploy - May Passos Store Catalog

## Passo a Passo para Deploy no Streamlit Cloud

### 1. Preparação do Repositório GitHub

1. **Criar um novo repositório no GitHub:**
   - Acesse [github.com](https://github.com) e faça login
   - Clique em "New repository"
   - Nome sugerido: `may-passos-store-catalog`
   - Marque como "Public" (necessário para Streamlit Cloud gratuito)
   - Clique em "Create repository"

2. **Upload dos arquivos:**
   - Extraia o arquivo `may-passos-store-catalog.zip`
   - Faça upload de todos os arquivos para o repositório GitHub
   - Ou use Git se preferir:
     ```bash
     git clone https://github.com/SEU_USUARIO/may-passos-store-catalog.git
     cd may-passos-store-catalog
     # Copie todos os arquivos do projeto aqui
     git add .
     git commit -m "Initial commit - May Passos Store Catalog"
     git push origin main
     ```

### 2. Deploy no Streamlit Cloud

1. **Acesse o Streamlit Cloud:**
   - Vá para [share.streamlit.io](https://share.streamlit.io)
   - Clique em "Sign up" ou "Sign in"
   - Conecte sua conta GitHub

2. **Criar nova aplicação:**
   - Clique em "New app"
   - Selecione o repositório `may-passos-store-catalog`
   - Branch: `main` (ou `master`)
   - Main file path: `app.py`
   - App URL (opcional): `may-passos-store` ou similar

3. **Deploy:**
   - Clique em "Deploy!"
   - Aguarde alguns minutos para o deploy ser concluído
   - Sua aplicação estará disponível em uma URL como: `https://may-passos-store.streamlit.app`

### 3. Configurações Adicionais (Opcional)

#### Domínio Personalizado
- No Streamlit Cloud, vá em Settings > General
- Configure um domínio personalizado se desejar

#### Secrets (se necessário no futuro)
- Para configurações sensíveis, use o arquivo de secrets do Streamlit Cloud
- Vá em Settings > Secrets

### 4. Atualizações Futuras

Para atualizar o catálogo:

1. **Adicionar novos produtos:**
   - Edite o arquivo `products.json`
   - Adicione as imagens na pasta `images/`
   - Faça commit das mudanças no GitHub

2. **Modificar o design:**
   - Edite o arquivo `app.py`
   - Modifique o CSS na seção de estilos
   - Faça commit das mudanças

3. **Deploy automático:**
   - O Streamlit Cloud fará deploy automático a cada commit no repositório

### 5. Estrutura de Dados dos Produtos

Para adicionar novos produtos, siga esta estrutura no `products.json`:

```json
{
  "id": "ID_UNICO",
  "name": "Nome do Produto",
  "price": "R$ 000,00",
  "description": "Descrição detalhada do produto com tamanhos e características",
  "image_url": "images/nome_da_imagem.png"
}
```

### 6. Otimizações Recomendadas

1. **Imagens:**
   - Use imagens em formato PNG ou JPG
   - Resolução recomendada: 800x800 pixels
   - Tamanho máximo: 1MB por imagem

2. **Performance:**
   - O cache está configurado para otimizar o carregamento
   - Evite arquivos muito grandes

3. **SEO:**
   - O título da página está configurado como "May Passos Store - Catálogo"
   - Adicione meta tags se necessário

### 7. Suporte e Manutenção

- **Logs:** Acesse os logs no Streamlit Cloud para debug
- **Monitoring:** O Streamlit Cloud fornece métricas básicas de uso
- **Updates:** Mantenha as dependências atualizadas no `requirements.txt`

### 8. Custos

- **Streamlit Cloud:** Gratuito para repositórios públicos
- **GitHub:** Gratuito para repositórios públicos
- **Domínio personalizado:** Opcional, custos variam

### 9. Backup

- Mantenha sempre um backup local dos arquivos
- O GitHub serve como backup automático
- Considere fazer backup das imagens separadamente

---

**Contato para Suporte Técnico:**
Em caso de dúvidas técnicas, consulte a documentação oficial do Streamlit ou entre em contato com o desenvolvedor do projeto.

