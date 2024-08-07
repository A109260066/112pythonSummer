import tkinter as tk
from tkinter import ttk
import requests

# 取得氣象數據
URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {'Authorization': 'CWB-80B8FFEA-FFCC-4931-B91C-C38CD577ACD7'}

def fetch_data():
    try:
        response = requests.get(URL, params=P)
        response.raise_for_status()  # 如果HTTP請求返回錯誤碼，會引發異常
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return {'records': {'Station': []}}  # 初始化為空數據以避免錯誤

data = fetch_data()

# 從數據中提取站點名稱列表
station_list = [station['StationName'] for station in data['records']['Station']]

def update_info(event):
    station_name = station_var.get()
    station_data = next((station for station in data['records']['Station'] if station['StationName'] == station_name), None)
    
    # 清空現有顯示
    for widget in info_frame.winfo_children():
        widget.destroy()
    
    if station_data:
        # 確保 'WeatherElement' 存在並且有相應的數據
        weather_elements = station_data.get('WeatherElement', {})
        air_temp = weather_elements.get('AirTemperature', 'N/A')
        relative_humidity = weather_elements.get('RelativeHumidity', 'N/A')
        weather = weather_elements.get('Weather', 'N/A')

        tk.Label(info_frame, text=f"觀測地點: {station_data['StationName']}", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', padx=10, pady=5)
        tk.Label(info_frame, text=f"觀測時間: {station_data['ObsTime']['DateTime']}", font=('Arial', 12)).grid(row=1, column=0, sticky='w', padx=10, pady=5)
        tk.Label(info_frame, text=f"觀測溫度: {air_temp} °C", font=('Arial', 12)).grid(row=2, column=0, sticky='w', padx=10, pady=5)
        tk.Label(info_frame, text=f"觀測濕度: {relative_humidity} %", font=('Arial', 12)).grid(row=3, column=0, sticky='w', padx=10, pady=5)
        tk.Label(info_frame, text=f"觀測天氣: {weather}", font=('Arial', 12)).grid(row=4, column=0, sticky='w', padx=10, pady=5)
    else:
        tk.Label(info_frame, text="站點資訊不存在", font=('Arial', 12, 'bold'), fg='red').grid(row=0, column=0, padx=10, pady=10)

# 初始化Tkinter窗口
root = tk.Tk()
root.title("Weather Station Info")
root.geometry("350x250")  # 設置窗口大小

# 創建下拉式選單
station_var = tk.StringVar()
station_menu = ttk.Combobox(root, textvariable=station_var)
station_menu['values'] = station_list
station_menu.bind('<<ComboboxSelected>>', update_info)
station_menu.pack(pady=10, padx=10)

# 顯示觀測資訊的框架
info_frame = tk.Frame(root)
info_frame.pack(pady=10, padx=10, fill='both', expand=True)

# 啟動Tkinter事件循環
root.mainloop()
