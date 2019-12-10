# Machine Learning Solvers for the Directory of Useful Decoys - Enhanced (DUD-E) 

## Motivation
This project assess the performance of various machine learning algorithms for the Directory of Useful Decoys - Enhanced (DUD-E).

The performance of the various algorithms is assessed by means of calculating the training scores, the log-loss, the confusion matrix, the f1-score, by plotting the ROC and computing the AUROC.

This code was created as an assignment for the _Data Science_ module, at the _EPSRC CDT in Sustainable Approached to Biomedical Sciences: Responsible and Reproducible Research - SABS R3_

## Installation
In order to install the packaged, the user will require the presence of Python3 and the [pip3](https://pip.pypa.io/en/stable/) installer. 

For installation on Linux or OSX, use the following commands. This will create an environment and automatically install all the requirements.

```bash
python3 -m venv env
source env/bin/activate
pip install -e .
```

## Usage
In order to run the solver, type the following commands int the activated python environment. 

```python
jupyter notebook
```

Following this, the user should open the *_MAIN.ipynb_* and run the commands. 

For running commands for specific DUD-E Targets, run the *_MAIN->target name>.ipynb_* files.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause) © [Jakke Neiro](https://github.com/jakke-neiro), [Andrei Roibu](https://github.com/AndreiRoibu)


## Credits
The team would like to express their gratitude to [Tom Hadfield](http://users.ox.ac.uk/~exet4511/) for his help and support during the development of this code.

