const fs = require('fs');
const path = require('path');

// Günlük etkinlik şablonu
function createEventHTML(event) {
    const locationColor = event.isOnline ? '#ff6b6b' : '#4a90e2';
    const locationIcon = event.isOnline ? '🌐' : '📍';
    
    return `
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #2a7a7a; margin-bottom: 2px;">
        <tr>
            <td style="padding: 15px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                    <tr>
                        <td width="60" valign="top" style="padding-right: 15px;">
                            <div style="width: 50px; height: 50px; background-color: #ffffff; border-radius: 8px; display: inline-block; text-align: center; line-height: 50px; font-size: 24px;">
                                ${event.clubIcon || '🎯'}
                            </div>
                        </td>
                        <td valign="top">
                            <div style="color: #ffffff; font-size: 13px; font-weight: bold; margin-bottom: 5px;">
                                ${event.clubName}
                            </div>
                            <div style="color: #ffd700; font-size: 15px; font-weight: bold; margin-bottom: 8px;">
                                ${event.eventTitle}
                            </div>
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0">
                                <tr>
                                    <td style="color: #ffffff; font-size: 12px; padding-right: 15px;">
                                        🕐 ${event.time}
                                    </td>
                                    <td style="color: ${locationColor}; font-size: 12px;">
                                        ${locationIcon} ${event.location}
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    `;
}

// Günlük bölüm şablonu
function createDaySection(day) {
    const dayName = day.dayName;
    const date = day.date;
    const events = day.events || [];
    
    let eventsHTML = '';
    events.forEach(event => {
        eventsHTML += createEventHTML(event);
    });
    
    return `
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 15px;">
        <tr>
            <td style="padding: 15px 20px; background-color: #2a7a7a;">
                <div style="color: #ffd700; font-size: 16px; font-weight: bold; margin-bottom: 10px;">
                    ${date} - ${dayName.toUpperCase()}
                </div>
            </td>
        </tr>
        <tr>
            <td style="padding: 0;">
                ${eventsHTML}
            </td>
        </tr>
    </table>
    `;
}

// Ana HTML oluşturma fonksiyonu
function generateEmailHTML(data) {
    const templatePath = path.join(__dirname, 'template.html');
    let template = fs.readFileSync(templatePath, 'utf8');
    
    // Tarih aralığını değiştir
    const dateRange = `${data.startDate} - ${data.endDate} HAFTASI`;
    template = template.replace('{{DATE_RANGE}}', dateRange);
    
    // Etkinlikleri oluştur
    let eventsContent = '';
    data.days.forEach(day => {
        eventsContent += createDaySection(day);
    });
    
    template = template.replace('{{EVENTS_CONTENT}}', eventsContent);
    
    return template;
}

// Ana fonksiyon
function main() {
    const dataPath = path.join(__dirname, 'events-data.json');
    const outputPath = path.join(__dirname, 'output-email.html');
    
    if (!fs.existsSync(dataPath)) {
        console.error('Hata: events-data.json dosyası bulunamadı!');
        process.exit(1);
    }
    
    const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
    const html = generateEmailHTML(data);
    
    fs.writeFileSync(outputPath, html, 'utf8');
    console.log('✅ E-posta HTML dosyası başarıyla oluşturuldu: output-email.html');
}

if (require.main === module) {
    main();
}

module.exports = { generateEmailHTML, createDaySection, createEventHTML };

