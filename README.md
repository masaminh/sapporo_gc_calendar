# sapporo_gc_calendar

札幌市家庭ごみ収集日カレンダーを iCalendar 形式にする。

# Dependency

- Python 3.8.2
- pandas 1.0.3
- icalendar 4.0.5
- python-dateutil 2.8.1

# Setup

- pipenv install

# Usage

1. [札幌市家庭ごみ収集日カレンダー](https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar)にて「札幌市家庭ごみ収集日カレンダー」の CSV ファイルをダウンロードする
1. [家庭ごみ収集日カレンダー](http://www.city.sapporo.jp/seiso/kaisyu/index.html)にて ical 化の対象となる地域名を調べる
1. pipenv run python sapporo_gc_calendar.py -a 地域名 CSV ファイル

# License

- MIT ライセンス

# Authors

- [masaminh](https://github.com/masaminh/)

# References

- [札幌市家庭ごみ収集日カレンダー](https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar)
