# RR-automate
Count up Top100

## Prerequirement
* MyGame Launcher + Rush Royale for PC
* python3
* Google spreadsheet
* Google Cloud Account's security JSON key file
  * place it under secrets/ folder

## How to use

1. Copy .env_sample to .env. Set spreadsheet's ID and JSON file name.
1. Install python modules. ``` > pip install -r requirement ```
1. Run command. ```> python3.exe DeckStatus.py```

## TODO

* [ ] ヒーローとアタッカーの組み合わせ、アタッカーだけでどれほど使われているのかを集計
* [ ] ユニットの順序をうまいことする
    * [ ] 画像の場所(どこかにとっておく)
* [ ] デッキの画像をキャプチャしてそこから画像取得する。（スレッドにすると早くなるかも）
* [ ] Dryad, KSはKSが先に来てほしいかDryadが先になってしまう
* [ ] ユニットの位置情報を記録する
* [ ] 才能を記録する

### DONE

* [x] トロフィー上位ではちょっとづつスクロールがずれていくので70位以降はぎりぎりのところをクリックしている
    * [x] まだちょっとずれるのでずれない調整値を探す[x] デッキの画像取得の範囲を狭める
* [x] デッキの画像取得の範囲を狭める
* [x] ランダームリーグの集計
    * [x] ユニットの順序をうまいことする
    * [x] 画像の場所(どこかにとっておく)
* [x] ユニットの順序をうまいことする
    * [x] レアリティ、タイプ（Damage -> Debuff -> Support -> Special)
