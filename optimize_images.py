#!/usr/bin/env python3
"""
Script pour optimiser les images WEBP et créer différentes résolutions
Utilise Pillow pour redimensionner les images
"""

import os
from PIL import Image
import sys

def optimize_webp_image(input_path, output_dir, base_name):
    """
    Crée différentes tailles d'une image WEBP pour srcset
    """
    try:
        with Image.open(input_path) as img:
            # Taille originale
            original_width, original_height = img.size
            print(f"Image originale: {original_width}x{original_height}")
            
            # Créer différentes tailles
            sizes = [
                (int(original_width * 0.25), int(original_height * 0.25), "small"),
                (int(original_width * 0.5), int(original_height * 0.5), "medium"),
                (int(original_width * 0.75), int(original_height * 0.75), "large"),
            ]
            
            for width, height, suffix in sizes:
                resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
                output_filename = f"{base_name}_{suffix}.webp"
                output_path = os.path.join(output_dir, output_filename)
                
                # Sauvegarder avec qualité élevée
                resized_img.save(output_path, 'WEBP', quality=95, method=6)
                print(f"Créé: {output_filename} ({width}x{height})")
                
    except Exception as e:
        print(f"Erreur avec {input_path}: {e}")

def main():
    webp_dir = "assets/img/WEBP"
    output_dir = "assets/img/WEBP_OPTIMIZED"
    
    # Créer le dossier de sortie
    os.makedirs(output_dir, exist_ok=True)
    
    # Traiter les images principales de produits
    main_images = [
        "Mockup_DOUBLE_Oversize_Blanc_Bleu.webp",
        "Mockup_DOUBLE_Oversize_Blanc_Or.webp",
        "Mockup_DOUBLE_Oversize_Noir_Blanc.webp",
        "Mockup_DOUBLE_Oversize_Noir_Blanc_2.webp",
        "Mockup_DOUBLE_Hoodie_Blanc_Bleu.webp",
        "Mockup_DOUBLE_Hoodie_Blanc _Or.webp",
        "Mockup_DOUBLE_Hoodie_Noir_Blanc.webp",
        "Mockup_DOUBLE_Hoodie_Noir_Blanc_2.webp"
    ]
    
    for image_name in main_images:
        input_path = os.path.join(webp_dir, image_name)
        if os.path.exists(input_path):
            base_name = os.path.splitext(image_name)[0]
            optimize_webp_image(input_path, output_dir, base_name)
        else:
            print(f"Image non trouvée: {input_path}")

if __name__ == "__main__":
    main()
