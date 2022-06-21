from custfunc import reduce_ram_usage
import pandas as pd
import gc

# Drop Outlier

def dropOutlier (df):
    #입력받은 인덱스를 제거하는 함수입니다(라인 축약)
    def dropIdx(df, idx) :
        df.drop(index=idx, inplace=True)
        dropIdx.dpIdx_sum +=len(idx)
        return df

    dropIdx.dpIdx_sum = 0

    print("Pre-Processing...")
    for i in df.columns.to_list() :
        df.drop(index=df[df[i].isnull()==True].index, inplace=True)
        
    print("Droping Outliers...")
    vip_features = ["assists","boosts","DBNOs","heals","kills","killStreaks","walkDistance", "revives", "roadKills", "vehicleDestroys"]
    
    #한 그룹 내에 너무 많은 인원이 있는 경우 (이하 제거).
    group = df.groupby('groupId').count()
    df = dropIdx(df, df[df.groupId.isin(group[group["Id"]>group["Id"].quantile(0.9999)].index)==True].index) 
    
    #수치형 데이터에서 0.1%의 극값
    for col in (vip_features + ["damageDealt","longestKill", "rideDistance", "swimDistance","weaponsAcquired", "matchDuration"]):
        df = dropIdx(df, df[df[col]>df[col].quantile(0.99999)].index)
    
    #걸은 거리보다 많은 킬/아이템 사용 등이 있는 경우
    for col in vip_features:
        df = dropIdx(df, df[df["walkDistance"]<df[col]].index)
    
    #한 게임의 플레이어보다 많은 처치를 기록한 경우
    df = dropIdx(df, df[df.groupby('matchId')['kills'].transform('max')  > df.groupby('matchId')['Id'].transform('count')  ].index)
    #차를 타지 않고 로드킬을 올린 경우
    df = dropIdx(df, df[(df['rideDistance']==0) & (df['roadKills']>0)  ].index)

    #한 서버에 한 팀만 있는 경우, 최대 등수를 조정
    df.loc[(df.maxPlace>1)&(df.numGroups==1), "maxPlace"] = 1

    print(f"{dropIdx.dpIdx_sum} Columns has deleted!") 

    del vip_features, group      
    gc.collect()
    
    return df


# Encode Match
def encodeMatch (df):
    print("Encoding matchType...")

    mapper = lambda x: 'normal' if ('normal' in x) or ('crash' in x)or ('flare' in x)else x 
    df["matchType"]=df["matchType"].apply(mapper)

    mapper = lambda x: 'solo' if ('solo' in x) else 'duo' if ('duo' in x) else 'normal' if ('normal' in x) else 'squad' 
    df["matchType"]=df["matchType"].apply(mapper)

    df = pd.concat([df,pd.get_dummies(df["matchType"])], axis=1)

    del mapper
    return df


# Make Cols
def makeCols (df) :
    print("Making columns...")
    df["killPlace"] = df.groupby("matchId")["kills"].transform('rank', ascending=False)
    #data leakage 없는 killPlace data

    stat_feature = ["assists",
                    "boosts",
                    "DBNOs",
                    "heals",
                    "kills",
                    "killStreaks",
                    "walkDistance", 
                    "revives", 
                    "roadKills", 
                    "vehicleDestroys",
                    "damageDealt",
                    "longestKill", 
                    "rideDistance", 
                    "swimDistance",
                    "weaponsAcquired"]
    stat_list = ["max","mean","median","min"]
    for col in stat_feature :
        for stat in stat_list:
            df = pd.concat([df,df.groupby("groupId")[col].transform(stat).rename(f"{col}_{stat}")], axis=1) 
            df = pd.concat([df,df.groupby("matchId")[f"{col}_{stat}"].transform('rank', ascending=False).rename(f"{col}_{stat}Place")], axis=1)
    #group별 column stats, match별 group stats 순위

    print(len(stat_feature)*len(stat_list)+1, f"columns Made! Now {len(df.columns)} column in DF.")
    df = reduce_ram_usage(df)
    return df


