import socket
import tkinter as tk

def main():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "IP não encontrado"

    msg = f"Hostname: {hostname}\nIP: {ip_address}"

    root = tk.Tk()
    root.title("Suporte Remoto")
    root.geometry("385x130")  # Tamanho maior para acomodar o botão

    # Impede redimensionamento
    root.resizable(False, False)
    # Remove botões de minimizar e maximizar (Windows)
    root.attributes('-toolwindow', True)

    label = tk.Label(root, text=msg, font=("Arial", 18))
    label.pack(expand=True, fill="both", padx=20, pady=(0, 10))  # pady alterado para (0, 10) para subir mais

    root.mainloop()

if __name__ == "__main__":
    main()
