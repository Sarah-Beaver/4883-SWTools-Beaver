* scrape_nfl.py 
    * gets all the ids and scrapes the nfl live site of the game stats then adds id to a dictionary, at end dumps the ids into GameIds.json and dumps the actually game json into Data/{{gameid}}.json
* GameIds.json
   * list all the gameid and shows year and if regular or postseason and week if applicable
* OrganizeTeams.py
     * this pulls out each teams penalties, penalties yard, win, and losses. It uses Valid_Teams.json to check and store team codes correctly then stores the team info into TeamInfo.json
* Valid_Teams.json
   * is used by OrganizeTeams.py as a way to check for valid team codes
* TeamInfo.json
     * where the team info is stored
* OrganizePlayers.py
     * this pulls out each players teams, year for each team, rushes for loss, rushes yards for loss, pass for loss, and stores it into PlayerInfo.json
* PlayerInfo.json
     * where the player info is stored
* OrganizeFieldGoals.py
     * pulls out all longest field goal, number of made field goals, and missed field goals for players then stores the info into FieldGoals.json
* FieldGoals.json
   * where the field goal info is stored
* calculate_stats.py
   * uses all Data/{{gameid}}.json file, FieldGoals.json, PlayerInfo.json, TeamInfo.json to calculate the stats then the answers is written to answer.txt
* answer.txt
   * list out which stat is being answered and the answer

     
Run scrape_nfl.py to get all the ids and will put each gameid.json file into a Data folder. 
OrganizeTeams.py and OrganizePlayers.py will pull all the gameid.json files from the Data and create the TeamInfo.json and PlayerInfo.json respectively. These files will be on the same level as the python files.
