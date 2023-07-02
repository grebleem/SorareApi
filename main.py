# Use 'pip install python-graphql-client' to install
from python_graphql_client import GraphqlClient

# import
import query

# Sorare GraphQL API
sorare = GraphqlClient(
    endpoint="https://api.sorare.com/federation/graphql"
)


def get_players(team):
    try:
        query_all_players = query.getAllPlayer
        variables = {"team": team}
        data = sorare.execute(query=query_all_players, variables=variables)
        return data['data']['baseballTeam']['players']

    except Exception as e:
        print(e)


if __name__ == '__main__':
    players = get_players('cleveland-guardians')
    for player in players:
        print(player["slug"])
        print(player["displayName"])
        print(player["positions"])
        print("----------")
