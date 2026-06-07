#!/usr/bin/env python3
"""
将文章页面的硬编码西班牙语/葡萄牙语内容翻译为中文
"""
from pathlib import Path

WORKSPACE = Path("D:/workspace")

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def translate_mexico_customs(content):
    """翻译墨西哥海关文章"""
    changes = []
    
    # 语言标签
    if 'ESPAÑOL' in content:
        content = content.replace('<span class="badge badge-es">ESPAÑOL</span>', '<span class="badge badge-zh">中文</span>', 1)
        changes.append("Language badge: ESPAÑOL -> 中文")
    
    # 标题
    if 'Cómo Pasar Aduana en México' in content:
        content = content.replace(
            '<h1>Cómo Pasar Aduana en México: Guía Completa de Importaciones desde China 2024</h1>',
            '<h1>墨西哥海关清关完整指南：中国进口商必读（2024）</h1>',
            1
        )
        changes.append("Title translated to Chinese")
    
    # 日期格式
    content = content.replace('<span>📅 12 de enero, 2024</span>', '<span>📅 2024年1月12日</span>', 1)
    content = content.replace('<span>🇲🇽 México</span>', '<span>🇲🇽 墨西哥</span>', 1)
    
    # 面包屑
    content = content.replace('>文章首页<', '>文章首页<', 1)
    
    return content, changes

def translate_brazil_market(content):
    """翻译巴西市场文章"""
    changes = []
    
    if 'PORTUGUÊS' in content:
        content = content.replace('<span class="badge badge-pt">PORTUGUÊS</span>', '<span class="badge badge-zh">中文</span>', 1)
        changes.append("Language badge: PORTUGUÊS -> 中文")
    
    if 'Guia de Acesso ao Mercado Brasileiro' in content:
        content = content.replace(
            '<h1>Guia de Acesso ao Mercado Brasileiro para Vendedores Chineses 2024</h1>',
            '<h1>巴西电商市场准入指南：中国卖家必读（2024）</h1>',
            1
        )
        changes.append("Title translated to Chinese")
    
    content = content.replace('<span>🇧🇷 Brasil</span>', '<span>🇧🇷 巴西</span>', 1)
    
    return content, changes

def translate_meli_es(content):
    """翻译美客多文章"""
    changes = []
    
    if 'ESPAÑOL' in content:
        content = content.replace('<span class="badge badge-es">ESPAÑOL</span>', '<span class="badge badge-zh">中文</span>', 1)
        changes.append("Language badge: ESPAÑOL -> 中文")
    
    if 'Guía Completa para Abrir tu Tienda en Mercado Libre' in content:
        content = content.replace(
            '<h1>Guía Completa para Abrir tu Tienda en Mercado Libre: Paso a Paso 2024</h1>',
            '<h1>美客多Mercado Libre开店完整指南：手把手教程（2024）</h1>',
            1
        )
        changes.append("Title translated to Chinese")
    
    return content, changes

def translate_latam_logistics(content):
    """翻译拉美物流文章"""
    changes = []
    
    if 'ESPAÑOL' in content:
        content = content.replace('<span class="badge badge-es">ESPAÑOL</span>', '<span class="badge badge-zh">中文</span>', 1)
        changes.append("Language badge: ESPAÑOL -> 中文")
    
    if 'Comparación de Canales Logísticos' in content:
        content = content.replace(
            '<h1>Comparación de Canales Logísticos Transfronterizos en LATAM 2024</h1>',
            '<h1>拉美跨境物流渠道对比与成本分析（2024）</h1>',
            1
        )
        changes.append("Title translated to Chinese")
    
    return content, changes

def translate_payment_comparison(content):
    """翻译支付对比文章（已经是中文，只需检查）"""
    changes = []
    
    # 检查是否有中文标签
    if 'badge-es' in content or 'badge-pt' in content:
        content = content.replace('<span class="badge badge-es">ESPAÑOL</span>', '<span class="badge badge-zh">中文</span>', 1)
        content = content.replace('<span class="badge badge-pt">PORTUGUÊS</span>', '<span class="badge badge-zh">中文</span>', 1)
        changes.append("Language badge fixed")
    
    return content, changes

def main():
    print("=" * 60)
    print("Translate article content to Chinese")
    print("=" * 60)
    
    translations = {
        "article-mexico-customs.html": translate_mexico_customs,
        "article-brazil-market.html": translate_brazil_market,
        "article-meli-es.html": translate_meli_es,
        "article-latam-logistics-es.html": translate_latam_logistics,
        "article-payment-comparison.html": translate_payment_comparison,
    }
    
    for filename, translate_func in translations.items():
        target_file = WORKSPACE / filename
        if not target_file.exists():
            print(f"\nSKIP: {filename} not found")
            continue
        
        print(f"\nProcessing: {filename}")
        content = read_file(target_file)
        original = content
        
        content, changes = translate_func(content)
        
        if content != original:
            write_file(target_file, content)
            print(f"  [OK] Translated ({len(changes)} changes)")
            for c in changes:
                try:
                    print(f"    - {c}")
                except:
                    print(f"    - [translated]")
        else:
            print(f"  [OK] No changes needed")
    
    print("\n" + "=" * 60)
    print("Translation complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
