import pandas as pd 

def export_to_csv(data, output_file):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index = False)