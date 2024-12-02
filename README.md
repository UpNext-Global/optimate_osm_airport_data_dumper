<br />
<div align="center">
  <h3 align="center">Optimate OSM Airport Data Dumper</h3>

  <p align="center">
    Extract airport data from OSM (OpenStreeMaps) in the GEOJSON format.
    <br />
    <a href="https://github.com/UpNext-Global/optimate_osm_airport_data_dumper/issues">Report Bug</a>
    ·
    <a href="https://github.com/UpNext-Global/optimate_osm_airport_data_dumper/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p>This project allows the retrieval of georeferenced aiport data from OSM.</p>
<p>The data is provided in the GEOJSON format and can e used for taxiway/runway segmentation and overall routing purposes.</p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

#### Python
##### Windows
1. Download and install Python3.x from <https://www.python.org/downloads/>.
##### Unix
1. Install Python 3.x
  ```sh
  sudo apt-get install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt-get update
  sudo apt-get install python3.11
  sudo apt-get install python3.11-venv
  sudo apt-get install python3-pip
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Development
### Checkout
1. Clone and checkout
   ```sh
   git clone https://github.com/UpNext-Global/optimate_osm_airport_data_dumper
   ./pull.sh
   ```

### Setup Python development environment
#### Linux
1. Setup a virtual environment
   ```sh
   cd project
   python<version> -m venv <virtual-environment-name>
   source <virtual-environment-name>/bin/activate
   ```
2. Install the dependencies using pip
   ```sh
   pip install -r requirements.txt
   ```
#### Windows
1. Setup a virtual environment
   ```sh
   cd project
   python<version> -m venv <virtual-environment-name>
   ./<virtual-environment-name>/Scripts/activate
   ```
2. Install the dependencies using pip
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
1. To install the Python module using pip run the following command:
   ```sh
   cd optimate_osm_airport_data_dumper
   python -m pip install .
   ```
2. To execute the application we need to supply at least an output file path.
   ```sh
   optimate-osm-airport-data-dumper -o ~/airport.json
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Retrieve all edges and nodes from OSM given the aiport ICAO code
- [x] Dump the nodes and edges in the GEOJSON format

See the [open issues](https://github.com/UpNext-Global/optimate_osm_airport_data_dumper/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Marco Várzea - [marco.varzea@criticalsoftware.com](marco.varzea@criticalsoftware.com)

Project Link: [https://github.com/UpNext-Global/optimate_osm_airport_data_dumper](https://github.com/UpNext-Global/optimate_osm_airport_data_dumper)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org

