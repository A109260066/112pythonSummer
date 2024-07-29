import tkinter as tk
from tkinter import messagebox
import requests

# LINE Notify API 配置
URL = 'https://notify-api.line.me/api/notify/'
ACCESS_TOKEN = 'ncgcrKBszCeRdtl4CCm8smbdclaiHHR7XDVjhdGDVWB'

def send_message():
    message = message_entry.get()
    if not message:
        messagebox.showwarning("输入错误", "消息不能为空!")
        return
    
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    payload = {
        'message': message
    }
    
    response = requests.post(URL, headers=headers, data=payload)
    
    if response.status_code == 200:
        messagebox.showinfo("成功", "消息已成功发送到 LINE!")
    else:
        messagebox.showerror("错误", f"消息发送失败: {response.text}")

# 创建主窗口
root = tk.Tk()
root.title("LINE Notify 消息发送器")

# 创建并放置标签、输入框和按钮
tk.Label(root, text="请输入消息:").pack(pady=10)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

send_button = tk.Button(root, text="发送", command=send_message)
send_button.pack(pady=20)

# 运行主事件循环
root.mainloop()
