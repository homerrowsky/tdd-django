from selenium import webdriver

browser = webdriver.Firefox()

#Usuario ha escuchado sobre una nueva página con una app de lista de tareas.
# Usuario va a la url de esta página a checarla
browser.get('http://localhost:8000')

# Usuario nota que el título de la página y el encabezado dice 'to-do'
assert 'To-Do' in browser.title

# Se le invita a ingresar una nueva tarea

# Escribe 'comprar plumas de tzenzontle' en una caja de texto

# Cuando presiona Enter, la página se actualiza, y ahora la página enlista
# '1: Comprar plumas de tzenzontle' como un ítem de lista de tareas

# La caja de texto permanece en la página para agregar otra tarea
# Usuario ingresa 'usar plumas para penacho lujoso'

# De nuevo la página se actualiza y ahora muestra ambas tareas

# Usuario se pregunta si el sitio recordará su lista. Se da cuenta que el
# sitio ha generado un URL única -- hay un texto explicativo para tal efecto

# Usuario visita la URL - la lista todavía permanece allí

# El usuario, satisfecho, se va a ver videos en youtube

browser.quit()
