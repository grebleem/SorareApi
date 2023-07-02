# Example queries for Sorare

getAllPlayer = """
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
            team{
        abbreviation
        name
        slug
      }
    }
  }
}
"""

all_teams_slug = {'milwaukee-brewers', 'houston-astros', 'minnesota-twins', 'baltimore-orioles', 'san-francisco-giants',
                  'washington-nationals', 'chicago-white-sox', 'colorado-rockies', 'pittsburgh-pirates',
                  'cleveland-guardians', 'chicago-cubs', 'new-york-yankees', 'los-angeles-angels', 'tampa-bay-rays',
                  'seattle-mariners', 'philadelphia-phillies', 'san-diego-padres', 'atlanta-braves', 'miami-marlins',
                  'oakland-athletics', 'los-angeles-dodgers', 'st-louis-cardinals', 'toronto-blue-jays',
                  'detroit-tigers', 'new-york-mets', 'arizona-diamondbacks', 'boston-red-sox', 'kansas-city-royals',
                  'texas-rangers', 'cincinnati-reds'}
