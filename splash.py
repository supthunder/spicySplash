from selenium import webdriver


def main():
	accounts = int(input("how many? "))
	link = "http://www.adidas.com/us/apps/yeezy5av"
	DRIVERS = []
	position = [0,0]
	count = 0
	for i in range(0,accounts):
		if count == 1000:
			count = 0
			position[0] += 500

		driver = webdriver.Chrome(executable_path="drivers/chromedriver")

		driver.set_window_size(500,250)
		driver.get(link)
		DRIVERS.append(driver)
		driver.set_window_position(position[0], position[1]+count)
		count += 250

	exit = input("exit? ")
	for eachWindow in DRIVERS:
		eachWindow.quit()




if __name__ == '__main__':
	main()
