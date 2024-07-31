import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
import requests
from io import BytesIO

# Define function to send LINE notifications
def send_line_notify(message, image_file=None, sticker_package_id=None, sticker_id=None):
    URL = 'https://notify-api.line.me/api/notify/'
    TOKEN = 'YOUR_ACCESS_TOKEN'  # Replace with your LINE Notify access token
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }
    data = {
        'message': message
    }
    
    if sticker_package_id and sticker_id:
        data.update({
            'stickerPackageID': sticker_package_id,
            'stickerID': sticker_id
        })
        response = requests.post(URL, headers=headers, data=data)
    elif image_file:
        files = {
            'imageFile': image_file
        }
        response = requests.post(URL, headers=headers, data=data, files=files)
    else:
        response = requests.post(URL, headers=headers, data=data)
    
    return response

# Define callback function for button
def on_send_button_click():
    message = message_entry.get()
    
    option = option_var.get()
    
    if option == 'Line Sticker':
        sticker_package_id = simpledialog.askinteger('Sticker Package ID', 'Enter Sticker Package ID:')
        sticker_id = simpledialog.askinteger('Sticker ID', 'Enter Sticker ID:')
        if sticker_package_id and sticker_id:
            response = send_line_notify(message, sticker_package_id=sticker_package_id, sticker_id=sticker_id)
            result_text = f'Status Code: {response.status_code}\nResponse: {response.text}'
        else:
            result_text = 'Sticker Package ID and Sticker ID are required.'
    
    elif option == 'Local Image File':
        file_path = filedialog.askopenfilename(title='Select Image File', filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:
            with open(file_path, 'rb') as image_file:
                response = send_line_notify(message, image_file=BytesIO(image_file.read()))
                result_text = f'Status Code: {response.status_code}\nResponse: {response.text}'
        else:
            result_text = 'No file selected.'
    
    elif option == 'Web Image File':
        img_url = simpledialog.askstring('Image URL', 'Enter the image URL:')
        if img_url:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                image_file = BytesIO(img_response.content)
                response = send_line_notify(message, image_file=image_file)
                result_text = f'Status Code: {response.status_code}\nResponse: {response.text}'
            else:
                result_text = 'Failed to download image from URL.'
        else:
            result_text = 'No URL provided.'
    
    else:
        result_text = 'Please select an option.'
    
    messagebox.showinfo('Result', result_text)

# Set up the GUI
root = tk.Tk()
root.title('LINE Notify Sender')

tk.Label(root, text='Select Notification Type:').pack(pady=10)

option_var = tk.StringVar(value='Select an option')
options = ['Line Sticker', 'Local Image File', 'Web Image File']
option_menu = ttk.Combobox(root, textvariable=option_var, values=options)
option_menu.pack(pady=5)

tk.Label(root, text='Enter Message:').pack(pady=10)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

send_button = tk.Button(root, text='Send', command=on_send_button_click)
send_button.pack(pady=20)

root.mainloop()