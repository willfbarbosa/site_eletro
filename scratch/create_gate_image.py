import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Canvas size 16:9 (1280x720)
W, H = 1280, 720
img = Image.new('RGB', (W, H), color='#0a0a0a')
draw = ImageDraw.Draw(img)

# Background subtle dark gradient grid pattern
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill='#141414', width=1)
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill='#141414', width=1)

# Red ambient glow on the left
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow)
glow_draw.ellipse([30, 80, 550, 650], fill=(230, 17, 31, 40))
glow = glow.filter(ImageFilter.GaussianBlur(80))
img.paste(glow, (0, 0), glow)

# Load user photo
photo_path = r'C:\Users\willian\.gemini\antigravity-ide\brain\0872212b-bce7-4f72-a2e8-cd0f8db24005\.user_uploaded\media_1791286990971.png'
if os.path.exists(photo_path):
    user_img = Image.open(photo_path).convert('RGBA')
    
    # Fit inside a nice frame on the left side
    target_h = 580
    aspect = user_img.width / user_img.height
    target_w = int(target_h * aspect)
    
    user_img_resized = user_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Position photo on left
    photo_x = 70
    photo_y = 70
    
    # Draw dark shadow behind photo
    shadow = Image.new('RGBA', (target_w + 30, target_h + 30), (0, 0, 0, 200))
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))
    img.paste(shadow, (photo_x - 15, photo_y - 15), shadow)
    
    # Paste photo
    img.paste(user_img_resized, (photo_x, photo_y), user_img_resized)
    
    # Red bracket border around photo
    bx, by, bw, bh = photo_x, photo_y, target_w, target_h
    # Top-Left corner
    draw.line([(bx-6, by-6), (bx+35, by-6)], fill='#e6111f', width=4)
    draw.line([(bx-6, by-6), (bx-6, by+35)], fill='#e6111f', width=4)
    # Top-Right corner
    draw.line([(bx+bw+6, by-6), (bx+bw-35, by-6)], fill='#e6111f', width=4)
    draw.line([(bx+bw+6, by-6), (bx+bw+6, by+35)], fill='#e6111f', width=4)
    # Bottom-Left corner
    draw.line([(bx-6, by+bh+6), (bx+35, by+bh+6)], fill='#e6111f', width=4)
    draw.line([(bx-6, by+bh+6), (bx-6, by+bh-35)], fill='#e6111f', width=4)
    # Bottom-Right corner
    draw.line([(bx+bw+6, by+bh+6), (bx+bw-35, by+bh+6)], fill='#e6111f', width=4)
    draw.line([(bx+bw+6, by+bh+6), (bx+bw+6, by+bh-35)], fill='#e6111f', width=4)

# Right side content panel
panel_x = 510
draw.rectangle([panel_x, 70, W - 60, H - 70], outline='#2c2c2c', fill='#121212', width=2)
# Panel header line
draw.line([(panel_x, 70), (W - 60, 70)], fill='#e6111f', width=4)

# Text fonts
try:
    font_title = ImageFont.truetype("arialbd.ttf", 34)
    font_sub = ImageFont.truetype("arialbd.ttf", 18)
    font_bold = ImageFont.truetype("arialbd.ttf", 20)
    font_body = ImageFont.truetype("arial.ttf", 17)
except:
    font_title = font_sub = font_bold = font_body = ImageFont.load_default()

draw.text((panel_x + 35, 105), "AUTOMAÇÃO DE PORTÕES", fill='#e6111f', font=font_sub)
draw.text((panel_x + 35, 135), "SISTEMA BASCULANTE", fill='#ffffff', font=font_title)
draw.text((panel_x + 35, 180), "Motor Basculante com Fuso e Trilho Lateral", fill='#b9b6ad', font=font_sub)

draw.line([(panel_x + 35, 218), (W - 95, 218)], fill='#2c2c2c', width=1)

items = [
    ("Motor Basculante de Alta Potência", "Instalação lateral com fuso de elevação em alumínio."),
    ("Acionamento Rápido & Desaceleração", "Abertura e fechamento com paradas suaves antiesmagamento."),
    ("Trava Eletromagnética & Nobreak", "Segurança reforçada mesmo durante interrupções de energia."),
    ("Controle via Celular & Placa Inversora", "Tecnologia de ponta e facilidade no dia a dia.")
]

y_pos = 245
for title, desc in items:
    # Red bullet point
    draw.ellipse([panel_x + 35, y_pos + 5, panel_x + 45, y_pos + 15], fill='#e6111f')
    draw.text((panel_x + 55, y_pos), title, fill='#ffffff', font=font_bold)
    draw.text((panel_x + 55, y_pos + 26), desc, fill='#b9b6ad', font=font_body)
    y_pos += 85

# Reticle badge at bottom
draw.rectangle([panel_x + 35, H - 120, W - 95, H - 85], outline='#e6111f', fill='#1a0a0c', width=1)
draw.text((panel_x + 55, H - 110), "ELETROZONE · AUTOMAÇÃO E MANUTENÇÃO", fill='#e6111f', font=font_bold)

# Save images
out_jpg = r'c:\Users\willian\Desktop\backup\cod\Site_eletrozone\site_eletro\assets\portoes_basculantes.jpg'
out_png = r'c:\Users\willian\Desktop\backup\cod\Site_eletrozone\site_eletro\assets\portoes_basculantes.png'

img.save(out_jpg, quality=95)
img.save(out_png)

print("Saved successfully to:", out_jpg)
