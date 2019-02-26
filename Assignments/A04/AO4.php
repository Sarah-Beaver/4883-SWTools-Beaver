<?php
/**

*Course: cmps 4883
*Assignemt: A04
*Date: 2/26/19
*Github username: bluefire8421
*Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
*Name: Sarah Beaver
*Description: 
*    using the database to answer question to show how much easier it is

*/

// Require the config file with credentials
include("./config.php");

//Connect to mysql
$mysqli = mysqli_connect($host, $username, $password, $database);
// Throw mysql error
if (mysqli_connect_errno($mysqli)) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}


function f(){
  
    flush();
}
/**
 * Pulls a player out of players table and returns:
 *     [name] => Player.Name
 * Params:
 *     playerId [string] : id of type => 00-000001234
 * Returns:
 *     name [string] : => T. Smith
 */
function getPlayer($playerId){
    global $mysqli;
    $sql = "SELECT `name` FROM players WHERE id = '{$playerId}' LIMIT 1";
    $response = runQuery($mysqli,$sql); 
    if(!array_key_exists('error',$response)){
        return $response['result'][0]['name'];
    }
    return null;
}
/**
 * Prints a question plus a border underneath
 * Params:
 *     question [string] : "Who ran the most yards in 2009?"
 *     pads [array] : [3,15,15,5] padding for each data field
 * Returns:
 *     header [string] : Question with border below
 */
function printHeader($question,$pads,$cols){
    if(strlen($question) > array_sum($pads)){
        $padding = strlen($question);
    }else{
        $padding = array_sum($pads);
    }
    $header = "\n<b>";
    $header .= "{$question}\n\n";
    for($i=0;$i<sizeof($cols);$i++){
        $header .= str_pad($cols[$i],$pads[$i]);
    }
    $header .= "\n".str_repeat("=",$padding);
    $header .= "</b>\n";
    return $header;
}
/**
 * formatRows:
 *    Prints each row with a specified padding for allignment
 * Params:
 *    $row [array] - array of multityped values to be printed
 *    $cols [array] - array of ints corresponding to each column size wanted
 * Example:
 *    
 *    $row = ['1','00-00000123','T. Smith','329']
 *    $pads = [4,14,20,5]
 */
function formatRows($row,$pads){
    $ouput = "";
    for($i=0;$i<sizeof($row);$i++){
        $output .= str_pad($row[$i],$pads[$i]);
    }
    
    return $output."\n";
}
/**
 * This function runs a SQL query and returns the data in an associative array
 * that looks like:
 * $response [
 *      "success" => true or false
 *      "error" => contains error if success == false
 *      "result" => associative array of the result
 * ]
 *
 */
function runQuery($mysqli,$sql){
    $response = [];
    // run the query
    $result = $mysqli->query($sql);
    // If we were successful
    if($result){
        $response['success'] = true;
        // loop through the result printing each row
        while($row = $result->fetch_assoc()){
            $response['result'][] = $row;
        }
        $result->free();
    }else{
        $response['success'] = false;
        $response['error'] = $mysqli->error;
    }
    return $response;
}
/**
 * displayQuery: print question + sql result in a consistent and 
 *               formatted manner
 * Params: 
 *     question [string] : question text
 *     sql [string] : sql query
 *     cols [array] : column headers in array form
 *     pads [array] : padding size in ints for each column
 */
function displayQuery($question,$sql,$cols,$pads,$coltitles){
    global $mysqli;
    $parts = explode('.',$question);
    if($parts[0]%2==0){
        $color="#C0C0C0";
    }else{
        $color = "";
    }
    echo"<pre style='background-color:{$color}'>";
    echo printHeader($question,$pads,$coltitles);
    $response = runQuery($mysqli,$sql);
    if($response['success']){
        foreach($response['result'] as $id => $row){
            //if it has win loss then prints id's backwards
            if($row['winlosspercent'])
            {
                $id=32-$id;
            }
            else{
                $id++;
            }
            
            $row['id'] = $id;
            if($row['playerid'])
            {
                $row['name'] = getPlayer($row['playerid']);
            }
            
            for( $i=0;$i<sizeof($cols);$i++)
            {
                $row[$i]=$row[$cols[$i]];
            }
            echo formatRows($row,$pads);
        }
    }
    else{
        echo $response['error'];
    }
    echo"</pre>";
    f();
}

/**
 * displayQuery2: print question + sql result in a consistent and 
 *               formatted manner used only for question 7
 * Params: 
 *     question [string] : question text
 *     sql [string] : sql query
 *     coltitles [array] : column headers in array form
 *     col[array] : column names in array form
 *     pads [array] : padding size in ints for each column
 *    
 */
function displayQuery2($question,$sql,$cols,$pads,$coltitles){
    global $mysqli;
    $parts = explode('.',$question);
    if($parts[0]%2==0){
        $color="#C0C0C0";
    }else{
        $color = "";
    }
    echo"<pre style='background-color:{$color}'>";
    echo printHeader($question,$pads,$coltitles);
    $response = runQuery($mysqli,$sql);
    if($response['success']){
        $season=0;
        $idcount=1;
        foreach ($response['result'] as $id => $row) {
            // only prints top row per season
            if ($row['season'] != $season) {
                $season = $row['season'];

                $row['id'] = $idcount;

                for ($i = 0; $i < sizeof($cols); $i++) {
                    $row[$i] = $row[$cols[$i]];
                }
                echo formatRows($row, $pads);
                $idcount++;
                $yearcount++;
            }
        }   
        }
    
    else{
        echo $response['error'];
    }
    echo"</pre>";
    f();
}

/**
 * Header
 */
echo"<pre style='background-color:#C0C0C0'>";
echo "Name: Sarah Beaver
Assignment: A04 - Nfl Stats 
Date: 2/23/19

