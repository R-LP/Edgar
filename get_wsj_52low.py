#Welcome to Alpha Vantage! Your API key is: 6T97AARFPOGKEG70. Please record this API key for future access to Alpha Vantage.
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen("http://www.wsj.com/mdc/public/page/2_3021-newhinyse-newhighs.html").read()
dfs = pd.read_html(sauce)

df = dfs[1]
bool_series = df[0].str.contains("New 52-Week Lows")
low_index = df.index[bool_series].tolist()[0]
df_low = df[low_index:].reset_index(drop=True)
columns = ['company_name', '52_wkLow', 'price', 'chg', 'perChg', 'volume']
df_low.columns = columns
df_low = df_low[2:].reset_index(drop=True)
df_low['ticker'] = df_low['company_name'].str.extract('\(([^\.]*)\)', expand=False)
new_order = [0, 6, 1, 2, 3, 4, 5]
df_low = df_low[df_low.columns[new_order]]



