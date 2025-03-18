# Prediction of DAAO Activity Categories
 
Code for the paper "Overcoming Antagonistic Epistasis in Enzyme Evolution through Multidimensional Feature Analysis: Rational Engineering of ReDAAO for Enhanced D-Phosphinothricin in Catalysis".
 
The script 'run_prediction.py' was used to run the prediction in papers for the activity of mutate protein.

## Installation

You can installing the dependency through folwing command:

```
pip3 install -r requirements.txt
```

## Example Usage

```
python run_prediction.py --input input_example.csv --output prediction_result.tsv
```

## Input Structure

Input Files Structure Should be Like:

```
Feature
-------
  ······
---kkkk
```


## Data Availablity

The raw data from the analyses in the paper can be found here: https://drive.google.com/drive/folders/1UJDOld0qZHSBSb1vNGik5AeufPUpS682?usp=sharing

The folder contains the following files about the activity prediction result used in paper:

* `prediction_result.csv` -- Results with the mutation prediction results listed in the Paper.
