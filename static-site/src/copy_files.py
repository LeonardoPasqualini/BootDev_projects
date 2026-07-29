import os
import shutil

def move_static_to_public():
    static_path = "static/"
    public_path = "public/"
    
    if not os.path.exists(static_path):
        raise FileNotFoundError("Static directory not found")
    
    if os.path.exists(public_path):
        print("Removing public directory...")
        shutil.rmtree(public_path)
    
    print("Creating empty public directory...")
    os.mkdir(public_path)
    
    print("Coping files from static to public...")
    move_files(static_path, public_path)
    print("Done.")
    
def move_files(src_path: str, dst_path: str):
    if os.path.isfile(src_path):
        print(f'Copying "{src_path}" to "{dst_path}"...')
        dir_path = "/".join(dst_path.split("/")[:-1])
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        shutil.copy(src_path, dir_path)
        return
    
    path_list = os.listdir(src_path)
    for path in path_list:
        from_path = os.path.join(src_path, path)
        to_path = os.path.join(dst_path, path)
        move_files(from_path, to_path)