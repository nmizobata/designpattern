import phase4_menu as menu
import phase4_waitress as wress

pancakeHouseMenu= menu.Menu("パンケーキハウスメニュー", "朝食")
dinerMenu=menu.Menu("食堂メニュー","昼食")
cafeMenu = menu.Menu("カフェメニュー","夕食")
dessertMenu = menu.Menu("デザートメニュー", "もちろんデザート!")

allMenus = menu.Menu("すべてのメニュー","すべてを統合したメニュー")

allMenus.add(pancakeHouseMenu)
allMenus.add(dinerMenu)
allMenus.add(cafeMenu)
pancakeHouseMenu.add(menu.MenuItem("K&Bのパンケーキ朝食",
                                   "スクランブルエッグとトースト付きパンケーキ",
                                   True,
                                   2.99))
pancakeHouseMenu.add(menu.MenuItem("いつものパンケーキ朝食",
                                   "卵焼きとソーセージ付きパンケーキ",
                                   False,
                                   2.99))
pancakeHouseMenu.add(menu.MenuItem("ブルーベリーパンケーキ",
                                   "新鮮なブルーベリーを使ったパンケーキ",
                                   True,
                                   3.49))
pancakeHouseMenu.add(menu.MenuItem("ワッフル",
                                   "ブルーベリーかイチゴの好きな方をのせたワッフル",
                                   True,
                                   3.59))
dinerMenu.add(menu.MenuItem("ベジタリアンBLT", 
                            "レタス、トマト、フェイクベーコンを挟んだ全粒小麦パンサンドイッチ", 
                            True, 
                            2.99))
dinerMenu.add(menu.MenuItem("BLT", 
                            "レタス、トマト、ベーコンを挟んだ全粒小麦パンサンドイッチ", 
                            False, 
                            2.99))
dinerMenu.add(menu.MenuItem("本日のスープ", 
                            "ポテトサラダを添えた本日のスープ", 
                            False, 
                            3.29))
dinerMenu.add(menu.MenuItem("ホットドッグ", 
                            "ザワークラウト、レリッシュ、玉ねぎ、チーズを挟んだホットドッグ", 
                            False, 
                            3.05))
dinerMenu.add(menu.MenuItem("蒸し野菜と玄米", 
                            "玄米の上に蒸し野菜", 
                            True, 
                            3.99))
dinerMenu.add(menu.MenuItem("パスタ", 
                            "マリナラソーススパゲティとサワードウパン", 
                            True, 
                            3.89))
dinerMenu.add(dessertMenu)
dessertMenu.add(menu.MenuItem("アップルパイ",
                              "バニラアイスクリームを押せたフレーク状生地のアップルパイ",
                              True,
                              1.59))
dessertMenu.add(menu.MenuItem("チーズケーキ",
                              "チョコレートグラハム生地のクリーミーなニューヨークチーズケーキ",
                              True,
                              1.99))
dessertMenu.add(menu.MenuItem("シャーベット",
                              "ラズベリーシャーベットとライムシャーベット",
                              True,
                              1.89))
cafeMenu.add(menu.MenuItem("野菜バーガーとフライドポテト", 
                           "全粒小麦にレタスとトマトを挟んだ野菜バーガーとフライドポテト", 
                           True, 
                           3.99))
cafeMenu.add(menu.MenuItem("本日のスープ", 
                           "サラダが付いた本日のスープ", 
                           False, 
                           3.69))
cafeMenu.add(menu.MenuItem("ブリトー", 
                           "インゲン豆、サルサ、グアカモーレ入りの大きなブリトー", 
                           True, 
                           4.29))


waitress = wress.Waitress(allMenus)
waitress.printMenu()