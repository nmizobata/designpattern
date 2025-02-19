import phase2_waitress as waitress
import phase2_menu as menu

pancakeHouseMenu = menu.PancakeHouseMenu()
dinerMenu = menu.DinerMenu()

waitress = waitress.Waitress(pancakeHouseMenu, dinerMenu)
waitress.printMenu()