==================================================================================

";
echo"</pre>";

/**
 * Question 1
 */
$question = "1. Count number of teams a player played for.";
$pads = [3,12,20,5];
$sql = "SELECT id as playerid,name,count(distinct(club)) as count FROM `players` group by id,name ORDER BY `count` DESC LIMIT 5";
$cols = ['id','playerid','name','count'];
$colsTitle=['#','PlayerID','Name','# Teams'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 2
 */
$question = "2. Find the top 5 rushing players per year.";
$pads = [3,12,15,7,8];
$sql = "SELECT playerid, season, sum(yards) as sumyards FROM `players_stats` where statid=10 or statid=75 or statid=76 group by season, playerid order by sumyards desc limit 5";
$cols = ['id','playerid','name','season','sumyards'];
$colsTitle=['#','PlayerID','Name','Year','# Yards'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 3
 */
$question = "3. Find the bottom 5 passing players per year.";
$pads = [3,12,15,7,8];
$sql = "SELECT playerid, season, sum(yards) as sumyards FROM `players_stats` where statid=15 or statid=16 or statid=77 or statid=78 group by season, playerid order by  sumyards asc limit 5";
$cols = ['id','playerid','name','season','sumyards'];
$colsTitle=['#','PlayerID','Name','Year','# Yards'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 4
 */
$question = "4. Find the top 5 that had the most rushes for a loss.";
$pads = [3,12,15,7,8];
$sql = "SELECT `playerid`,`season`,COUNT(`yards`) as negative_carries FROM `players_stats` WHERE `yards` < 0 and `statid` = '10' GROUP BY `season`,`playerid`  ORDER BY `negative_carries`  DESC LIMIT 5";
$cols = ['id','playerid','name','season','negative_carries'];
$colsTitle=['#','PlayerID','Name','Year','# Rushed for Loss'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 5
 */
$question = "5. Find the top 5 teams with the most penalties.";
$pads = [3,12,15];
$sql = "SELECT club,sum(pen) as pen FROM `game_totals` GROUP BY club  ORDER BY `pen`  DESC LIMIT 5";
$cols = ['id','club','pen'];
$colsTitle=['#','Team','# Penalties'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 6
 */
$question = "6. Find the average number of penalties per year.";
$pads = [3,8,17,17];
$sql = "SELECT season,sum(pen) as sum,avg(pen) as avg FROM `game_totals` group by season";
$cols = ['id','season','sum','avg'];
$colsTitle=['#','Season','Total Penalties', 'Avg Penalties'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 7
 */
$question = "7. Find the Team with the least amount of average plays every year.";
$pads = [3,8,6,17];
$sql = "Select gamesperclub.season as season ,gamesperclub.club as club, count(Distinct playid)/gamesperclub.count as avgplays from plays, (SELECT club,  count(DISTINCT gameid) as count, season FROM `game_totals` group by season, club) as gamesperclub where gamesperclub.club=plays.clubid group by gamesperclub.season,gamesperclub.club order by season,avgplays asc";
$cols = ['id','season','club','avgplays'];
$colsTitle=['#','Season','Team', 'Avg Plays'];
displayQuery2($question,$sql,$cols,$pads,$colsTitle,1);

/**
 * Question 8
 */
$question = "8. Find the top 5 players that had field goals over 40 yards.";
$pads = [3,12,15,10];
$sql = "SELECT playerid, yards FROM `players_stats`  where `statid`=70 and yards>40 group by playerid  ORDER BY yards  DESC limit 5";
$cols = ['id','playerid','name','yards'];
$colsTitle=['#','PlayerID','Name', 'Field Goal Yards'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 9
 */
$question = "9. Find the top 5 players with the shortest avg field goal length.";
$pads = [3,10,15,10];
$sql = "SELECT players_stats.playerid,avg(players_stats.yards) as avgyards FROM `players_stats`  where `statid`=70  group by players_stats.playerid  ORDER BY avgyards  asc limit 5";
$cols = ['id','playerid','name','avgyards'];
$colsTitle=['#','PlayerID','Name', 'Avg Field Goal'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 10
 */
$question = "10. Rank the NFL by win loss percentage (worst first).";
$pads = [5,10,15];
$sql = "SELECT `club`, sum(if(`wonloss` like 'won',1,0))/ sum(if(`wonloss` like 'loss',1,0)) as winlosspercent FROM `game_totals` group by club ORDER BY winlosspercent ASC";
$cols = ['id','club','winlosspercent'];
$colsTitle=['#','Team','Win/Loss %'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);

/**
 * Question 11
 */
$question = "11. Find the top 5 most common last names in the NFL.";
$pads = [3,10,15,10];
$sql = "SELECT   validlastnames.lastname as lastname, count(validlastnames.lastname) as occurences FROM (SELECT  id, name, if(substring_index(name,'.',-1)='',substring_index(name,'.',-2),substring_index(name,'.',-1)) as lastname FROM `players`  group by id order by lastname) as validlastnames  group by validlastnames.lastname ORDER BY occurences DESC limit 5";
$cols = ['id','lastname','occurences'];
$colsTitle=['#','Name','Occurances'];
displayQuery($question,$sql,$cols,$pads,$colsTitle);


/**
 * Bonus
 */
echo "Bonus
==================================================================================
";
$question = "12. Find the best 'away' team for every year.";
$pads = [3,10,15,10];
$sql = "SELECT `away_club`,season,(sum(if(win_type='away',1,0))/count(win_type))*100 as awaypercent FROM `games` group by season, away_club order by season,awaypercent desc";
$cols = ['id','season','away_club','awaypercent'];
$colsTitle=['#','Season','Club', 'Away %'];
displayQuery2($question,$sql,$cols,$pads,$colsTitle);
?>