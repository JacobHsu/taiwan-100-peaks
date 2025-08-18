document.addEventListener('DOMContentLoaded', function() {
    // 初始化地圖 - 調整為顯示整個台灣
    const map = L.map('map').setView([23.8, 120.9], 10);

    // 添加地圖圖層 - 使用衛星影像圖層
    const satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
        maxZoom: 18
    });

    // 添加街道地圖圖層
    const streetLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
    });

    // 默認使用衛星圖層
    satelliteLayer.addTo(map);

    // 圖層控制
    const baseLayers = {
        '衛星影像': satelliteLayer,
        '街道地圖': streetLayer
    };
    L.control.layers(baseLayers).addTo(map);

    // 存儲標記的對象
    const markers = {};
    let activeMarker = null;

    // 自定義山峰圖標
    const peakIcon = L.divIcon({
        html: '<div class="custom-peak-marker">🏔️</div>',
        className: 'custom-peak-icon',
        iconSize: [30, 30],
        iconAnchor: [15, 30]
    });

    const activePeakIcon = L.divIcon({
        html: '<div class="custom-peak-marker active">🏔️</div>',
        className: 'custom-peak-icon',
        iconSize: [35, 35],
        iconAnchor: [17.5, 35]
    });

    // 為每個山峰添加標記
    peaksData.forEach(peak => {
        const marker = L.marker([peak.lat, peak.lng], { icon: peakIcon })
            .addTo(map)
            .bindPopup(`
                <div class="popup-content">
                    <h3>${peak.name}</h3>
                    <p><strong>海拔：</strong>${peak.elevation}</p>
                    <p><strong>區域：</strong>${peak.status}</p>
                    <p>${peak.description}</p>
                </div>
            `);

        // 標記點擊事件
        marker.on('click', function() {
            highlightPeakCard(peak.id);
            setActiveMarker(marker);
        });

        markers[peak.id] = marker;
    });

    // 設置活躍標記
    function setActiveMarker(marker) {
        // 重置所有標記為普通狀態
        Object.values(markers).forEach(m => {
            m.setIcon(peakIcon);
        });
        
        // 設置選中標記為活躍狀態
        marker.setIcon(activePeakIcon);
        activeMarker = marker;
    }

    // 高亮顯示對應的山峰卡片
    function highlightPeakCard(peakId) {
        // 移除所有活躍狀態
        document.querySelectorAll('.peak-item').forEach(item => {
            item.classList.remove('active');
        });

        // 添加活躍狀態到對應卡片
        const targetCard = document.querySelector(`[data-peak-id="${peakId}"]`);
        if (targetCard) {
            targetCard.classList.add('active');
            // 滾動到該卡片
            targetCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // 山峰卡片點擊事件
    document.querySelectorAll('.peak-item').forEach(item => {
        item.addEventListener('click', function() {
            const peakId = parseInt(this.dataset.peakId);
            const lat = parseFloat(this.dataset.lat);
            const lng = parseFloat(this.dataset.lng);

            // 移動地圖到對應位置
            map.setView([lat, lng], 12);

            // 設置活躍標記
            const marker = markers[peakId];
            if (marker) {
                setActiveMarker(marker);
                marker.openPopup();
            }

            // 高亮當前卡片
            highlightPeakCard(peakId);
        });

        // 卡片懸停效果
        item.addEventListener('mouseenter', function() {
            const peakId = parseInt(this.dataset.peakId);
            const marker = markers[peakId];
            if (marker && marker !== activeMarker) {
                marker.setIcon(activePeakIcon);
            }
        });

        item.addEventListener('mouseleave', function() {
            const peakId = parseInt(this.dataset.peakId);
            const marker = markers[peakId];
            if (marker && marker !== activeMarker) {
                marker.setIcon(peakIcon);
            }
        });
    });

    // 地圖點擊事件 - 取消選中狀態
    map.on('click', function(e) {
        // 如果點擊的不是標記，則取消所有選中狀態
        if (!e.originalEvent.target.closest('.custom-peak-marker')) {
            document.querySelectorAll('.peak-item').forEach(item => {
                item.classList.remove('active');
            });
            Object.values(markers).forEach(m => {
                m.setIcon(peakIcon);
            });
            activeMarker = null;
        }
    });
});