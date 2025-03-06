# 都道府県ごとの合格者数と人口を入力
prefecture_data = {
    "東京都": {"population": 14180000, "passers": 5704},
    "宮城県": {"population": 2266000, "passers": 311},
    "大阪府": {"population": 2754000, "passers": 1499},
    "愛知県": {"population": 7461111, "passers": 1250},
    "広島県": {"population": 2768000, "passers": 316},
    "福岡県": {"population": 5117000, "passers": 640},

}

# 10万人あたりの合格者数を計算
result = {}
for pref, data in prefecture_data.items():
    result[pref] = (data["passers"] / data["population"]) * 100000

# 降順にソート
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# 結果を表示
print("都道府県別 10万人あたりの合格者数:")
for pref, rate in sorted_result:
    print(f"{pref}: {rate:.2f} 人")
