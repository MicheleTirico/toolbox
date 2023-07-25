import pandas as pd

def test_package(a): print ("handfiles: packages has been imported\nrun run from toolbox.handlefiles import tools")

def storeDataframe(logger,pathStore,df):
    logger.log(cl=None,method=None,message="Store dataframe in:{}".format(pathStore))
    df.to_csv(pathStore, sep=';')


def dropValColumns(columns,listValToDrop):
    for i in listValToDrop:        columns.pop(columns.index(i))
    return columns

def mergeDfSns(df_mat,df_sym,mat_col,sym_col,quantile,resetIndex,nameColumn,minQuant):
    df1=pd.DataFrame(df_mat[["time",mat_col]])
    df2=pd.DataFrame(df_sym[["p_range",sym_col]])
    if quantile != None:
        if minQuant:
            newQuantile=min(df1[mat_col].quantile(quantile),df2[sym_col].quantile(quantile))
            quantile=newQuantile
        df1=df1[df1[mat_col]<df1[mat_col].quantile(quantile)]
        df2=df2[df2[sym_col]<df2[sym_col].quantile(quantile)]
    df1["model"]="MATSim"
    df1=df1.rename(columns={mat_col:nameColumn,"time":"p_range"})
    df2["model"]="Symuvia"
    df2=df2.rename(columns={sym_col:nameColumn})
    df3=pd.concat([df1,df2])
    if resetIndex:    df3=df3.reset_index()
    return df3

def saveFig(fig,logger, pathSave):
    logger.log(cl=None,method=None,message="store figure at:{}".format(pathSave))
    fig.savefig(pathSave)
