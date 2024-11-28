import csv
from pathlib import Path
import shutil
from banco import conectar_banco

def exportar_para_csv(caminho_csv):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    with open(caminho_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Título', 'Autor', 'Ano de Publicação', 'Preço'])
        writer.writerows(livros)

    print(f"Dados exportados para {caminho_csv}")
    conn.close()

def importar_de_csv(caminho_csv):
    conn = conectar_banco()
    cursor = conn.cursor()

    with open(caminho_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Pula o cabeçalho
        for row in reader:
            cursor.execute('''
                INSERT INTO livros (id, titulo, autor, ano_publicacao, preco)
                VALUES (?, ?, ?, ?, ?)
            ''', (None, row[1], row[2], int(row[3]), float(row[4])))

    conn.commit()
    conn.close()
    print(f"Dados importados do arquivo {caminho_csv}")

def fazer_backup():
    conn = conectar_banco()
    cursor = conn.cursor()

    # Realiza backup do banco de dados
    backup_path = Path('backups') / f"backup_livraria_{Path().resolve().name}.db"
    shutil.copy('data/livraria.db', backup_path)
    print(f"Backup criado em {backup_path}")

    conn.close()

def limpar_backups_antigos():
    backups_dir = Path('backups')
    backups = sorted(backups_dir.glob('*.db'), key=lambda p: p.stat().st_mtime)

    # Mantém apenas os 5 últimos backups
    for backup in backups[:-5]:
        backup.unlink()
        print(f"Backup {backup} excluído.")
