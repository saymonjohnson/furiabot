from PIL import Image


def resize_logo():
    try:
        img = Image.open('furia_logo_original.png')

        # Usar Resampling.LANCZOS (versões Pillow >= 9.1.0)
        img = img.resize((96, 96), resample=Image.Resampling.LANCZOS)

        img.save('furia_logo_emote.png', optimize=True, quality=85)
        print("✅ Imagem redimensionada com sucesso!")

    except Exception as e:
        print(f"❌ Erro: {e}")