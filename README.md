# 🧱 LEGO BrickFinder | 樂高型號查詢系統

一個專為樂高愛好者設計的型號搜尋網站。使用者只需輸入樂高盒組型號（如 `10333`），系統便會透過 **Rebrickable API** 即時動態抓取該盒組的完整資訊，包含官方圖片、零件總數、發行年份及所屬主題系列，並提供在地化的搜尋歷史紀錄與個人收藏清單功能。

## 🚀 核心功能

- **即時 API 數據檢索**：串接全球最大樂高資料庫 Rebrickable，動態渲染最新、最準確的樂高盒組規格。
- **防禦性程式設計（Defensive Programming）**：完善的異常處理機制，友善攔截 API 路徑錯誤與 404 找不到型號之狀況，提升使用者體驗。
- **流暢的動態互動（UI/UX）**：整合 Tailwind CSS 響應式設計，並加入愛心微動效、卡片滑入動畫與加載中狀態鎖定（防重複點擊）。
- **輕量化狀態管理**：完全無需後端資料庫，純利用瀏覽器 `LocalStorage` 實現「最近搜尋歷史」與「我的收藏清單」之資料持久化。

---

## 🛠️ 技術堆疊 (Tech Stack)

- **前端(FrontEnd)**: HTML5, JavaScript (ES6+, Async/Await), Tailwind CSS
- **後端(BackEnd / Scripting)**: Python (資料分析/預處理腳本)
- **Data Source**: Rebrickable API v3

---

## 💻 負責內容與技術實現

此專案中，獨立負責從 API 對接、前端介面開發到錯誤處理的完整流程：

### 1. 核心 API 串接與資料預處理
- 使用 JavaScript `fetch` 非同步架構（Async/Await）串接 Rebrickable 盒組與主題（Themes）API。
- 針對 API 規範自動進行型號補正（例如：自動將使用者輸入的 `10333` 格式化為官方規格的 `10333-1`）。
- 同步搭配 Python 腳本進行 API 測試、資料欄位結構分析與預處理驗證。

### 2. 響應式搜尋介面與動態渲染
- 運用 Tailwind CSS 打造 RWD 響應式介面，完美兼容手機與桌機視窗。
- 動態操控 DOM 節點，結合 `setTimeout` 與 CSS Keyframes 觸發結果圖層的淡入動畫、卡片交錯滑入效果。

### 3. 完善的容錯與異常處理 (Error Handling)
- 實作 `try...catch` 監聽網路請求，精準擷取 `!response.ok` 等非 200 狀態碼。
- 針對常見的 404（找不到型號）或網路斷線問題，設計防錯提示圖層（`statusMsg`），避免網頁畫面崩潰或無回應。
- 在發送請求期間，動態為按鈕動態注入 `btn-loading` 樣式並開啟 `pointer-events: none`，阻擋使用者的重複無效點擊。

### 4. 外部詳細資料導向
- 串接 Rebrickable 原廠 URL 數據，建立安全的外部連結導向（使用 `target="_blank"` 與 `rel="noopener noreferrer"` 防範安全漏洞），提供使用者深度的樂高零件清單與圖紙檢視。

---

## 📦 專案結構

```text
├── index.html          # 前端核心頁面 (包含 HTML 結構、Tailwind 樣式與 JS 邏輯)
├── scripts/
│   └── api_test.py     # Python API 資料驗證與結構測試腳本
└── README.md           # 專案說明文件

