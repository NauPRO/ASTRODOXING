from tkinter import colorchooser  # Importar colorchooser
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
from tkinter import PhotoImage

# Función para abrir el navegador
def open_browser(url):
    webbrowser.open_new_tab(url)

# --- FUNCIONES DE BÚSQUEDA ---
def search_ip():
    ip = ip_entry.get()
    if ip:
        url = f"https://ipinfo.io/{ip}"
        open_browser(url)
    else:
        messagebox.showwarning("Input Error", "Please enter an IP address.")

def search_name():
    name = name_entry.get()
    if name:
        url = f"https://www.pipl.com/search/?q={name}"
        open_browser(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a name and last name.")

def search_number():
    number = number_entry.get()
    if number:
        url = f"https://www.truecaller.com/search/{number}"
        open_browser(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a phone number.")

def search_company():
    company = company_entry.get()
    if company:
        url = f"https://www.glassdoor.com.ar/Reviews/index.htm?countryRedirect=true/{company}"
        open_browser(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a company name.")

def go_to_telegram():
    telegram_url = "https://t.me/MOSCAMBULO"
    open_browser(telegram_url)

# --- CAMBIO DE COLORES ---
def change_background():
    color = colorchooser.askcolor(title="Select Background Color")[1]
    if color:
        root.configure(bg=color)
        menu_frame.configure(bg=color)
        search_frame.configure(bg=color)
        settings_frame.configure(bg=color)
        more_tools_frame.configure(bg=color)

def change_text_color():
    color = colorchooser.askcolor(title="Select Text Color")[1]
    if color:
        for widget in menu_frame.winfo_children() + search_frame.winfo_children() + settings_frame.winfo_children() + more_tools_frame.winfo_children():
            if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                widget.configure(fg=color)

# --- VENTANA PRINCIPAL Y MENÚ ---
root = tk.Tk()
root.title("ASTRODOX Prototype")
root.geometry("900x600")
root.configure(bg="#000000")
root.resizable(False, False)

menu_frame = tk.Frame(root, bg="#0A0A0A", padx=20, pady=20)
menu_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(menu_frame, text="Welcome to ASTRODOX!", fg="#00FF00", bg="#0A0A0A", font=("Courier", 18, "bold"))
welcome_label.pack(pady=10)

# Funciones para mostrar las diferentes secciones
def show_search_section():
    menu_frame.pack_forget()
    search_frame.pack(fill="both", expand=True)

def show_settings_section():
    menu_frame.pack_forget()
    settings_frame.pack(fill="both", expand=True)

def show_about_section():
    # Cambiar el color de fondo y el texto
    messagebox.showinfo(
        "About", 
        "ASTRODOX Prototype\nVersion 2.0\nCreated by Noctámbulo", 
        icon='info'
    )
    # Personalizar el fondo y el color del texto del pop-up
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("400x200")
    about_window.configure(bg="#000000")

    about_label = tk.Label(about_window, 
                           text="ASTRODOX Prototype\nVersion 2.0\nCreated by Noctámbulo", 
                           fg="#FF0000",  # Rojo vivo
                           bg="#000000",  # Fondo negro
                           font=("Courier", 14, "bold"),
                           justify="center")
    about_label.pack(expand=True)
    
    close_button = tk.Button(about_window, 
                             text="Close", 
                             command=about_window.destroy, 
                             fg="#FF0000",  # Rojo vivo
                             bg="#000000",  # Fondo negro
                             font=("Courier", 12))
    close_button.pack(pady=20)

def show_more_tools():
    menu_frame.pack_forget()
    more_tools_frame.pack(fill="both", expand=True)

def back_to_menu():
    search_frame.pack_forget()
    settings_frame.pack_forget()
    more_tools_frame.pack_forget()
    menu_frame.pack(fill="both", expand=True)

# Botones del menú principal
button_search = tk.Button(menu_frame, text="Search Information", command=show_search_section, fg="#00FF00", bg="#0A0A0A", font=("Courier", 14), width=25, pady=10)
button_search.pack(pady=10)

button_settings = tk.Button(menu_frame, text="Settings", command=show_settings_section, fg="#00FF00", bg="#0A0A0A", font=("Courier", 14), width=25, pady=10)
button_settings.pack(pady=10)

button_about = tk.Button(menu_frame, text="About", command=show_about_section, fg="#00FF00", bg="#0A0A0A", font=("Courier", 14), width=25, pady=10)
button_about.pack(pady=10)

button_more_tools = tk.Button(menu_frame, text="More Tools", command=show_more_tools, fg="#00FF00", bg="#0A0A0A", font=("Courier", 14), width=25, pady=10)
button_more_tools.pack(pady=10)

button_telegram = tk.Button(menu_frame, text="Go to Telegram", command=go_to_telegram, fg="#00FF00", bg="#0A0A0A", font=("Courier", 14), width=25, pady=10)
button_telegram.pack(pady=10)

logo_image = PhotoImage(file="logo.png")
logo_label = tk.Label(menu_frame, image=logo_image, bg="#0A0A0A")
logo_label.pack(side="bottom", pady=20)

# --- SECCIÓN DE BÚSQUEDA ---
search_frame = tk.Frame(root, bg="#0A0A0A", padx=20, pady=20)

search_label = tk.Label(search_frame, text="Search Options", fg="#00FFFF", bg="#0A0A0A", font=("Courier", 16, "bold"))
search_label.pack(pady=10)

ip_entry = tk.Entry(search_frame, font=("Courier", 12), fg="#000000", bg="#00FF00", width=30)
ip_entry.pack(pady=5)
button_ip = tk.Button(search_frame, text="Search by IP", command=search_ip, fg="#0A0A0A", bg="#00FF00", font=("Courier", 12), width=20)
button_ip.pack(pady=5)

name_entry = tk.Entry(search_frame, font=("Courier", 12), fg="#000000", bg="#00FF00", width=30)
name_entry.pack(pady=5)
button_name = tk.Button(search_frame, text="Search by Name", command=search_name, fg="#0A0A0A", bg="#00FF00", font=("Courier", 12), width=20)
button_name.pack(pady=5)

number_entry = tk.Entry(search_frame, font=("Courier", 12), fg="#000000", bg="#00FF00", width=30)
number_entry.pack(pady=5)
button_number = tk.Button(search_frame, text="Search by Number", command=search_number, fg="#0A0A0A", bg="#00FF00", font=("Courier", 12), width=20)
button_number.pack(pady=5)



company_entry = tk.Entry(search_frame, font=("Courier", 12), fg="#000000", bg="#00FF00", width=30)
company_entry.pack(pady=5)
button_company = tk.Button(search_frame, text="Search by Company", command=search_company, fg="#0A0A0A", bg="#00FF00", font=("Courier", 12), width=20)
button_company.pack(pady=5)

# --- SECCIÓN DE CONFIGURACIÓN ---
settings_frame = tk.Frame(root, bg="#0A0A0A", padx=20, pady=20)

settings_label = tk.Label(settings_frame, text="Settings", fg="#00FFFF", bg="#0A0A0A", font=("Courier", 16, "bold"))
settings_label.pack(pady=10)

button_background_color = tk.Button(settings_frame, text="Change Background Color", command=change_background, fg="#00FF00", bg="#0A0A0A", font=("Courier", 14), width=25, pady=10)
button_background_color.pack(pady=10)

button_text_color = tk.Button(settings_frame, text="Change Text Color", command=change_text_color, fg="#00FF00", bg="#0A0A0A", font=("Courier", 14), width=25, pady=10)
button_text_color.pack(pady=10)

back_button = tk.Button(settings_frame, text="Back to Menu", command=back_to_menu, fg="#00FF00", bg="#0A0A0A", font=("Courier", 14), width=25, pady=10)
back_button.pack(pady=10)

# --- SECCIÓN DE MÁS HERRAMIENTAS --- 
more_tools_frame = tk.Frame(root, bg="#000000", padx=20, pady=20)  # Fondo negro

more_tools_label = tk.Label(more_tools_frame, text="More Tools", fg="#FFFFFF", bg="#000000", font=("Courier", 16, "bold"))  # Texto blanco
more_tools_label.pack(pady=10)

# Agregar un scrollbar
canvas = tk.Canvas(more_tools_frame, bg="#000000")  # Fondo negro
scrollbar = tk.Scrollbar(more_tools_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#000000")  # Fondo negro

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Lista de páginas recomendadas con descripciones breves
websites = [
    ("W3Schools", "Learn web development tutorials."),
    ("MDN Web Docs", "Comprehensive web tech docs."),
    ("Stack Overflow", "Platform for programming questions."),
    ("GitHub", "Version control repository hosting."),
    ("GeeksforGeeks", "Computer science and programming tutorials."),
    ("FreeCodeCamp", "Interactive web development learning."),
    ("Reddit - WebDev", "Web dev community discussions."),
    ("Python Docs", "Official Python documentation."),
    ("CSS-Tricks", "CSS tips, tricks, techniques."),
    ("CodePen", "Online front-end code editor."),
    ("JQuery", "Fast and small JavaScript library."),
    ("Codewars", "Coding challenges and games."),
    ("LeetCode", "Coding interview preparation platform."),
    ("HackerRank", "Practice coding skills through challenges."),
    ("Codecademy", "Interactive programming language learning."),
]

# Crear botones para abrir las páginas con descripciones
for name, description in websites:
    frame = tk.Frame(scrollable_frame, bg="#000000")  # Fondo negro
    button = tk.Button(frame, text=name, command=lambda name=name: open_browser(f"https://{name.lower().replace(' ', '')}.com"), fg="#00FF00", bg="#000000", font=("Courier", 12), width=30, pady=5)  # Texto verde, fondo negro
    button.pack(anchor="w", padx=5, pady=5)  # Alineado a la izquierda y con un pequeño padding
    description_label = tk.Label(frame, text=description, fg="#FFFFFF", bg="#000000", font=("Courier", 10))  # Texto blanco
    description_label.pack(anchor="w", padx=5, pady=5)  # Alineado a la izquierda
    frame.pack(pady=10, anchor="w")  # Asegura que el marco también se alinee a la izquierda

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

back_button_more_tools = tk.Button(more_tools_frame, text="Back to Menu", command=back_to_menu, fg="#00FF00", bg="#000000", font=("Courier", 14), width=25, pady=10)  # Texto verde, fondo negro
back_button_more_tools.pack(pady=10)


root.mainloop()
