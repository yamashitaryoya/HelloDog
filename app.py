import streamlit as st
import requests

# タイトルと説明文
st.title('🐶 Hello Dog 🐶')
st.markdown("### Welcome to the Dog Image App!")

# 犬種のリストを取得
breeds_response = requests.get('https://dog.ceo/api/breeds/list/all')
breeds_data = breeds_response.json()
breeds_list = list(breeds_data['message'].keys())

# 犬種を選択するセレクトボックス
selected_breed = st.selectbox('Select dog breed', breeds_list, help='Select a dog breed to view its image.')

# ボタンのスタイルを変更
button_style = """
    <style>
    .stButton>button {
        background-color: #ffcc00;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 12em;
        font-size: 1.2em;
        font-weight: bold;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# 画像の表示
if st.button('Come here!!'):
    # 選択された犬種の画像を取得
    image_response = requests.get(f'https://dog.ceo/api/breed/{selected_breed}/images/random')
    image_data = image_response.json()
    image_url = image_data['message']
    
    # 犬の画像を表示
    st.image(image_url, caption=f'Here is a {selected_breed} for you!', use_column_width=True)

    # 画像が表示されたことを示すメッセージ
    st.success('Enjoy your dog image! 🐕')
else:
    # 画像がない場合のプレースホルダー
    st.image('https://via.placeholder.com/300x200.png?text=Select+a+breed+and+click+the+button+to+see+the+dog+image')

# フッター
st.markdown("""
    ---
    Created with ❤️ by a Dog Lover
""")
