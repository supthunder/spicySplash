from selenium import webdriver
import concurrent.futures

def multi_splash(item, DRIVERS, etc):
	link = "http://www.adidas.com/us/apps/yeezy5av"
	link = "https://www.google.com"
	driver = webdriver.Chrome(executable_path="drivers/chromedriver") #.exe if windows
	driver.set_window_size(500,250)
	driver.get(link)
	DRIVERS.append(driver)

def main():
	DRIVERS = []
	accounts = int(input("how many? "))
	items = [0]*accounts
	position = [0,0]
	count = 0
	with concurrent.futures.ThreadPoolExecutor(max_workers=accounts) as executor:
		for item in items:
			executor.submit(multi_splash, item, DRIVERS,60)

	for driver in DRIVERS:
		if count == 1000:
			count = 0
			position[0] += 500
		driver.set_window_position(position[0], position[1]+count)
		count += 250

	exit = input("exit? ")
	for eachWindow in DRIVERS:
		eachWindow.quit()

if __name__ == '__main__':
	main()
