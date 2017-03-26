import pandas as pd
states = {'OH': 'Ohio', 'KY': 'Kentucky',
          'AS': 'American Samoa',
          'NV': 'Nevada', 'WY': 'Wyoming',
          'NA': 'National', 'AL': 'Alabama',
          'MD': 'Maryland', 'AK': 'Alaska',
          'UT': 'Utah', 'OR': 'Oregon',
          'MT': 'Montana', 'IL': 'Illinois',
          'TN': 'Tennessee', 'DC': 'District of Columbia',
          'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas',
          'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii',
          'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana',
          'NJ': 'New Jersey', 'AZ': 'Arizona',
          'GU': 'Guam', 'MS': 'Mississippi',
          'PR': 'Puerto Rico', 'NC': 'North Carolina',
          'TX': 'Texas', 'SD': 'South Dakota',
          'MP': 'Northern Mariana Islands',
          'IA': 'Iowa', 'MO': 'Missouri',
          'CT': 'Connecticut', 'WV': 'West Virginia',
          'SC': 'South Carolina', 'LA': 'Louisiana',
          'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska',
          'OK': 'Oklahoma', 'FL': 'Florida',
          'CA': 'California', 'CO': 'Colorado',
          'PA': 'Pennsylvania', 'DE': 'Delaware',
          'NM': 'New Mexico', 'RI': 'Rhode Island',
          'MN': 'Minnesota', 'VI': 'Virgin Islands',
          'NH': 'New Hampshire', 'MA': 'Massachusetts',
          'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def findFile(search, state='', binsize=400):
    """
    find file name for the area "search" and
    state "state", records outside US have state=NaN
    """
    columnsToKeep = [
        'STATEL', 'NAME', 'FILE', 'LATITUDE', 'LONGITUDE', 'ELEVATION']

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    # convert abbr. to full state name
    df['STATEL'] = df['STATE'].map(states)

    mask = (df['NAME'].str.contains(search.upper()))

    if len(state.strip()) == 2:
        mask = mask & (df['STATE'] == state.upper().strip())
    elif len(state.strip()) > 2:
        mask = mask & (df['STATEL'] == state.title().strip())
    elif len(state.strip()) == 0:
        mask = mask & (df['STATE'].isnull())

    if len(mask) > 0:
        res = df[mask]
        res['FILE'] = res['hash'].apply(
            lambda x: 'data/C2A2_data/BinnedCsvs_d{}/{}.csv'.format(binsize,x))
        res['STATEL'] = res['STATEL'].str.title()
        if len(state.strip()) >= 2:
            res = res[~res['STATE'].isnull()]
        return res[columnsToKeep]