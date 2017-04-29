from selenium import webdriver
import concurrent.futures

DRIVERS = []
def multi_splash(item, etc):
	global DRIVERS
	link = "http://www.adidas.com/us/apps/yeezy5av"
	driver = webdriver.Firefox()
	driver.set_window_size(500,250)
	driver.get(link)
	DRIVERS.append(driver)

def main():
	global DRIVERS
	accounts = int(input("how many? "))
	items = [0]*accounts
	position = [0,0]
	count = 0
	with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
		for item in items:
			executor.submit(multi_splash, item,60)

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
