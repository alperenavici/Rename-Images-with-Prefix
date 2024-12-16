import os

def rename_images(folder_path, prefix=""):
    
    for filename in os.listdir(folder_path):
        
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{name}{ext}"
            
            
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_name}")

# Kullanım
folder_path = folder_path = 'Saat\\images\\wainer2' #folder path vermeniz lazım değiştirmek istediğiniz klasörün
prefix = "wainer2_" #on ad olarak eklemek istiyorsanız

rename_images(folder_path, prefix)
