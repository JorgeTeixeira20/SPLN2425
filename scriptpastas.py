import os

def criar_pastas():
    for i in range(1, 9):
        pasta_tpx = f"TP{i}"
        os.makedirs(pasta_tpx, exist_ok=True)
        
        readme_path = os.path.join(pasta_tpx, "README.md")
        with open(readme_path, "w") as f:
            f.write(f"# TPC {i}\n")
    
    print("Pastas criadas com sucesso!")

if __name__ == "__main__":
    criar_pastas()

