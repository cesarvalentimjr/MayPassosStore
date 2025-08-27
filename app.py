import streamlit as st
import pandas as pd
import os
from PIL import Image

# Configuração da página
st.set_page_config(
    page_title="May Passos Store - Catálogo",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado para seguir a identidade visual
st.markdown("""
<style>
    @import url(\'https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap\');

    .main {
        padding-top: 0rem;
    }

    .header-container {
        background-color: white;
        padding: 0rem 0;
        margin-bottom: 0rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1rem;
    }
    .logo-container img {
        max-width: 400px;   /* ajuste aqui para deixar maior/menor */
    }

    .product-card {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: box-shadow 0.3s ease;
    }

    .product-card:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    .product-name {
        font-family: \'Montserrat\', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: black;
        margin-bottom: 0.5rem;
        background-color: white;
        padding: 0.5rem;
        border-radius: 4px;
    }

    .product-price {
        font-family: \'Montserrat\', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: black;
        margin-bottom: 1rem;
        background-color: white;
        padding: 0.5rem;
        border-radius: 4px;
    }

    .product-description {
        font-family: \'Montserrat\', sans-serif;
        font-size: 1rem;
        font-weight: 400;
        color: #333;
        line-height: 1.6;
        margin-bottom: 1rem;
        background-color: white;
        padding: 0.5rem;
        border-radius: 4px;
    }

    .contact-button {
        background-color: black;
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-family: \'Montserrat\', sans-serif;
        font-size: 1rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        cursor: pointer;
        border-radius: 4px;
        transition: background-color 0.3s ease;
    }

    .contact-button:hover {
        background-color: #333;
    }

    .filter-container {
        background-color: #f8f8f8;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 2rem;
    }

    .filter-title {
        font-family: \'Montserrat\', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        color: black;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Função para carregar os dados dos produtos do Excel
@st.cache_data
def load_products_from_excel(file_path="products.xlsx"):
    try:
        df = pd.read_excel(file_path)
        # Converte o DataFrame para uma lista de dicionários
        products = df.to_dict(orient="records")
        return products
    except FileNotFoundError:
        st.error(f"Arquivo de produtos não encontrado: {file_path}")
        return []
    except Exception as e:
        st.error(f"Erro ao carregar produtos do Excel: {e}")
        return []

# Função para carregar imagem
def load_image(image_path):
    try:
        if os.path.exists(image_path):
            return Image.open(image_path)
        else:
            st.warning(f"Imagem não encontrada: {image_path}")
            return None
    except Exception as e:
        st.warning(f"Erro ao carregar imagem: {e}")
        return None

# Header da aplicação com logo centralizada
st.markdown("<div class=\"header-container\">", unsafe_allow_html=True)
st.markdown("<div class=\"logo-container\">", unsafe_allow_html=True)
st.image("logo.jpg") 
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Carregar produtos
products = load_products_from_excel()

if products:
    st.sidebar.markdown(\"<p class=\"filter-title\">Filtros</p>\", unsafe_allow_html=True)

    price_filter = st.sidebar.selectbox(
        "Faixa de Preço",
        ["Todos os preços", "Até R$ 200", "R$ 200 - R$ 400", "Acima de R$ 400"]
    )

    categories = ["Todas as categorias"]
    for product in products:
        # Adiciona categorias baseadas no nome do produto, se ainda não existirem
        if "Vestido" in product["name"] and "Vestidos" not in categories:
            categories.append("Vestidos")
        elif "Blusa" in product["name"] and "Blusas" not in categories:
            categories.append("Blusas")
        elif "Calça" in product["name"] and "Calças" not in categories:
            categories.append("Calças")
        elif "Camisa" in product["name"] and "Camisas" not in categories:
            categories.append("Camisas")
        elif "Conjunto" in product["name"] and "Conjuntos" not in categories:
            categories.append("Conjuntos")
        elif "Regata" in product["name"] and "Regatas" not in categories:
            categories.append("Regatas")
    
    category_filter = st.sidebar.selectbox("Categoria", categories)

    filtered_products = products.copy()

    if price_filter != "Todos os preços":
        temp_filtered_products = []
        for product in filtered_products:
            price_str = str(product["price"]).replace("R$ ", "").replace(",", ".")
            try:
                price_value = float(price_str)
            except ValueError:
                price_value = 0.0 # Valor padrão para preços inválidos
            
            if price_filter == "Até R$ 200" and price_value <= 200:
                temp_filtered_products.append(product)
            elif price_filter == "R$ 200 - R$ 400" and 200 < price_value <= 400:
                temp_filtered_products.append(product)
            elif price_filter == "Acima de R$ 400" and price_value > 400:
                temp_filtered_products.append(product)
        filtered_products = temp_filtered_products

    if category_filter != "Todas as categorias":
        filtered_products = [p for p in filtered_products if category_filter.rstrip(\'s\') in p["name"]]

    st.markdown(f"### Encontrados {len(filtered_products)} produto(s)")

    cols_per_row = 2
    for i in range(0, len(filtered_products), cols_per_row):
        cols = st.columns(cols_per_row)

        for j, col in enumerate(cols):
            if i + j < len(filtered_products):
                product = filtered_products[i + j]

                with col:
                    with st.container():
                        st.markdown(\"<div class=\"product-card\">\", unsafe_allow_html=True)
                        
                        # Carrossel de imagens
                        image_urls = []
                        if \'image_urls\' in product and pd.notna(product[\'image_urls\']):
                            image_urls = [url.strip() for url in str(product[\'image_urls\']).split(\,\') if url.strip()]
                        
                        if image_urls:
                            # Inicializa o índice da imagem atual no session_state
                            if f\'current_image_index_{product["id"]}\' not in st.session_state:
                                st.session_state[f\'current_image_index_{product["id"]}\' ] = 0

                            current_image_index = st.session_state[f\'current_image_index_{product["id"]}\' ]
                            
                            # Exibe a imagem atual
                            st.image(load_image(image_urls[current_image_index]), use_column_width=True)
                            
                            # Botões de navegação do carrossel
                            if len(image_urls) > 1:
                                col1_carousel, col2_carousel, col3_carousel = st.columns([1, 6, 1])
                                with col1_carousel:
                                    if st.button("◀️", key=f"prev_img_{product["id"]}"):
                                        st.session_state[f\'current_image_index_{product["id"]}\' ] = (current_image_index - 1) % len(image_urls)
                                        st.rerun()
                                with col3_carousel:
                                    if st.button("▶️", key=f"next_img_{product["id"]}"):
                                        st.session_state[f\'current_image_index_{product["id"]}\' ] = (current_image_index + 1) % len(image_urls)
                                        st.rerun()
                        else:
                            st.warning("Nenhuma imagem disponível para este produto.")

                        st.markdown(f\'<h3 class=\"product-name\">{product["name"]}</h3>\', unsafe_allow_html=True)
                        st.markdown(f\'<p class=\"product-price\">{product["price"]}</p>\', unsafe_allow_html=True)
                        st.markdown(f\'<p class=\"product-description\">{product["description"]}</p>\', unsafe_allow_html=True)

                        if st.button(f"Tenho Interesse", key=f"btn_{product[\'id\']}", help="Clique para demonstrar interesse"):
                            st.success(f"Interesse registrado em: {product[\'name\']}")
                            st.info("Entre em contato conosco pelo WhatsApp para mais informações!")

                        st.markdown(\'</div>\', unsafe_allow_html=True)

else:
    st.error("Nenhum produto encontrado!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p style="font-family: \'Montserrat\', sans-serif; font-size: 0.9rem;">
        © 2025 May Passos Store - Todos os direitos reservados
    </p>
    <p style="font-family: \'Montserrat\', sans-serif; font-size: 0.8rem;">
        Entre em contato: <a href=\"https://wa.me/5571991001682\"> (71) 99100-1682</a>
    </p>
</div>
""", unsafe_allow_html=True)
