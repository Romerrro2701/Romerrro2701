from selenium import webdriver ## импорт селениума
from webdriver_manager.chrome import ChromeDriverManager ## импорт хромдрайвера
from selenium.webdriver.chrome.service import Service ## 

service = Service(executable_path=ChromeDriverManager().install()) ## установка хромдрайвера
driver = webdriver.Chrome(service=service) ## запуск хромдрайвера
