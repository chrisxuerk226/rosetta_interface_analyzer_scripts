def get_energy_table(df) : 
    column_name = df['SEQUENCE: '].loc[0].split()[1:] 
    data = df['SEQUENCE: '].loc[1].split()[1:] 
    energy_table = pd.DataFrame(columns=column_name, index=['value'])  
    for i in range(len(column_name)) : 
        energy_table[column_name[i]] = data[i]  
    return energy_table   
