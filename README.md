# sapporo_gc_calendar

札幌市家庭ごみ収集日カレンダーをiCalendar形式にする。

# Dependency

* Python 3.7.3
* pandas 0.24.2
* icalendar 4.0.3

# Setup

* pipenv install

# Usage

1. [札幌市家庭ごみ収集日カレンダー](https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar)にて「札幌市家庭ごみ収集日カレンダー」のCSVファイルをダウンロードする
1. [家庭ごみ収集日カレンダー](http://www.city.sapporo.jp/seiso/kaisyu/index.html)にてical化の対象となる地域名を調べる
1. pipenv run python sapporo_gc_calendar.py -a 地域名 CSVファイル

# License

* MITライセンス

# Authors

* [masaminh](https://github.com/masaminh/)

# References

* [札幌市家庭ごみ収集日カレンダー](https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar)
