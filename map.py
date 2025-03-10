import graphviz

# Graphviz オブジェクト作成
dot = graphviz.Digraph(format='png', comment="知育サイト マインドマップ")

# フォント設定 (Windows 用)
dot.attr('node', fontname='Meiryo UI')
dot.attr('edge', fontname='Meiryo UI')

# メインノード
dot.node("知育サイト", shape="box", style="filled", fillcolor="lightblue")

# 年齢別と教科別のカテゴリ
dot.node("年齢別", shape="ellipse", style="filled", fillcolor="lightgray")
dot.node("教科別", shape="ellipse", style="filled", fillcolor="lightgray")

dot.edge("知育サイト", "年齢別")
dot.edge("知育サイト", "教科別")

# 年齢別カテゴリ
ages = {
    "3歳": ["ひらがな", "数字"],
    "4歳": ["ひらがな", "カタカナ", "数字"],
    "5歳": ["ひらがな", "カタカナ", "簡単な計算"],
    "小学生": ["国語", "算数", "理科", "社会"]
}
for age, subjects in ages.items():
    dot.node(age, shape="ellipse", style="filled", fillcolor="lightyellow")
    dot.edge("年齢別", age)
    for subject in subjects:
        dot.node(subject, shape="rect", style="filled", fillcolor="white")
        dot.edge(age, subject)

# 教科別カテゴリ
subjects = {
    "国語": ["ひらがな", "カタカナ", "漢字"],
    "算数": ["数の概念", "計算", "図形"],
    "理科": ["自然", "実験"],
    "社会": ["地理", "歴史"]
}
for subject, topics in subjects.items():
    dot.node(subject, shape="ellipse", style="filled", fillcolor="lightgreen")
    dot.edge("教科別", subject)
    for topic in topics:
        dot.node(topic, shape="rect", style="filled", fillcolor="white")
        dot.edge(subject, topic)

# 画像として出力
dot.render("知育サイト_マインドマップ", view=True)
