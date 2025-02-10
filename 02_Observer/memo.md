# Observerパターン
# Observerパターンとは
- オブジェクトで何か発生したときに、オブジェクトにそれを知らせるパターン。

# 要件
- WeatherDataクラスには「気温取得getTemperature()」「湿度取得getHumidity()」「気圧取得getPresure()」「何か発生したら起動measurementChanged()」の関数がある。
- measurementChanged()内に処理を実装する。
  -- 気温、湿度、気圧の最新情報を取得。
  -- 基本、湿度、気圧の情報を元に、「気象状況」「気象統計データ」「予想」を表示する。
  --- 気象状況の表示: currentConditionDispplay.update(temp,humidity,pressure)
  --- 気象統計データの表示: statisticDisplay.update(temp, humidity, pressure)
  --- 予想の表示: forecastDisplay.update(temp, humidity, pressure)
  -- 将来発生するかもしれない、別の表示ニーズに対し、measurementChanged()の中身を変えずに対応できる方法を考える。


