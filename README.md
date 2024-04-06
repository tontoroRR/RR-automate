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
* [ ] デッキの画像をキャプチャしてそこから画像取得する。（スレッドにすると早くなるかも）
* [x] ユニットの順序をうまいことする
  1. [ ] 画像の場所(どこかにとっておく) 
  1. [x] レアリティ、タイプ（Damage -> Debuff -> Support -> Special)
    * Dryad, KSはKSが先に来てほしいかDryadが先になってしまう

## DONE

* [x] トロフィー上位ではちょっとづつスクロールがずれていくので70位以降はぎりぎりのところをクリックしている
  * [x] まだちょっとずれるのでずれない調整値を探す 
* [x] デッキの画像取得の範囲を狭める
* [x] Rhandumリーグの集計
