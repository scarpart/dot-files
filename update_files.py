import os

dot_paths = {
    "lvim": "~/.config/lvim/config.lua",
    "i3": "~/.config/i3/config",
    "picom": "~/.config/picom/picom.conf"
}

def update_files():
    status = "successful"
    for dir, path in dot_paths.items():
        try:
            print(f"Copying {path}...")
            
            if dir not in os.listdir():
                os.system(f"mkdir {dir}")
            os.system(f"cp -r {path} ~/github/dot-files/{dir}/")
        
        except FileNotFoundError:
            print("File not found, make sure the paths in the script are correct, \
                    you might have changed something.")
            status = "unsuccessful"
            break
    print("Script ended. Status:", status)

update_files()
