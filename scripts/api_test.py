#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEGO BrickFinder - API Integration & Data Validation Script
Description: 用於測試 Rebrickable API 連線狀態、驗證 API Key，並預覽樂高盒組與主題系列之資料結構。
Author: Your Name
Date: 2026
"""

import os
import json
import requests

# === 全域設定 ===
# 建議實務上可改用 os.getenv('REBRICKABLE_API_KEY') 從環境變數讀取
API_KEY = '8cbdfafeaae44206585e06909cf319fc' 
BASE_URL = 'https://rebrickable.com/api/v3/lego'

# 設定請求表頭 (Request Headers)
HEADERS = {
    'Authorization': f'key {API_KEY}',
    'Accept': 'application/json'
}

def test_lego_set_api(set_id="10333-1"):
    """
    測試樂高特定盒組的 API 連線與資料擷取
    """
    url = f"{BASE_URL}/sets/{set_id}/"
    print(f"==================================================")
    print(f"🚀 正在發送請求至盒組 API... ")
    print(f"🔗 URL: {url}")
    print(f"==================================================")
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        # 檢查 HTTP 狀態碼是否為 200 系列，否則拋出異常
        response.raise_for_status()
        
        # 解析 JSON 資料
        data = response.json()
        print("✅ 連線成功！成功擷取資料。")
        print(f"📦 盒組名稱: {data.get('name')}")
        print(f"🔢 零件數量: {data.get('num_parts')} pcs")
        print(f"📅 發行年份: {data.get('year')}")
        print(f"🎨 主題 ID (Theme ID): {data.get('theme_id')}")
        print(f"🖼️ 圖片連結: {data.get('set_img_url')}")
        
        # 返回 theme_id 供後續測試主題 API
        return data.get('theme_id')

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP 錯誤發生: {http_err}")
        if response.status_code == 404:
            print("💡 提示: 找不到該樂高型號，請檢查型號後綴是否加上 '-1'。")
        elif response.status_code == 401:
            print("💡 提示: 認證失敗，請檢查你的 API_KEY 是否正確。")
    except requests.exceptions.ConnectionError:
        print("❌ 網路連線錯誤，請檢查您的網路狀態。")
    except requests.exceptions.Timeout:
        print("❌ 請求逾時 (Timeout)。")
    except Exception as err:
        print(f"❌ 發生預期之外的錯誤: {err}")
    
    return None

def test_lego_theme_api(theme_id):
    """
    根據盒組回傳的 theme_id，測試系列主題 API
    """
    if not theme_id:
        print("\n⚠️ 缺少 Theme ID，跳過主題 API 測試。")
        return

    url = f"{BASE_URL}/themes/{theme_id}/"
    print(f"\n==================================================")
    print(f"🚀 正在發送請求至系列主題 API...")
    print(f"🔗 URL: {url}")
    print(f"==================================================")

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        theme_data = response.json()
        print("✅ 連線成功！成功擷取主題資料。")
        print(f"🏷️ 系列名稱 (Theme Name): {theme_data.get('name')}")
        
    except Exception as err:
        print(f"❌ 擷取主題資料失敗: {err}")

if __name__ == "__main__":
    # 執行主測試流程
    # 預設測試魔戒巴拉多盒組 (10333-1)
    target_set = "10333-1" 
    
    detected_theme_id = test_lego_set_api(target_set)
    test_lego_theme_api(detected_theme_id)
    
    print(f"\n==================================================")
    print("🏁 API 驗證測試結束")
    print(f"==================================================")
