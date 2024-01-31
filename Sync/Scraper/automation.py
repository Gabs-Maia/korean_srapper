from selenium import webdriver
from selenium.webdriver.edge.options import Options
import os

url = ''

def web_instance(url):
    
    binary_pathDriver = "C:\Users\gabri\OneDrive\Área de Trabalho\Tor Browser\Browser\firefox"

    geckodriver = 'Sync\geckodriver-v0.34.0-win-aarch64'

    os.open(binary_pathDriver)
    op = Options()
    op.headless = True

    driver_capabilities = webdriver.DesiredCapabilities.FIREFOX
    driver_capabilities['proxy'] = {
        "proxyType": "MANUAL",
        'socksProxy' : '127.0.0.1:9150',
        "socksVersion" : 5
    }

    driver = webdriver.Firefox(capabilities=driver_capabilities,
                               options=op,
                               exe_path=geckodriver)
    return driver


if __name__ == '__main__':

  os.system("""osascript -e 'tell app "Tor Browser" to open'""")

  try:
    driver = web_instance()
    driver.get(url)

    

  except Exception as e:
    print(f"An error occurred: {e}")
  finally:
    driver.close()
    subprocess.call(['osascript', '-e', 'tell application "Tor Browser" to quit'])








