* scrape_nfl.py 
    * gets all the ids and scrapes the nfl live site of the game stats then adds id to a dictionary, at end dumps the ids into GameIds.json and dumps the actually game json into ./Data/{{gameid}}.json
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

    
Run scrape_nfl.py to get all the gameids and will put each gameid.json file into a ./Data folder and store the gameids in GameIds.json. 
The users can then either download the remaining data structures or .json files and place them at same level as calculate_stats.py or can download OrganizeFieldGoals.py,OrganizePlayers.py, Valid_Teams.json, OrganizeTeams.py and follow the steps below.
Running OrganizeFieldGoals.py and OrganizePlayers.py will pull all the gameid.json files from the ./Data folder and create the TeamInfo.json and PlayerInfo.json respectively. These files will be on the same level as the python files. Next make sure Valid_Teams.json is on the same level as the python files before running Organizeteams.py which will also use the gameid.json files from the ./Data folder to create the TeamInfo.json
Now the user can run calculate_stats.py which uses the .json files and the ./Data/{{gameid}}.json files to calculate the stats. The answer is then written to answer.txt.
