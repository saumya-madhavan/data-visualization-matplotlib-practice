# --------------
import pandas as pd 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# Load the dataset and create column `year` which stores the year in which match was played
df = pd.read_csv(path)
df.shape
df['year']= df.date.apply(lambda x:x[:4])
print (df[['date','year']].head())
# Plot the wins gained by teams across all seasons
print(df.groupby(['winner'])['match_code'].nunique())
t1=df.groupby(['winner'])['match_code'].nunique()
t1.sort_values(inplace=True)
t1.plot(kind='barh',title='Team wins across all Seasons',figsize=(15,7))
plt.xlabel('Number of wins')
plt.ylabel('Winner')

# Plot Number of matches played by each team through all seasons
team_1 = df.groupby(['team1'])['match_code'].nunique()
team_2 = df.groupby(['team2'])['match_code'].nunique()
###print (team_1)
###print (team_2)
team_3 = team_1 + team_2
##print (team_3)
plt.figure(figsize=(15,7))
team_3.sort_values(inplace=True)
team_3.plot(kind='barh',title='No. of Matches played by each team')
plt.xlabel('Number of Matches')
plt.ylabel('Teams')

# Performance of top bowlers over seasons
print('*'*30)
print (df['wicket_kind'].unique())
s1=df.loc[~(df.wicket_kind.isin(['run out','obstructing the field','retired hurt'])),:]
s2=s1.loc[s1.player_out.notnull(),:].reset_index(drop=True)

s3=s2['bowler'].value_counts()
s3.sort_values(inplace=True,ascending=False)
plt.figure(figsize=(15,7))
s3.head(10).plot(kind='barh',title='No. of Wickets taken by each bowler')
plt.xlabel('Number of Wickets')
plt.ylabel('Bowlers')
##print('*'*30)
###s3=s1.loc[s1.player_out.notnull(),:].reset_index(drop=True)
###print(s3[['match_code','bowler','wicket_kind']].head())
###s4=s3['bowler'].value_counts()
###s4.sort_values(inplace=True, ascending=False)
###print(s4)
###plt.figure(figsize=(15,7))
###s4.head(10).plot(kind='barh',colormap='Accent')

# How did the different pitches behave? What was the average score for each stadium?
##s1=df['wicket_kind'].value_counts()
##print (s1)
##fig,ax =plt.subplots(1,2,figsize=(15,17))
##s1.plot(kind='bar',ax=ax[0])
##explst=[0.03,0,0,0,0,0,0,0,0]
##s1.plot(kind='pie',ax=ax[1],autopct='%1.1f%%',explode=explst)
##ax[0].title.set_text('First plot')
##ax[1].legend(labels=s1.index,bbox_to_anchor=(1,1))
f1=df.groupby(['venue','inning','match_code'])['total'].sum()
f2=f1.reset_index()
###print(f2.head())
f3=f2.groupby(['venue','inning'])['total'].mean().reset_index()
###print(f3.head())
plt.figure(figsize=(15,7))
inn1=f3.loc[f3.inning==1,:]
inn2=f3.loc[f3.inning==2,:]
plt.plot(inn1['venue'],inn1['total'],'r',marker='o',label='Innings 1')
plt.plot(inn2['venue'],inn2['total'],'b',marker='o',label='Innings 2')
plt.xticks(rotation=90)
plt.xlabel('Venue')
plt.ylabel('Average Runs')
plt.legend(fontsize=10)

# Types of Dismissal and how often they occur
print(df['wicket_kind'].value_counts())
g1=df['wicket_kind'].value_counts()
fig,ax=plt.subplots(1,2,figsize=(15,7))
g1.plot(kind='bar',ax=ax[0])
explist=[0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03]
g1.plot(kind='pie',ax=ax[1],autopct='%1.1f%%',explode=explist)
ax[0].title.set_text('Bar Chart')
ax[1].title.set_text('Pie Chart')

# Plot no. of boundaries across IPL seasons
run_4=df.loc[df.runs==4,:].reset_index(drop=True)
run_6=df.loc[df.runs==6,:].reset_index(drop=True)
r4=run_4.groupby(['year'])['runs'].size()
r6=run_6.groupby(['year'])['runs'].size()

plt.figure(figsize=(15,7))
plt.plot(r4.index,r4.values,'r',marker='^',label='Fours')
plt.plot(r6.index,r6.values,'b',marker='o',label='Sixes')

plt.xlabel('Year')
plt.ylabel('No. of Boundaries')
plt.legend(fontsize=10,loc='upper right')

# Average statistics across all seasons
match_wise_data=df.drop_duplicates(subset='match_code').reset_index(drop=True)
total_runs_per_season=df.groupby(['year'])['total'].sum()
total_balls_per_season=df.groupby(['year'])['delivery'].sum()
match_per_season=match_wise_data.groupby(['year'])['match_code'].count()

avg_ball_per_match=total_balls_per_season/match_per_season
avg_runs_per_match=total_runs_per_season/match_per_season
avg_run_per_ball=total_runs_per_season/total_balls_per_season

avg_data=pd.DataFrame([match_per_season,avg_runs_per_match,avg_ball_per_match,avg_run_per_ball])
avg_data.index=['No. of Matches','Avg runs per match','Avg balls per match','Avg runs per ball']
print(avg_data.T)

plt.figure(figsize=(15,7))
avg_data.T.plot(kind='bar')




