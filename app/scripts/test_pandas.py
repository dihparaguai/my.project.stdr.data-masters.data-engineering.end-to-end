import pandas as pd

def create_and_show_df(): # Function to test Pandas dependency usage inside Docker
    header = ['nome', 'idade']
    records = [
        ['diego', 28],
        ['rodrigo', 27]
    ]
    
    df = pd.DataFrame(records, columns=header)

    print(df)

create_and_show_df()