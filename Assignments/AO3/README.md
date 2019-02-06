* scrape_nfl.py 
    * gets all the ids and scrapes the nfl live site of the game stats then adds id to a dictionary, at end dumps the ids into GameIds.json
* OrganizeTeams.py
     * this pulls out each teams penalties, penalties yard, win, and losses and stores it into TeamInfo.json
* TeamInfo.json
     * where the team info is stored
* OrganizePlayers.py
     * this pulls out each players teams, year for each team, rushes for loss, rushes yards for loss, pass for loss, and stores it into PlayerInfo.json
* PlayerInfo.json
     * where the player info is stored
     
Run scrape_nfl.py to get all the ids and will put each gameid.json file into a Data file. 
OrganizeTeams.py and OrganizePlayers.py will pull all the gameid.json files from the Data and create the TeamInfo.json and PlayerInfo.json respectively. These files will be on the same level as the python files.
