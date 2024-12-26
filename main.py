from tabulate import tabulate
from data import products, transaction_items, transactions  # Mengimpor data dari data.py

def show_header():
    print("\n" + "="*50)
    print(" " * 10 + "\033[95mMK_CELL\033[0m")
    print(" " * 8 + "Menjual Voucher Internet All Operator")
    print("="*50 + "\n")

def show_menu():
    menu = [
        ["1", "Tambah Data Produk"],
        ["2", "Hapus Data Produk"],
        ["3", "Ubah Harga Produk"],
        ["4", "Cek Stok Produk"],
        ["5", "Laporan Penjualan"],
        ["6", "Buat Transaksi Pembelian"],
        ["7", "Lihat Semua Produk"],
        ["8", "Keluar"]
    ]
    print(tabulate(menu, headers=["Pilihan", "Menu"], tablefmt="fancy_grid"))

def view_all_products():
    # Menampilkan semua produk
    print(tabulate(products, headers=["ID", "Nama Produk", "Harga", "Stok"], tablefmt="fancy_grid"))

def sales_report():
    # Menampilkan laporan penjualan
    report = []
    for transaction in transactions:
        for item in transaction_items:
            if item[0] == transaction[0]:  # Cocokkan berdasarkan ID transaksi
                report.append([transaction[0], products[item[1] - 1][1], item[2], item[3], item[4]])

    if report:
        print(tabulate(report, headers=["ID Transaksi", "Nama Produk", "Jumlah", "Harga Satuan", "Subtotal"], tablefmt="fancy_grid"))
    else:
        print("\033[93mBelum ada penjualan!\033[0m")

def main():
    show_header()

    while True:
        show_menu()
        choice = input("Pilih menu: ")

        if choice == "1":
            # Fungsi untuk menambah produk (Anda bisa menambahkan logika untuk menambah produk di sini)
            pass
        elif choice == "2":
            # Fungsi untuk menghapus produk (Anda bisa menambahkan logika untuk menghapus produk di sini)
            pass
        elif choice == "3":
            # Fungsi untuk mengubah harga produk (Anda bisa menambahkan logika untuk mengubah harga di sini)
            pass
        elif choice == "4":
            # Fungsi untuk cek stok produk (Anda bisa menambahkan logika untuk cek stok di sini)
            pass
        elif choice == "5":
            sales_report()
        elif choice == "6":
            # Fungsi untuk buat transaksi (Anda bisa menambahkan logika untuk membuat transaksi di sini)
            pass
        elif choice == "7":
            view_all_products()
        elif choice == "8":
            print("\033[92mTerima kasih!\033[0m")
            break
        else:
            print("\033[91mPilihan tidak valid!\033[0m")

if __name__ == "__main__":
    main()
