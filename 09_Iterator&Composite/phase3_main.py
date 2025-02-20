import phase3_waitress as waitress
import phase3_menu as menu

pancakeHouseMenu = menu.PancakeHouseMenu()
dinerMenu = menu.DinerMenu()
cafeMenu = menu.CafeMenu()

waitress = waitress.Waitress(pancakeHouseMenu, dinerMenu, cafeMenu)
waitress.printMenu()