from graphviz import Digraph

def create_mindmap():
    dot = Digraph(format='png', encoding='utf-8')
    dot.attr(dpi='300')
    dot.attr('node', fontname='Meiryo UI')
    dot.attr('edge', fontname='Meiryo UI')
    
    # ルートノード
    dot.node('基本情報技術者試験', shape='box', style='filled', fillcolor='lightblue')
    
    # 大分類
    categories = {
        'テクノロジ系（基礎理論）': ['数学', '情報理論'],
        'テクノロジ系（コンピュータシステム）': ['ハードウェア', 'ソフトウェア'],
        'テクノロジ系（技術要素・開発技術）': ['開発技術', 'セキュリティ', 'データベース', 'ネットワーク', 'その他'],
        'マネジメント系': ['プロジェクトマネジメント', 'サービスマネジメント'],
        'ストラテジ系': ['システム監査', 'システム戦略', '経営戦略', 'ビジネスインダストリ', '企業と法務'],
        '科目B': ['プログラムの処理の基本要素', 'データ構造及びアルゴリズム', 'プログラミングの諸分野への適用', '情報セキュリティの確保']
    }
    
    # 大分類の追加
    for category, subcategories in categories.items():
        dot.node(category, shape='ellipse', style='filled', fillcolor='lightgray')
        dot.edge('基本情報技術者試験', category)
        
        # 中分類の追加
        for subcategory in subcategories:
            dot.node(subcategory, shape='ellipse', style='filled', fillcolor='white')
            dot.edge(category, subcategory)
    
    return dot

# マインドマップ作成
mindmap = create_mindmap()
mindmap.render('fe_exam_mindmap', view=True)
