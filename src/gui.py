from tkinter import Tk, Label, Button, StringVar, OptionMenu, filedialog
import graphiques as g
import csv

def generate_graph():
    graph_type = graph_type_var.get()
    filename = filename_var.get()
    
    if filename:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        
        if graph_type == "Graphique à barres":
            g.create_bar_chart(data)
        elif graph_type == "Diagramme circulaire":
            g.create_pie_chart(data)
        elif graph_type == "Graphique linéaire":
            g.create_line_chart(data)
        elif graph_type == "Nuage de points":
            g.create_scatter_plot(data)
        elif graph_type == "Histogramme":
            g.create_histogram(data)
        elif graph_type == "Box plot":
            g.create_box_plot(data)
        elif graph_type == "Graphique de surface":
            g.create_area_chart(data)
        elif graph_type == "Barres empilées":
            g.create_barres_empilees(data)

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    filename_var.set(filename)

root = Tk()
root.title("Graphique Generator")

graph_type_var = StringVar(root)
graph_type_var.set("Graphique à barres")  # Default value

filename_var = StringVar(root)

Label(root, text="Choisissez un type de graphique :").pack()
OptionMenu(root, graph_type_var, "Graphique à barres", "Diagramme circulaire", "Graphique linéaire", 
           "Nuage de points", "Histogramme", "Box plot", "Graphique de surface", "Barres empilées").pack()

Label(root, text="Nom du fichier CSV :").pack()
Entry(root, textvariable=filename_var).pack()

Button(root, text="Parcourir", command=browse_file).pack()
Button(root, text="Générer le graphique", command=generate_graph).pack()

root.mainloop()