class ItemNode:
    def __init__(self, kode, nama, kategori, stok, harga):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.stok = stok
        self.harga = harga
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.kode} | {self.nama} | {self.kategori} | Stok: {self.stok} | Harga: {self.harga}"

def insert(root, node):
    if not root:
        return node
    if node.nama.lower() < root.nama.lower():
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root

def inorder_traversal(root):
    if root:
        return inorder_traversal(root.left) + [root] + inorder_traversal(root.right)
    return []

def search_by_name(root, nama):
    if not root:
        return None
    if nama.lower() == root.nama.lower():
        return root
    elif nama.lower() < root.nama.lower():
        return search_by_name(root.left, nama)
    else:
        return search_by_name(root.right, nama)

class ItemNode:
    def __init__(self, kode, nama, kategori, stok, harga):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.stok = stok
        self.harga = harga
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.kode} | {self.nama} | {self.kategori} | Stok: {self.stok} | Harga: {self.harga}"


def insert(root, node):
    if not root:
        return node
    if node.nama.lower() < root.nama.lower():
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root


def inorder_traversal(root):
    if root:
        return inorder_traversal(root.left) + [root] + inorder_traversal(root.right)
    return []


def search_by_name(root, nama):
    if not root:
        return None
    if nama.lower() == root.nama.lower():
        return root
    elif nama.lower() < root.nama.lower():
        return search_by_name(root.left, nama)
    else:
        return search_by_name(root.right, nama)


# =========================
# Fungsi Visualisasi Pohon dengan Garis
# =========================
def display_tree_with_lines(node, prefix="", is_left=True):
    if node is not None:
        print(prefix + ("├── " if is_left else "└── ") + f"{node.nama}")

        if node.left or node.right:
            if node.left:
                display_tree_with_lines(node.left, prefix + ("│   " if is_left else "    "), True)
            else:
                print(prefix + ("│   " if is_left else "    ") + "├── None")

            if node.right:
                display_tree_with_lines(node.right, prefix + ("│   " if is_left else "    "), False)
            else:
                print(prefix + ("│   " if is_left else "    ") + "└── None")


# =========================
# Contoh Penggunaan
# =========================
if __name__ == "__main__":
    # Buat tree dan tambahkan data
    root = None
    root = insert(root, ItemNode(1001, "Sabun Mandi", "Kebutuhan Pribadi", 56, 39.456))
    root = insert(root, ItemNode(1002, "Shampoo",	"Kebutuhan Pribadi",53,	4.888 ))
    root = insert(root, ItemNode(1003, "Sikat Gigi",	"Kebutuhan Pribadi",	34	,40.042 ))
    root = insert(root, ItemNode(1004, "Pasta Gigi",	"Kebutuhan Pribadi"	,35	, 45.770 ))
    root = insert(root, ItemNode(1006, "Mi Instan Goreng",	"Makanan"	,91	, 32.423 ))
    root = insert(root, ItemNode(1007, "Mi Instan Kuah",	"Makanan"	,69	,12.539 ))
    root = insert(root, ItemNode(1008,	"Susu UHT",	"Minuman"	,65	,14.521 ))
    root = insert(root, ItemNode(1009,	"Air Mineral 600ml",	"Minuman"	,75	, 32.276)) 
    root = insert(root, ItemNode(1010,	"Air Mineral 1.5L",	"Minuman"	,35	, 16.079 ))
    root = insert(root, ItemNode(1011,	"Roti Tawar",	"Makanan"	,50	, 20.422))
    root = insert(root, ItemNode(1012,	"Cokelat Batang",	"Makanan",	96,	 27.169)) 
    root = insert(root, ItemNode(1013,	"Permen Mint",	"Makanan"	,35 ,18.067 ))
    root = insert(root, ItemNode(1014,	"Teh Botol",	"Minuman"	,51,	 49.806)) 
    root = insert(root, ItemNode(1015,	"Kopi Instan",	"Minuman" ,21	 ,44.922))
    root = insert(root, ItemNode(1016,	"Deterjen Bubuk", 	"Kebutuhan Rumah"	,15	 ,28.975 ))
    root = insert(root, ItemNode(1017,	"Pembersih Lantai", 	"Kebutuhan Rumah"	,60,14.255))
    root = insert(root, ItemNode(1018,	"Pel" ,	"Kebutuhan Rumah",	91	, 7.823 ))
    root = insert(root, ItemNode(1019,	"Sapu" ,	"Kebutuhan Rumah"	,80	 ,12.593)) 
    root = insert(root, ItemNode(1020,	"Ember" ,	"Kebutuhan Rumah",	13,	 44.414 ))
    root = insert(root, ItemNode(1021,	"Minyak Goreng 1L", 	"Makanan"	,29	 ,25.750)) 
    root = insert(root, ItemNode(1022,	"Gula Pasir",	"Makanan",	44,	 39.170 ))
    root = insert(root, ItemNode(1023,	"Garam Dapur","Makanan"	,43	 ,17.763 ))
    root = insert(root, ItemNode(1024,	"Kecap Manis","Makanan"	,46, 4.303 ))
    root = insert(root, ItemNode(1025,	"Saus Sambal" ,	"Makanan"	,58	 ,47.301))
    root = insert(root, ItemNode(1026,	"Telur Ayam (1kg)","Makanan"	,11	, 39.370)) 
    root = insert(root, ItemNode(1027,	"Beras 5kg" ,	"Makanan"	,27	 ,36.414))
    root = insert(root, ItemNode(1028,	"Snack Kentang", 	"Makanan"	,20	, 16.685 ))
    root = insert(root, ItemNode(1029,	"Tisu Gulung" ,	"Kebutuhan Rumah"	,71	, 22.550))
    root = insert(root, ItemNode(1030,	"Sabun Cuci Piring"," Kebutuhan Rumah",	11	, 40.016)) 

    # Cetak pohon
    print("Struktur Pohon Binary Search Tree:")
    display_tree_with_lines(root)

    # Cetak traversal inorder
    print("\n\nData Barang (Inorder Traversal):")
    for node in inorder_traversal(root):
        print(node)




