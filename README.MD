## Sorare API Python example

### Installation
```commandline
pip install python-graphql-client
```
See Sorare API: https://github.com/sorare/api 

Sorare PlayGround: https://api.sorare.com/federation/graphql/playground

Example query to get all player of a MLB team in the Playground:
```
query AllTeamPlayer($team:String!) {
  baseballTeam(slug: $team) {
    players{
      slug
      displayName
      positions
      isActive
      age
      playerInjury{
        comment
        startDate
        description
      }
      avatarImageUrl
      croppedPictureUrl
    }
  }
}
```

variables:
```json
{
  "team": "colorado-rockies"
}
```

Sorare team-slugs:
```json
{
  'milwaukee-brewers', 
  'houston-astros', 
  'minnesota-twins', 
  'baltimore-orioles', 
  'san-francisco-giants',
  'washington-nationals', 
  'chicago-white-sox', 
  'colorado-rockies', 
  'pittsburgh-pirates',
  'cleveland-guardians',
  'chicago-cubs', 
  'new-york-yankees', 
  'los-angeles-angels', 
  'tampa-bay-rays',
  'seattle-mariners', 
  'philadelphia-phillies', 
  'san-diego-padres', 
  'atlanta-braves', 
  'miami-marlins',
  'oakland-athletics', 
  'los-angeles-dodgers', 
  'st-louis-cardinals', 
  'toronto-blue-jays',
  'detroit-tigers', 
  'new-york-mets', 
  'arizona-diamondbacks', 
  'boston-red-sox', 
  'kansas-city-royals',
  'texas-rangers', 'cincinnati-reds'}
```