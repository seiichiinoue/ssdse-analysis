# ssdse-analysis

Atsuya Kobayashi 2018-10-31

---

## Description  

*SSDSE* : [教育用標準データセット](https://www.nstac.go.jp/SSDSE/)（Standardized Statistical Data Set for Education）

> e-Statに収録されている「都道府県・市区町村のすがた（社会・人口統計体系）」の市区町村データから約100項目余を抜き出し、縦に市区町村、横にデータ項目が並ぶ表形式のデータに整備したものです

- ([データ説明](https://www.nstac.go.jp/SSDSE/SSDSE2018_kaisetsu.pdf))
- ([Data (.csv)](https://www.nstac.go.jp/SSDSE/SSDSE.csv))


*[e-Stat](https://www.e-stat.go.jp/)* : 政府のオープンデータセット。必要に応じて都道府県別・市町村別などのデータセットを探そう。


### How

ノートブック`.ipynb`を追加する形で分析を進める。ノートブック冒頭で`setup.py`を実行してくだせえ。

```
import setup

ssdse = setup.ssdse()
```

`setup`により，以下のライブラリ・変数がつかるようになる。

- numpy/scipy/matplotlib/
- `ssdse.ssdse`: `pandas.DataFrame`
- `ssdse.per_capita`: `pandas.DataFrame`

### Aim

データ分析の練習とビジコン(？)への準備。

### Plans

何かしらのデータ分析を`.ipynb`上で行う予定。

- データ成形・マンジング(必要？) 
- 可視化 `matplolib.pyplot`
- 分布の確認、正規性の検定等 `scipy`
- 因子分析 `mca` `sklearn.decomposition.FactorAnalysis`
- 多変量解析・多重回帰モデル選択・正則化GLM・変数選択 `sklearn`
- その他

## Requirements

- numpy
- pandas
- scipy
- matplotlib
  - pyplot
  - IPA fonts
- scikit-learn
