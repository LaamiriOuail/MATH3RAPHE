# MATH3RAPHE: A Desktop Application for Graph Theory Algorithms and Real-Time Graph Visualization

*MATH3RAPHE* is a desktop application meticulously designed to facilitate the manipulation of algorithms in graph theory, offering real-time graph visualization capabilities. This powerful tool not only enables users to interact with a variety of graph algorithms but also provides an immersive experience through dynamic, on-the-fly graph visualization.

## Key Features:

### 1.Algorithm Manipulation:

- **MATH3RAPHE** empowers users to work seamlessly with a diverse set of algorithms derived from graph theory. Whether it's traversing paths, analyzing connectivity, or extracting crucial insights from graphs, the application provides an intuitive interface for algorithmic exploration.

### 2.Real-Time Graph Visualization:

- Experience the beauty of graph theory in action with real-time visualization. As algorithms unfold, watch the dynamic changes in the graphical representation of graphs, offering a visual aid that enhances understanding and insight into complex structures.

### 3.PDF Report Generation:

- **MATH3RAPHE** goes beyond real-time visualization by offering users the ability to generate comprehensive PDF reports. These reports contain valuable information, statistics, and visual representations of graphs, making it easy to document and share findings.

### 4.Graph Information and Photo Compilation:

- The application allows users to download PDF files containing not only algorithmic details but also a compilation of essential information and vivid photos related to the graphs under consideration. This feature enhances the documentation process and provides a holistic view of the graphs being analyzed.

## Usage Scenarios:

- **Educational Tool**: Ideal for students and educators exploring the intricacies of graph theory.
- **Research Companion**: A valuable asset for researchers delving into graph-related studies and analyses.
- **Practical Application**: Engineers and professionals can leverage *MATH3RAPHE* to solve real-world problems involving graph structures.


## Project Folder Structure

The structure of the project is organized to enhance clarity and maintainability. Here is an overview of the main folders:

### `controller`
- The `controller` folder contains the main controller of the application, referred to as the "orchestra." This component orchestrates the flow of the application, managing interactions between different parts.

### `public`
- The `public` folder is designated for static files such as images, audio files, or any other resources that do not require dynamic processing. This separation helps keep the project organized.

### `model`
- In the `model` folder, you will find the SQLite database file (`app.db`). This file stores and manages the application's data.

### `docs`
- The `docs` folder is generated by Sphinx and contains the documentation for the project. Sphinx provides a powerful tool for creating well-organized and easily navigable documentation.

### `package`
- The `package` folder is subdivided into subfolders containing classes related to various aspects of the application:
  - `UI`: Contains classes related to the user interface.
  - `DB`: Contains classes responsible for interacting with the database.
  - `PDF`: Contains classes related to generating PDF reports.
  - `Graphe`: Contains classes related to graphe operations 

### `view`
- The `view` folder houses Python files, each containing functions following the principle of returning components, akin to the principles of React.js. This separation of concerns facilitates a clean and modular structure for building the application's user interface.

This folder structure is designed to promote a clear separation of concerns, making it easier to navigate and maintain the codebase. Feel free to explore each folder to gain insights into the specific functionalities and components of the application.

## Libraries Used

This project leverages several powerful libraries to achieve its functionalities. Below is a list of the key libraries along with their respective versions:

### 1. PyQt5 (version 5.15.5)
- PyQt5 is a comprehensive set of Python bindings for Qt libraries, providing tools for creating desktop applications with a rich graphical user interface.

### 2. pymongo (version 3.12.0)
- pymongo is a Python driver for MongoDB, allowing seamless integration with MongoDB databases and facilitating efficient interaction with MongoDB data.

### 3. networkx (version 2.8.3)
- networkx is a powerful library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks or graphs.

### 4. pygame (version 2.0.2)
- pygame is a cross-platform set of Python modules designed for writing video games. It is also used here for handling multimedia elements such as audio and images.

### 5. sphinx (version 4.4.2)
- sphinx is a documentation generation tool that enables the creation of high-quality documentation for Python projects. It is used to generate organized and easily navigable documentation for this project.

### 6. fpdf (version 1.7.2)
- fpdf is a Python library for creating PDF documents. In this project, it is utilized for generating comprehensive PDF reports containing information and visual representations of graphs.

### 7. matplotlib (version 3.4.3)
- matplotlib is a popular 2D plotting library for Python. It is employed here for creating visualizations and graphs as part of the project's features.
### 8. sqlite3
- sqlite3 is a lightweight and self-contained relational database engine. It is used in this project for managing the SQLite database (`app.db`), which stores and manages the application's data.

These libraries play a crucial role in enhancing the functionality, aesthetics, and documentation aspects of the application. Each library is chosen for its specific strengths and contributions to the overall success of the project.


## Get Started:

### 1.Clone from github : 
```bash
# clone the repository in your local pc from github
$ git clone https://github.com/LaamiriOuail/MATH3RAPHE
# go to MATH3RAPHE folder :
$ cd MATH3RAPHE/
```

### 2.Install requirements : 
```bash
# install python requirements for running the project
$ pip install -r requerements.txt
```

### 3.Run the application : 
```bash
# install python requirements for running the project
$ python controller/manager.py
```



## License

This project is licensed under the terms of the GNU General Public License v3.0 

### GNU General Public License (GPL)

The GNU General Public License is a free, copyleft license for software and other kinds of works. The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users.



## Stay in touch :
- Author - [Ouail Laamiri](https://www.linkedin.com/in/ouaillaamiri/) 
- Documentation - [Sphinix](https://laamiriouail.github.io/MATH3RAPHE/)