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

* [x] トロフィー上位ではちょっとづつスクロールがずれていくので70位以降はぎりぎりのところをクリックしている
  * [ ] まだちょっとずれるのでずれない調整値を探す
* [ ] ヒーローとアタッカーの組み合わせ、アタッカーだけでどれほど使われているのかを集計
* [x] 蘭だーむリーグの集計
* [ ] デッキの画像をキャプチャしてそこから画像取得する。（スレッドにすると早くなるかも）
* [ ] ユニットの順序をうまいことする
  1. 画像の場所
  1. レアリティ、タイプ（Damage -> Debuff -> Support -> Special)
