# 代碼品質和架構標準

這些指令自動應用於整個 test_space 專案，確保代碼品質和一致性。

## CSS 規範

### 禁止硬編碼顏色和數值
❌ **禁止**：
```css
.button {
    color: #667eea;
    padding: 12px 15px;
    border-radius: 10px;
}
```

✅ **必須使用 CSS 變數**：
```css
:root {
    --color-primary: #667eea;
    --spacing-md: 15px;
    --radius-md: 10px;
}

.button {
    color: var(--color-primary);
    padding: var(--spacing-md);
    border-radius: --radius-md;
}
```

### Design Token 系統
必須定義以下類別的 CSS 變數：
- **色彩系統**：主色、副色、中性色、狀態色（success/error/warning）
- **間距系統**：xs, sm, md, lg, xl, 2xl 等
- **圓角系統**：sm, md, lg, xl
- **陰影系統**：sm, md, lg
- **排版系統**：字號、字族、行高
- **動畫系統**：過渡時間等

## JavaScript 架構規範

### Component-Based 結構
必須将代碼分解為多個清晰職責的 components/modules：

```javascript
// ❌ 禁止：所有邏輯混在一個檔案
function searchCity() { ... }
function getWeather() { ... }
function formatData() { ... }

// ✅ 必須：分解為 components
const APIService = { ... }
const DataTransformer = { ... }
const UIManager = { ... }
const ApplicationLogic = { ... }
```

### 標準 Component 結構

#### 1. 配置 Component (Config)
負責常量和配置參數：
```javascript
const API_CONFIG = {
    GEO_API: 'https://...',
    WEATHER_API: 'https://...',
    TIMEOUT: 5000,
};
```

#### 2. DOM 管理 Component (DOMManager)
負責所有 DOM 操作和狀態管理：
```javascript
const DOMManager = {
    elements: { ... },
    init() { ... },
    showLoading() { ... },
    showError(message) { ... },
};
```

#### 3. 數據轉換 Component (Transformer/Formatter)
負責業務邏輯和數據格式化：
```javascript
const DataTransformer = {
    MAPPING: { ... },
    transform(rawData) { ... },
    format(value, type) { ... },
};
```

#### 4. API 服務 Component (APIService)
負責所有 HTTP 請求和網絡邏輯：
```javascript
const APIService = {
    async fetchWithTimeout(url, timeout) { ... },
    async getGeoData(city) { ... },
    async getWeatherData(lat, lon) { ... },
};
```

#### 5. 應用邏輯 Component (AppLogic/MainApp)
負責業務流程和組件協調：
```javascript
const WeatherApp = {
    async searchCity(city) { ... },
    updateUI(data) { ... },
};
```

### Production-Ready 要求

✅ **必須包含**：
- 錯誤處理和邊界情況處理
- 超時控制（防止永久掛起）
- 驗證輸入
- 有意義的錯誤信息
- 日誌/console 調試信息
- 初始化和清理函数

✅ **必須避免**：
- 全局變數污染
- 硬編碼的API端點（必須在CONFIG)
- 混合關注點
- 過長的函數（超過50行需要拆分）

## 檔案組織

```
project/
├── .github/
│   └── copilot-instructions.md (本檔案)
├── index.html (HTML + 內聯 CSS + 內聯 JS)
├── main.py (Flask 備選方案)
├── requirements.txt
├── README.md
└── skills/
    └── skill1.md (編碼標準參考)
```

## 代碼審查清單

在提交代碼前，檢查：

- [ ] CSS：所有顏色、間距、圓角等都用變數替換了嗎？
- [ ] CSS：CSS 變數定義在 `:root` 中了嗎？
- [ ] JavaScript：代碼分解成了多個職責清晰的 components 嗎？
- [ ] JavaScript：是否有超時控制和錯誤處理？
- [ ] JavaScript：是否避免了硬編碼的配置值？
- [ ] JavaScript：所有 DOM 操作集中在 DOM Manager 了嗎？
- [ ] 函數：是否清楚、精簡、單一職責？
- [ ] 註解：複雑邏輯有清晰的註解嗎？

## 提交信息規範

使用 Conventional Commits 格式：

```
feat: 新增功能簡述
fix: 修復 bug 簡述
style: CSS/格式化改進
refactor: 代碼重構不改變功能
docs: 文檔更新
test: 添加或修改測試
```

例子：
```
refactor: 根據設計規範重構 CSS 為 Design Token 系統

- 提取所有硬編碼顏色到 CSS 變數
- 定義統一的間距系統
- 提高樣式可維護性
```

## 相關資源

- [skill1.md](../skills/skill1.md) - 詳細的編碼標準參考
- [CSS Design System](./copilot-instructions.md) - 本檔案
