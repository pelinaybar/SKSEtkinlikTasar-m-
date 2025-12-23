#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Üsküdar Üniversitesi Haftalık Etkinlik Programı E-Posta Oluşturucu
Python versiyonu
"""

import json
import os
from pathlib import Path

def create_event_html(event):
    """Tek bir etkinlik için HTML oluşturur"""
    location_color = '#ff6b6b' if event.get('isOnline', False) else '#4a90e2'
    location_icon = '🌐' if event.get('isOnline', False) else '📍'
    club_icon = event.get('clubIcon', '🎯')
    
    return f"""
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #2a7a7a; margin-bottom: 2px;">
        <tr>
            <td style="padding: 15px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                    <tr>
                        <td width="60" valign="top" style="padding-right: 15px;">
                            <div style="width: 50px; height: 50px; background-color: #ffffff; border-radius: 8px; display: inline-block; text-align: center; line-height: 50px; font-size: 24px;">
                                {club_icon}
                            </div>
                        </td>
                        <td valign="top">
                            <div style="color: #ffffff; font-size: 13px; font-weight: bold; margin-bottom: 5px;">
                                {event.get('clubName', '')}
                            </div>
                            <div style="color: #ffd700; font-size: 15px; font-weight: bold; margin-bottom: 8px;">
                                {event.get('eventTitle', '')}
                            </div>
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0">
                                <tr>
                                    <td style="color: #ffffff; font-size: 12px; padding-right: 15px;">
                                        🕐 {event.get('time', '')}
                                    </td>
                                    <td style="color: {location_color}; font-size: 12px;">
                                        {location_icon} {event.get('location', '')}
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    """

def create_day_section(day):
    """Bir günün tüm etkinlikleri için HTML oluşturur"""
    day_name = day.get('dayName', '')
    date = day.get('date', '')
    events = day.get('events', [])
    
    events_html = ''.join([create_event_html(event) for event in events])
    
    return f"""
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 15px;">
        <tr>
            <td style="padding: 15px 20px; background-color: #2a7a7a;">
                <div style="color: #ffd700; font-size: 16px; font-weight: bold; margin-bottom: 10px;">
                    {date} - {day_name.upper()}
                </div>
            </td>
        </tr>
        <tr>
            <td style="padding: 0;">
                {events_html}
            </td>
        </tr>
    </table>
    """

def generate_email_html(data):
    """Ana HTML e-posta dosyasını oluşturur"""
    script_dir = Path(__file__).parent
    template_path = script_dir / 'template.html'
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Tarih aralığını değiştir
    date_range = f"{data.get('startDate', '')} - {data.get('endDate', '')} HAFTASI"
    template = template.replace('{{DATE_RANGE}}', date_range)
    
    # Etkinlikleri oluştur
    events_content = ''.join([create_day_section(day) for day in data.get('days', [])])
    template = template.replace('{{EVENTS_CONTENT}}', events_content)
    
    return template

def main():
    """Ana fonksiyon"""
    script_dir = Path(__file__).parent
    data_path = script_dir / 'events-data.json'
    output_path = script_dir / 'output-email.html'
    
    if not data_path.exists():
        print('Hata: events-data.json dosyası bulunamadı!')
        return
    
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html = generate_email_html(data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print('✅ E-posta HTML dosyası başarıyla oluşturuldu: output-email.html')

if __name__ == '__main__':
    main()


