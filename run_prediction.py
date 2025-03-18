import argparse
import joblib
import numpy as np

def Prameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input",type=str, help="input predict file")
    parser.add_argument("-o", "--output",type=str, help="set output filename")
    args = parser.parse_args()
    return args.input,args.output

def ReadInput(filename):
    print('\n--------------START RUN PREDICTION---------------\n')
    CHAR_TO_ONEHOT = {'-': [1, 0, 0],'k': [0, 1, 0],  'r': [0, 0, 1]}
    features,targets=[],[]
    print('Fetching data···\n')
    with open(filename,encoding='utf-8') as fi:
        next(fi).strip()
        for line in fi:
            line=line.strip()
            if not line:
                continue
            sequence_part= line.strip().split('\n')[0]
            feature_vector = []
            targets.append(sequence_part)
            for char in sequence_part:
                if char not in CHAR_TO_ONEHOT:
                    feature_vector.extend(CHAR_TO_ONEHOT['-'])
                else:
                    feature_vector.extend(CHAR_TO_ONEHOT[char])
            features.append(feature_vector)
    return features,targets

def Predict(data,output):
    print("Start Prediction!!!\n")
    CHAR_TO_FEATURE = {0: 'Low',1: 'Medium',  2: 'High'}
    rf_loaded = joblib.load("random_forest.pkl")
    X_name,y_new_pred=np.ravel(data[0]),np.ravel(rf_loaded.predict(data[1]))
    y_new_pred = [CHAR_TO_FEATURE[int(i)] for i in np.ravel(y_new_pred)]
    print("Generating Output！！！\n")
    with open(output,'w') as file:
        file.write('Feature\tOutput\n')
        for (Prediction_name,Prediction_result) in zip(X_name,y_new_pred):
            file.write("%s\t%s\n" % (Prediction_name,Prediction_result))
    print('--------------RUN OVER---------------')

def main():
    Data_Input, Output_filename=Prameters()
    Feature_Coded, Feature_name = ReadInput(Data_Input)
    Total_Data=[Feature_name,Feature_Coded]
    Predict(Total_Data,Output_filename)

if __name__=='__main__':
    main()
    
    


