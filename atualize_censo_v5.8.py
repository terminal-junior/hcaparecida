import os
import subprocess
import time
import psutil
import tempfile
import shutil
import logging
from datetime import datetime
from pywinauto import Application
from pywinauto.keyboard import send_keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service  # Adicione este import
import uuid
import sys

# === CONFIGURAÇÃO DO LOG ===
# Caminho para a pasta "Log_censo" no Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Log_Censo")

# Criar a pasta se não existir
os.makedirs(desktop_path, exist_ok=True)

# Define o nome do arquivo de log com data e hora
log_filename = f"log_atualize_censo_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
log_path = os.path.join(desktop_path, log_filename)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Início da automação Fathos + Censo")

MAX_TENTATIVAS = 5
tentativa = 0

while tentativa < MAX_TENTATIVAS:
    tentativa += 1
    logging.info(f"Iniciando tentativa {tentativa} de {MAX_TENTATIVAS}")
    erro_ocorreu = False

    try:
        # === ENCERRA FATHOS SE JÁ ESTIVER ABERTO ===
        nome_processo = "Fathos.exe"
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == nome_processo:
                logging.info(f"Fechando {nome_processo} (PID: {proc.pid})")
                proc.terminate()
                proc.wait()
                logging.info(f"{nome_processo} encerrado.")
                break
        else:
            logging.info(f"{nome_processo} não estava em execução.")

        # === ABRE O FATHOS ===
        try:
            subprocess.Popen([r"C:\\AGFA_Exe_22\\Fathos.exe", "agfaprod", "%profile%"])
            logging.info("Fathos inicializado.")
            time.sleep(5)

            send_keys("youusername{TAB}youpassword{ENTER}")
            logging.info("Login feito com sucesso!")
            time.sleep(1)
                        
            app = Application(backend="uia").connect(title_re="Fathos - SOCIEDADE BENEFICENTE SANTA TEREZINHA.*", timeout=1)
            main_window = app.window(title_re="Fathos - SOCIEDADE BENEFICENTE SANTA TEREZINHA.*")
            main_window.wait("enabled visible ready", timeout=1)

            relatorios_menu = main_window.child_window(title="Relatórios", control_type="MenuItem")
            relatorios_menu.wait("enabled visible ready", timeout=1)
            relatorios_menu.select()
            logging.info("Menu 'Relatórios' acessado.")
            logging.info("Menu 'Censo Ocupacional' acessado.")

            send_keys("c{TAB 6}{SPACE}{TAB 12}{DOWN}{ENTER 2}")
            logging.info("CheckBox 'Apenas Leitos Ocupados' marcado e item 'Leito' selecionado.")
            logging.info("Gerando relatório do Censo...")
            time.sleep(4)
            logging.info("Relatório do Censo gerado com sucesso.")
        
            janela = app.window(title_re="Fathos - SOCIEDADE BENEFICENTE SANTA TEREZINHA.*")
            botoes = janela.descendants(control_type="Button")
            botoes[0].invoke()

            checkbox = janela.child_window(control_type="CheckBox", found_index=1)
            if checkbox.exists() and checkbox.is_enabled():
                checkbox.toggle()
                logging.info("CheckBox Imprimir para Arquivo marcada.")
            else:
                logging.warning("CheckBox Imprimir para Arquivo não encontrada ou desabilitada.")

            send_keys('{TAB}{DOWN 11}{TAB}')
            logging.info("Tipo: 'XLS DATA File' selecionado")
            caminho_arquivo = r"\\srv-02\inetpub\wwwroot\mapa\censo.xls"
            send_keys(caminho_arquivo)
            send_keys('{ENTER 2}')
            logging.info(r"Censo salvo em: \\srv-02\inetpub\wwwroot\mapa\censo.xls")
            time.sleep(4)

        except Exception as e:
            logging.error(f"Erro durante a automação do Fathos + Censo: {e}")
            erro_ocorreu = True
            continue  # Vai para a próxima tentativa

        # === ENCERRA FATHOS NOVAMENTE, SE NECESSÁRIO ===
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == nome_processo:
                logging.info(f"Fechando {nome_processo} (PID: {proc.pid})")
                proc.terminate()
                proc.wait()
                logging.info(f"{nome_processo} encerrado.")
                break
        else:
            logging.info(f"{nome_processo} não estava em execução.")

        # === GARANTE QUE O EDGE NÃO ESTÁ ABERTO ===
        nome_processo2 = "msedge.exe"
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == nome_processo2:
                logging.info(f"Fechando {nome_processo2} (PID: {proc.pid}) antes de iniciar o Selenium")
                proc.terminate()
                proc.wait()
                logging.info(f"{nome_processo2} encerrado.")

        # === INICIALIZA EDGE COM PERFIL TEMPORÁRIO ===
        temp_profile = os.path.join(tempfile.gettempdir(), f"edge_profile_{uuid.uuid4().hex}")
        os.makedirs(temp_profile, exist_ok=True)
        options = Options()
        options.add_argument(f"--user-data-dir={temp_profile}")
        options.add_argument("--disable-features=EdgeIdentitySignin")
        options.add_argument("--disable-features=msEdgeAccountIntegration")
        logging.info(f"Perfil temporário criado: {temp_profile}")

        # Caminho do driver Edge
        if getattr(sys, 'frozen', False):
            # Executável compilado: driver está em sys._MEIPASS
            driver_path = os.path.join(sys._MEIPASS, "msedgedriver.exe")
        else:
            # Execução normal: driver está ao lado do script
            driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "msedgedriver.exe")

        if not os.path.exists(driver_path):
            logging.error(f"msedgedriver.exe não encontrado em: {driver_path}")
            raise FileNotFoundError(f"msedgedriver.exe não encontrado em: {driver_path}")

        try:
            service = Service(driver_path)
            driver = webdriver.Edge(service=service, options=options)
            logging.info("Edge inicializado!")
        except Exception as e:
            logging.error(f"Falha ao iniciar o Edge: {e}")
            raise

        try:
            driver.get("http://yousite.com")
            logging.info("Sistema 'MAPA - Sistema de Controle de Mapa Cirúrgico' aberto.")

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
            driver.find_element(By.NAME, "username").send_keys("youusername")
            senha = driver.find_element(By.NAME, "password")
            senha.send_keys("youpassword")
            senha.send_keys(Keys.RETURN)
            logging.info("Login feito com sucesso!")

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu_17"]/li[2]/a')))
            driver.find_element(By.XPATH, '//*[@id="menu_17"]/li[2]/a').click()
            logging.info("Menu 'Censo' acessado.")

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fConsCensolistsrch"]/table/tbody/tr[2]/td/span/label[3]/a')))
            driver.find_element(By.XPATH, '//*[@id="fConsCensolistsrch"]/table/tbody/tr[2]/td/span/label[3]/a').click()
            logging.info("Importar Censo do Sistema RECEP")

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnAction")))
            driver.find_element(By.ID, "btnAction").click()
            logging.info("Atualização do Censo concluída.")
            time.sleep(1)

        except Exception as e:
            logging.error(f"Erro no navegador: {e}")
            erro_ocorreu = True
        finally:
            try:
                if 'driver' in locals() and driver:
                    driver.quit()
                    logging.info("Navegador encerrado.")
            except Exception as e:
                logging.warning(f"Erro ao encerrar navegador: {e}")
            try:
                shutil.rmtree(temp_profile)
                logging.info(f"Perfil temporário apagado: {temp_profile}")
            except Exception as e:
                logging.warning(f"Erro ao apagar perfil temporário: {e}")

        # === ENCERRA EDGE SE AINDA ESTIVER ABERTO ===
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == nome_processo2:
                logging.info(f"Fechando {nome_processo2} (PID: {proc.pid})")
                proc.terminate()
                proc.wait()
                logging.info(f"{nome_processo2} encerrado.")
                break
        else:
            logging.info(f"{nome_processo2} não estava em execução.")

        if not erro_ocorreu:
            break  # Sai do loop se tudo ocorreu bem

    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        erro_ocorreu = True

if erro_ocorreu:
    logging.error("Automatização do Censo falhou após várias tentativas.")
    print("❌ Erro ao executar a automação. Verifique o log para detalhes.")
else:
    logging.info("Automatização do Censo finalizada com sucesso. Log salvo em: %s", log_path)
    print(f"✅ Log salvo no Desktop: {log_path}")
# Fim do Código
