document.addEventListener('DOMContentLoaded', function() {
    const weatherElement = document.querySelector('.navbar-weather');
    
    function updateWeather() {
        // Simple weather simulation - in production you'd use a real weather API
        const weatherConditions = [
            { icon: '☀️', text: '晴天' },
            { icon: '⛅', text: '多雲' },
            { icon: '🌤️', text: '晴時多雲' },
            { icon: '🌧️', text: '雨天' }
        ];
        
        const randomWeather = weatherConditions[Math.floor(Math.random() * weatherConditions.length)];
        
        const weatherIcon = weatherElement.querySelector('.weather-icon');
        const weatherText = weatherElement.querySelector('.weather-text');
        
        if (weatherIcon && weatherText) {
            weatherIcon.textContent = randomWeather.icon;
            weatherText.textContent = randomWeather.text;
        }
    }
    
    // Update weather every 30 seconds
    updateWeather();
    setInterval(updateWeather, 30000);
    
    // Add click handler for weather
    weatherElement.addEventListener('click', function() {
        alert('天氣資訊功能開發中...');
    });
});