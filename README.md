# Electric Vehicles Data Visualization Project

This project provides a set of tools for visualizing CSV data through various types of graphs. Users can generate visual representations of data from CSV files using both a command-line interface and a graphical user interface.

## Project Structure

```
Electric_vehicles
├── src
│   ├── main.py          # Entry point for the command-line interface
│   ├── graphiques.py    # Contains functions for generating different types of graphs
│   └── gui.py           # Implements the graphical user interface for the application
├── requirements.txt      # Lists the dependencies required for the project
└── README.md             # Documentation for the project
```

## Features

- **Graph Types**: The application supports the following types of graphs:
  - Bar Charts
  - Pie Charts
  - Line Charts
  - Scatter Plots
  - Histograms
  - Box Plots
  - Area Charts
  - Stacked Bar Charts

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Electric_vehicles
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface

To run the application using the command-line interface, execute the following command:

```
python src/main.py
```

Follow the prompts to select a graph type and provide the name of the CSV file containing the data.

### Graphical User Interface

The graphical user interface will be implemented in `src/gui.py`. Once completed, it will allow users to select graph types and input CSV file names through a visual interface.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.