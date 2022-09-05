# Given the following code: 
#
# teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#    for away_team in teams:
#
# What should the next line be to avoid both variables being printed with the same value?

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
      if home_team != away_team:
        print(home_team +"  VS  "+away_team) 
