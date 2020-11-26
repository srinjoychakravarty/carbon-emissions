# masked-array

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

#### Solved Bug

> **Tip:** To simulate a command run of this repo simply copy paste the .nc4 data file into the same folder as this repo

    
### IDE 

* Python 3 Code built and run using Visual Studio Code 

### Prerequisites and Running on Discovery Cluster

1. Download a Miniconda 3 environment
    ```sh
    $ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    ```
    
2. Make the downloaded file executable
    ```sh
    $ chmod +x Miniconda3-latest-Linux-x86_64.sh
    ```
    
3. Install using the script
    ```sh
    $ bash Miniconda3-latest-Linux-x86_64.sh
    ```
    
4. Agree to everything
    ```sh
    Agree to license agreement >> yes
    ```

5. Choose any path to download to
    ```sh
    Directory to install >> /path/to/my/conda
    ```
    
6. Change into the same directory that was chosen above 
    ```sh
    $ cd /path/to/my/conda/bin
    ```
    
7. Activate the miniconda install
    ```sh
    $ source activate
    ```
    
8. Update conda (optional) 
    ```sh
    $ conda update conda
    ```
    
9.  Proceed as required
    ```sh
    $ Proceed? >> yes
    ```
    
10. Clone this project directory
    ```sh
    $ git clone https://github.com/srinjoychakravarty/masked-array.git
    ```
    
11. Copy paste the .nc4 dataset into the repo
    ```sh
    $ mv /location/to/my/dataset/Vulcan_v3_US_annual_1km_total_mn.nc4 masked_array/
    ```
    
12. Recreate the customized environment required to run all the code in this repo:
    ```sh
    $ conda env create -f environment.yaml
    ```
**Tip:** Make sure to install a miniconda environment and activate it before running step 4

13. Activate your imported conda environment:
    ```sh
    $ bash run.sh
    ```

License
----

Northeastern University

_Srinjoy Chakravarty_
