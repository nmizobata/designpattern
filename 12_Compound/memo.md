# Compound
## 各phaseのコード
- phase1:  ガチョウをカモに偽装(アダプタパターン)
- phase2:  デコレータ(鳴き声数のカウント付)で鳴き声数をカウント
- phase3:  デコレータ(鳴き声数のカウント付)の抜けをなくすため、Abstract Factoryで再実装
- phase4:  カモの群れをシミュレート(コンポジットパターン)
- phase5:  カモを1羽づつ監視(オブザーバーパターン)
## 概要
- 2つ以上のデザインパターンを組み合わせ、繰り返し発生する問題や一般的な問題を解決する解決策となる。
- 
## Observeパターンの実装
- サブジェクトは、register()とnotifyObservers()を実装しなければならない。(observerパターン参照)
- クラスにハードコーディングする事も可だが、phase5の事例のようにサブジェクトが多数にわたる場合は、サブジェクトインターフェースにメソッドを実装して、それを子クラスが受ける、としたほうが、管理が楽になる。

## 群を扱う時の注意
- ObserverパターンやCompositeパターンでオブジェクトを群として管理して扱う時、その群の要素がしっかりと「別のオブジェクトインスタンスを登録しているか」に注意が必要。
- 群管理用のリスト変数に登録したとき、違うものとして登録しているつもりが、実は同じインスタンスを何度も登録していることがある。例えば、以下の場合、flockというCompositeにmallardduckを2匹登録するつもりで実装したが、実は一つのmallardduckを2回登録しているだけである。
  ```
  mallardduck = Mallardduck()
  flock.add(mallardduck)
  flock.add(mallardduck)
  ```
- 違うmallardduckを2匹登録したい場合は、以下のようにしなければならない。
  ```
  mallardduck1 = Mallardduck()
  mallardduck2 = Mallardduck()
  flock.add(mallardduck1)
  flock.add(mallardduck2)
  ```

## MVC (Model-View-Controller)
- アプリケーション設計概念の一つ。ユーザーインターフェースおよび表示を担当するView、アクション要求に対して何かを実行するModel、Viewからのアクションをモデルのアクションに変換して伝えるControllerを分離して設計することにより、疎結合を実現。これによりViewやModelが変わっても、再利用性を確保することができる。
- MVCの各部の役割を実現するために、Observer、Strategy、CompositeパターンからなるCompoundパターンである。これにより設計が明瞭で柔軟になる。
  - Modelの状況をViewに伝えて最新の状態を維持しつつも、Viewから分離された状態を保てるObserverパターン
  - ControllerはViewに対するStrategy。Viewは様々なController実装を使って様々な振る舞いを手に入れることができる。
  - ViewはConpositeパターンを使ってユーザーインターフェースを実装。通常UIはパネル、フレーム、ボタンなどのネストされたコンポーネントで構成される。
- Adapterパターンを使って、メソッドが異なる新しいモデルを既存のViewやControllerに適応させることができる。
- 多くのWeb MVCフレームワークが存在し、MVCパターンをクライアント/サーバーアプリケーション構造に適応させている。
## その他
- クラスメソッド、クラス変数
  - クラス変数とはインスタンス間で共有される変数のこと。すべてのインスタンスで同じ値が得られる。
  - クラスメソッドとはインスタンスを作らずに使えるメソッドのこと。JavaではStaticメソッドとも呼ばれる。@classmethodを付ければそのメソッドはクラスメソッドとなる。
  - クラス変数は、classの直下で使用開始し、メソッドやclass外では、class名.変数名で参照する。
  - クラスメソッドは、class名.メソッドで実行する。

- 