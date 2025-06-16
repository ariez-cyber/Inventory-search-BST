import pandas as pd
from struktur_tree import ItemNode, insert, inorder_traversal, search_by_name

df = pd.read_excel('Data_Inventory_Supermarket.xlsx')

root = None
for _, row in df.iterrows():
    node = ItemNode(
        kode=row['Kode Barang'],
        nama=row['Nama Barang'],
        kategori=row['Kategori'],
        stok=row['Stok'],
        harga=row['Harga']
    )
    root = insert(root, node)

print("Data Barang (terurut berdasarkan nama):")
for item in inorder_traversal(root):
    print(item)

nama_dicari = "Indomie Goreng"
hasil = search_by_name(root, nama_dicari)
if hasil:
    print(f"\nHasil pencarian untuk '{nama_dicari}':\n{hasil}")
else:
    print(f"\nBarang '{nama_dicari}' tidak ditemukan.")
