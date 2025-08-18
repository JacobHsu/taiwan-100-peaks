# 台灣百岳專案 - Docker 啟動教學

## 📋 前置條件

### 必需軟體
**Docker Desktop**
- 下載：https://www.docker.com/products/docker-desktop/
- 安裝後請確保 Docker Desktop 正在運行

## 🚀 啟動步驟

### 步驟 1：確認 Docker 已安裝並啟動
```bash
docker --version
docker-compose --version
```

### 步驟 2：進入專案資料夾
```bash
cd D:\2-outsourcing\hiking\taiwan-100-peaks
```

### 步驟 3：啟動服務
```bash
docker-compose up --build
```

### 步驟 4：等待服務啟動完成
- 第一次會下載 PostgreSQL + PostGIS 映像檔
- 等待看到 "Starting development server at http://0.0.0.0:8000/"
- 資料庫健康檢查通過後，網站才會啟動

### 步驟 5：執行資料庫遷移
**另開一個終端機執行：**
```bash
docker-compose exec web python manage.py migrate
```

### 步驟 6：創建管理員帳號（可選）
```bash
docker-compose exec web python manage.py createsuperuser
```

### 步驟 7：開啟瀏覽器
**網站首頁：** `http://localhost:3952`
**管理後台：** `http://localhost:3952/admin`

🎉 **恭喜！你的台灣百岳網站已經啟動成功了！**

---

## 📊 資料庫特色

本專案使用 **PostgreSQL + PostGIS** 具有以下優勢：

### 🗺️ 地理空間功能
- **座標儲存**：每座山的精確經緯度
- **地理查詢**：找出附近的山峰
- **距離計算**：計算山峰間的實際距離
- **地圖整合**：支援各種地圖服務

### 🏔️ Peak 模型欄位
```python
name          # 百岳名稱 (例: 玉山主峰)
elevation     # 海拔高度 (例: 3952 公尺)
location      # 經緯度座標 (PostGIS Point)
difficulty    # 難度等級 (初級/中級/高級/專家級)
distance      # 來回距離 (公里)
duration_days # 預估天數
status        # 完成狀態 (未完成/已完成/計劃中)
completion_date # 完成日期
planned_date  # 計劃日期
```

---

## 🛠️ 常見問題解決

### Q1: Docker 啟動失敗
**解決方法**：
- 確認 Docker Desktop 正在運行
- 重啟 Docker Desktop
- 檢查防火牆設定

### Q2: Port 3952 被佔用
**解決方法**：
```bash
# 查看佔用 port 的程序
netstat -ano | findstr :3952

# 或修改 docker-compose.yml 中的 port
# 將 "3952:8000" 改為 "3953:8000"
```

### Q3: 資料庫連線失敗
**解決方法**：
```bash
# 檢查資料庫容器狀態
docker-compose ps

# 重新啟動服務
docker-compose down
docker-compose up --build
```

### Q4: 遷移執行失敗
**解決方法**：
```bash
# 等待資料庫完全啟動後再執行
docker-compose exec web python manage.py migrate

# 如果還是失敗，檢查資料庫日誌
docker-compose logs db
```

---

## 📁 專案結構說明

```
taiwan-100-peaks/
├── docker-compose.yml    # Docker 服務配置
├── Dockerfile           # Docker 建置設定
├── requirements.txt     # Python 套件清單
├── manage.py           # Django 管理檔案
├── .env.example        # 環境變數範例
├── taiwan_peaks/       # Django 主設定
├── peaks/             # 百岳應用程式
│   ├── models.py      # 資料模型 (含地理空間)
│   ├── views.py       # 視圖邏輯
│   └── admin.py       # 管理後台
├── templates/         # HTML 模板
└── static/           # 靜態檔案
```

---

## 🎯 下一步可以做什麼

1. **管理後台新增百岳資料**：訪問 `http://localhost:3952/admin`
2. **修改網站樣式**：編輯 `static/css/style.css`
3. **新增地圖功能**：整合 Google Maps 或 OpenStreetMap
4. **API 開發**：為手機 App 提供資料介面

---

## 🆘 需要幫助？

1. **檢查 Docker 日誌**：`docker-compose logs`
2. **進入容器除錯**：`docker-compose exec web bash`
3. **重置所有服務**：`docker-compose down -v && docker-compose up --build`

---

## 🎊 成功畫面

當你成功啟動後，應該會看到：
- ✅ 頂部有 logo 和天氣的導航列
- ✅ 左側有台灣百岳列表
- ✅ 右側有地圖區域（開發中）
- ✅ 現代化的漸層背景設計
- ✅ Port 3952（玉山主峰海拔高度）

**祝你開發愉快！** 🏔️