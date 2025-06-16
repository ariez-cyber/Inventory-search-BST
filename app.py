from flask import Flask, render_template, request
import pandas as pd
from struktur_tree import ItemNode, insert, inorder_traversal, search_by_name

app = Flask(__name__)

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

@app.route('/')
def index():
    data_barang = inorder_traversal(root)
    return render_template('index.html', barang=data_barang)

@app.route('/cari', methods=['POST'])
def cari():
    nama = request.form['nama']
    hasil = search_by_name(root, nama)
    data_barang = inorder_traversal(root)
    return render_template('index.html', barang=data_barang, hasil=hasil, nama_dicari=nama)

if __name__ == '__main__':
    app.run(debug=True)
