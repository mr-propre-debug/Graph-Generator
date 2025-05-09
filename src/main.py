from tkinter import Tk, Label, Button, StringVar, OptionMenu, Entry, filedialog
import graphiques as g
import csv
import sys

class GraphApp:
    def __init__(self, master):
        self.master = master
        master.title("Graph Generator")
        master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.graph_types = [
            "Graphique à barres",
            "Diagramme circulaire",
            "Graphique linéaire",
            "Nuage de points",
            "Histogramme",
            "Box plot",
            "Graphique de surface",
            "Barres empilées"
        ]

        self.selected_graph_type = StringVar(master)
        self.selected_graph_type.set(self.graph_types[0])  # Default value

        self.label = Label(master, text="Choisissez un type de graphique:")
        self.label.pack()

        self.dropdown = OptionMenu(master, self.selected_graph_type, *self.graph_types)
        self.dropdown.pack()

        self.file_label = Label(master, text="Nom du fichier CSV:")
        self.file_label.pack()

        self.file_entry = Entry(master)
        self.file_entry.pack()

        self.browse_button = Button(master, text="Parcourir", command=self.browse_file)
        self.browse_button.pack()

        self.generate_button = Button(master, text="Générer le graphique", command=self.generate_graph)
        self.generate_button.pack()

        self.quit_button = Button(master, text="Quitter", command=master.quit)
        self.quit_button.pack()
    
    def on_close(self):
        self.master.destroy()
        sys.exit()


    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.file_entry.delete(0, 'end')
        self.file_entry.insert(0, filename)

    def generate_graph(self):
        filename = self.file_entry.get()
        graph_type = self.selected_graph_type.get()

        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        graph_functions = {
            "Graphique à barres": g.create_bar_chart,
            "Diagramme circulaire": g.create_pie_chart,
            "Graphique linéaire": g.create_line_chart,
            "Nuage de points": g.create_scatter_plot,
            "Histogramme": g.create_histogram,
            "Box plot": g.create_box_plot,
            "Graphique de surface": g.create_area_chart,
            "Barres empilées": g.create_barres_empilees
        }

        graph_functions[graph_type](data, self.master)

if __name__ == "__main__":
    root = Tk()
    app = GraphApp(root)
    root.mainloop()