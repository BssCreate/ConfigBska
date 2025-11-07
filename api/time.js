// api/time.js
export default async function handler(req, res) {
  try {
    // Можно добавить кеширование на 1 минуту
    res.setHeader('Cache-Control', 'public, max-age=60');
    
    const currentTime = Math.floor(Date.now() / 1000);
    
    res.status(200).json({
      unixtime: currentTime,
      iso: new Date().toISOString(),
      timezone: 'UTC',
      success: true
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Server error'
    });
  }
}
