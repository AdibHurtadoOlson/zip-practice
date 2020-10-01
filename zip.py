nations = ['United States', 'Mexico', 'Canada', 'Korea', Germany', 'Mozambique']
capitals = ['Washington D.C', 'Mexico City', 'Ottawa', 'Seoul', 'Berlin', 'Maputo']

for capital, nation in zip(capitals, nations):
  print(f'{capitals} is the capital of {nation}')
