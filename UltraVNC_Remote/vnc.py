import subprocess
import os
import tkinter as tk
from tkinter import simpledialog

def conectar_vnc():
    # Configurações (ajuste conforme necessário)
    VNC_PATH = r"C:\Program Files\uvnc bvba\UltraVNC\vncviewer.exe"  # Caminho do UltraVNC
    SENHA = "password"  # Substitua pela senha real
    
    # Cria a janela para pedir o IP/Hostname
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    
    # Mostra diálogo para inserir IP/Hostname
    server_address = simpledialog.askstring("Conexão VNC", "Digite o IP ou Hostname do servidor VNC:")
    
    if server_address:  # Se o usuário digitou algo
        try:
            # Monta o comando para conectar
            comando = [
                VNC_PATH,
                "-connect", server_address,
                "-password", SENHA,
                "-autoscaling",
                #"-dsmplugin", "SecureVNCPlugin64.dsm"
            ]
            
            # Executa o UltraVNC
            subprocess.Popen(comando)
            print(f"Conectando ao servidor VNC: {server_address}")
            
        except Exception as e:
            print(f"Erro ao conectar: {e}")
    else:
        print("Nenhum endereço foi informado.")

if __name__ == "__main__":
    conectar_vnc()
