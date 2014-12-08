from selenium import webdriver
capabilities = {
  'chromeOptions': {
    'androidPackage': 'com.android.chrome',
  }
}
driver = webdriver.Remote('http://localhost:9515', capabilities)
driver.get('http://appium.io')
driver.execute_script("window.scrollBy(0,200)")
driver.quit()
