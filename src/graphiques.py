"""
graphiques.py

Ce module fournit différentes fonctions pour générer des graphiques à partir de données CSV
en utilisant matplotlib. Les types de graphiques disponibles incluent :
- graphique à barres
- graphique circulaire (camembert)
- graphique linéaire
- histogramme
- nuage de points (scatter plot)
- box plot
- graphique de surface (area chart)
- graphique à barres empilées

Chaque fonction demande à l'utilisateur des informations sur les axes et le titre du graphique,
puis affiche le graphique correspondant.
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.cm as cm
from tkinter import simpledialog

# ...existing code...
def get_inputs_bar_chart(parent):
    title = simpledialog.askstring("Titre", "Titre du graphique :", parent=parent)
    x_label = simpledialog.askstring("Axe X", "Label de l'axe X :", parent=parent)
    y_label = simpledialog.askstring("Axe Y", "Label de l'axe Y :", parent=parent)
    parent.destroy()
    return title, x_label, y_label

def create_bar_chart(data, parent):
    keys = list(data[0].keys())
    x_key = keys[0]
    y_key = keys[1]
    title, x_label, y_label = get_inputs_bar_chart(parent)
    x = [item[x_key] for item in data]
    y = [int(item[y_key]) for item in data]
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='skyblue', width=0.4)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def get_inputs_pie_chart(data, parent):
    key = simpledialog.askstring("Clé", f"Clé pour les labels (parmi {list(data[0].keys())}) :", parent=parent)
    title = simpledialog.askstring("Titre", "Titre du graphique :", parent=parent)
    parent.destroy()
    return key, title

def create_pie_chart(data, parent):
    key, title = get_inputs_pie_chart(data, parent=parent)
    labels = [item[key] for item in data]
    sizes = [int(item['count']) for item in data]
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()

def get_inputs_line_chart(parent):
    title = simpledialog.askstring("Titre", "Titre du graphique :", parent=parent)
    x_label = simpledialog.askstring("Axe X", "Label de l'axe X :", parent=parent)
    y_label = simpledialog.askstring("Axe Y", "Label de l'axe Y :", parent=parent)
    parent.destroy()
    return title, x_label, y_label

def create_line_chart(data, parent):
    keys = list(data[0].keys())
    x_key = keys[0]
    y_key = keys[1]

    title, x_label, y_label = get_inputs_line_chart(parent=parent)
    x = [item[x_key] for item in data]
    y = [int(item[y_key]) for item in data]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='x', color='skyblue')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def get_inputs_histogram(parent):
 
    key = simpledialog.askstring("Clé", "Clé numérique à représenter :", parent=parent)
    title = simpledialog.askstring("Titre", "Titre du graphique :", parent=parent)
    x_label = simpledialog.askstring("Axe X", "Label de l'axe X :", parent=parent)
    y_label = simpledialog.askstring("Axe Y", "Label de l'axe Y :", parent=parent)
    parent.destroy()
    return key, title, x_label, y_label

def create_histogram(data, parent):
    key, title, x_label, y_label = get_inputs_histogram(parent=parent)
    values = [int(item[key]) for item in data]

    plt.figure(figsize=(10, 6))
    plt.hist(values, bins=20, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.tight_layout()
    plt.show()

def get_inputs_scatter_plot(parent):
    title = simpledialog.askstring("Titre", "Titre du graphique :", parent=parent)
    x_label = simpledialog.askstring("Axe X", "Label de l'axe X :", parent=parent)
    y_label = simpledialog.askstring("Axe Y", "Label de l'axe Y :", parent=parent)
    parent.destroy()
    return title, x_label, y_label

def create_scatter_plot(data, parent):
    keys = list(data[0].keys())
    x_key = keys[0]
    y_key = keys[1]
    if len(keys) > 2:
        texte_key = keys[2]
    
    title, x_label, y_label = get_inputs_scatter_plot(parent=parent)
    x = [item[x_key] for item in data]
    y = [float(item[y_key]) for item in data]

    texte = [item[texte_key] for item in data] if len(keys) > 2 else None

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='skyblue', marker='x')
    if texte:
        for xi, yi, item in zip(x, y, texte):
            plt.text(xi, yi, str(item), fontsize=8, ha='right', va='bottom')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def get_inputs_box_plot(parent):

    key = simpledialog.askstring("Clé", "Clé numérique à représenter :", parent=parent)
    title = simpledialog.askstring("Titre", "Titre du graphique :",parent=parent)
    x_label = simpledialog.askstring("Axe X", "Label de l'axe X :", parent=parent)
    y_label = simpledialog.askstring("Axe Y", "Label de l'axe Y :", parent=parent)
    parent.destroy()
    return key, title, x_label, y_label

def create_box_plot(data, parent):
    key, title, x_label, y_label = get_inputs_box_plot(parent=parent)
    values = [int(item[key]) for item in data]

    plt.figure(figsize=(10, 6))
    plt.boxplot(values, patch_artist=True, boxprops=dict(facecolor='skyblue'))
    plt.title(title)
    plt.ylabel(y_label)
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.xticks([1], [x_label])
    plt.tight_layout()
    plt.show()

def get_inputs_area_chart(parent):

    title = simpledialog.askstring("Titre", "Titre du graphique :", parent=parent)
    x_label = simpledialog.askstring("Axe X", "Label de l'axe X :", parent=parent)
    y_label = simpledialog.askstring("Axe Y", "Label de l'axe Y :",parent=parent)
    parent.destroy()
    return title, x_label, y_label

def create_area_chart(data, parent):
    keys = list(data[0].keys())
    x_key = keys[0]
    y_key = keys[1]
    title, x_label, y_label = get_inputs_area_chart(parent=parent)
    x = [item[x_key] for item in data]
    y = [int(item[y_key]) for item in data]

    plt.figure(figsize=(10, 6))
    plt.fill_between(x, y, color='skyblue', alpha=0.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def get_inputs_barres_empilees(parent):
    title = simpledialog.askstring("Titre", "Titre du graphique :", parent=parent)
    x_label = simpledialog.askstring("Axe X", "Label de l'axe X :", parent=parent)
    y_label = simpledialog.askstring("Axe Y", "Label de l'axe Y :", parent=parent)
    parent.destroy()
    return title, x_label, y_label

def create_barres_empilees(data, parent):
    data_keys = list(data[0].keys())
    x_key = data_keys[0]
    y_keys = data_keys[1:]
    title, x_label, y_label = get_inputs_barres_empilees(parent=parent)
    x = [item[x_key] for item in data]
    bottom = [0.0] * len(data)

    plt.figure(figsize=(14, 6))

    # Génère une couleur différente pour chaque barre empilée
    
    colors = cm.get_cmap('tab20', len(y_keys))

    for idx, y_key in enumerate(y_keys):
        y_values = [float(item[y_key]) for item in data]
        plt.bar(x, y_values, bottom=bottom, label=y_key, color=colors(idx))
        bottom = [i + j for i, j in zip(bottom, y_values)]

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.tight_layout()
    plt.subplots_adjust(right=0.75)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()