from functions.get_files_info import get_files_info

print(f"Resuslts for current directory:")
print(get_files_info("calculator", "."))

print(f"Resuslts for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))

print(f"Resuslts for '/bin' directory:")
print(get_files_info("calculator", "/bin"))

print(f"Resuslts for '../' directory:")
print(get_files_info("calculator", "../"))