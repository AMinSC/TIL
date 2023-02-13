#결측치 출력
def checkNaN(df):
    print("Missing Value List")
    for col in df.columns:
            if df[col].isnull().sum():
                print(f"{col} : {df[col].isnull().sum()} ")



#결측치 제거
def dropNaN(df):
    print("Pre-Processing...")
    for i in df.columns.to_list() :
        dpIdx = df[df[i].isnull()==True].index
        df.drop(index=dpIdx, inplace=True)
    print(f"{dpIdx} Columns Dropped.")    
    return df

