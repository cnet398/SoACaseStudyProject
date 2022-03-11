import sqlite3
from sqlite3 import Error
import pandas as pd
from StdevFunc import StdevFunc
import time
start_time = time.time()

db = pd.read_excel('LeagueDefense.xlsx')


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn








def ageScore(name):
    weight = 1
    cursor.execute("SELECT stdev(Age) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(Age) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT Age FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET ageScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET ageScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET ageScore = ? where Players = ? ", (score, name,))
    return

def N90sScore(name):
    weight = 1
    cursor.execute("SELECT stdev(N90s) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(N90s) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT N90s FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        score += ((item[0]-average)/stdev)*weight
        cursor.execute("UPDATE " + tableName + " SET N90sScore = ? where Players = ? ", (score, name,))
        #     if item[0] > average + stdev:
        #         score += weight
        #         cursor.execute("UPDATE " + tableName + " SET N90sScore = ? where Players = ? ", (score, name,))
        #     elif item[0] < average - stdev:
        #         score -= weight
        #         cursor.execute("UPDATE " + tableName + " SET N90sScore = ? where Players = ? ", (score, name,))
        #     else:
        #         cursor.execute("UPDATE " + tableName + " SET N90sScore = ? where Players = ? ", (score, name,))
    return


def tackleTklScore(name):
    weight = 1
    cursor.execute("SELECT stdev(TacklesTkl) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(TacklesTkl) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT TacklesTkl FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score +=  weight
            cursor.execute("UPDATE " + tableName + " SET TackleTklScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET TackleTklScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET TackleTklScore = ? where Players = ? ", (score, name,))
    return


def tacklesTklWScore(name):
    weight = 1
    cursor.execute("SELECT stdev(TacklesTklW) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(TacklesTklW) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT TacklesTklW FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET tacklesTklWScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET tacklesTklWScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET tacklesTklWScore = ? where Players = ? ", (score, name,))
    return


def tacklesDef3rdScore(name):
    weight = 1
    cursor.execute("SELECT stdev(TacklesDef3rd) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(TacklesDef3rd) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT TacklesDef3rd FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET tacklesDef3rdScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET tacklesDef3rdScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET tacklesDef3rdScore = ? where Players = ? ", (score, name,))
    return


def tacklesMid3rdScore(name):
    weight = 1
    cursor.execute("SELECT stdev(TacklesMid3rd) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(TacklesMid3rd) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT TacklesMid3rd FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET tacklesMid3rdScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET tacklesMid3rdScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET tacklesMid3rdScore = ? where Players = ? ", (score, name,))
    return


def tacklesAtt3rdScore(name):
    weight = 1
    cursor.execute("SELECT stdev(TacklesAtt3rd) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(TacklesAtt3rd) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT TacklesAtt3rd FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET tacklesAtt3rdScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET tacklesAtt3rdScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET tacklesAtt3rdScore = ? where Players = ? ", (score, name,))
    return

def vsDribblesTklScore(name):
    weight = 1
    cursor.execute("SELECT stdev(VsDribblesTkl) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(VsDribblesTkl) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT VsDribblesTkl FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET vsDribblesTklScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET vsDribblesTklScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET vsDribblesTklScore = ? where Players = ? ", (score, name,))
    return

def vsDribblesTklPercentageScore(name):
    weight = 1
    value = None
    cursor.execute("SELECT stdev(VsDribblesTkl) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(VsDribblesTkl) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT VsDribblesTkl FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] is None:
            cursor.execute("UPDATE " + tableName + " SET PressuresPercentageScore = ? where Players = ? ",
                           (value, name,))
        elif item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET vsDribblesTklPercentageScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET vsDribblesTklPercentageScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET vsDribblesTklPercentageScore = ? where Players = ? ", (score, name,))
    return



def vsDribblesPastScore(name):
    weight = 1
    cursor.execute("SELECT stdev(VsDribblesPast) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(VsDribblesPast) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT VsDribblesPast FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET vsDribblesPastScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET vsDribblesPastScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET vsDribblesPastScore = ? where Players = ? ", (score, name,))
    return


def pressuresPressScore(name):
    weight = 1
    cursor.execute("SELECT stdev(PressuresPress) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(PressuresPress) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT PressuresPress FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET PressuresPressScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET PressuresPressScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET PressuresPressScore = ? where Players = ? ", (score, name,))
    return


def pressuresSuccScore(name):
    weight = 1
    cursor.execute("SELECT stdev(PressuresSucc) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(PressuresSucc) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT PressuresSucc FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET PressuresSuccScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET PressuresSuccScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET PressuresSuccScore = ? where Players = ? ", (score, name,))
    return


def pressuresPercentageScore(name):
    weight = 1
    value = None
    cursor.execute("SELECT stdev(PressuresPercentage) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(PressuresPercentage) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT PressuresPercentage FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] is None:
            cursor.execute("UPDATE " + tableName + " SET PressuresPercentageScore = ? where Players = ? ", (value, name,))
        elif item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET PressuresPercentageScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET PressuresPercentageScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET PressuresPercentageScore = ? where Players = ? ", (score, name,))
    return



def pressuresDef3rdScore(name):
    weight = 1
    cursor.execute("SELECT stdev(PressuresDef3rd) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(PressuresDef3rd) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT PressuresDef3rd FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET PressuresDefScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET PressuresDefScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET PressuresDefScore = ? where Players = ? ", (score, name,))
    return

def pressuresMid3rdScore(name):
    weight = 1
    cursor.execute("SELECT stdev(PressuresMid3rd) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(PressuresMid3rd) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT PressuresMid3rd FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET PressuresMid3rdScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET PressuresMid3rdScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET PressuresMid3rdScore = ? where Players = ? ", (score, name,))
    return


def blocksBlocksScore(name):
    weight = 1
    cursor.execute("SELECT stdev(BlocksBlocks) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(BlocksBlocks) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT BlocksBlocks FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET BlocksBlocksScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET BlocksBlocksScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET BlocksBlocksScore = ? where Players = ? ", (score, name,))
    return


def blocksShScore(name):
    weight = 1
    cursor.execute("SELECT stdev(BlocksSh) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(BlocksSh) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT BlocksSh FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET BlocksShScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET BlocksShScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET BlocksShScore = ? where Players = ? ", (score, name,))
    return



def blocksPassScore(name):
    weight = 1
    cursor.execute("SELECT stdev(BlocksPass) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(BlocksPass) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT BlocksPass FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET BlocksPassScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET BlocksPassScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET BlocksPassScore = ? where Players = ? ", (score, name,))
    return


def intScore(name):
    weight = 1
    cursor.execute("SELECT stdev(Int) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(Int) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT Int FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET IntScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET IntScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET IntScore = ? where Players = ? ", (score, name,))
    return


def tklPlusIntScore(name):
    weight = 1
    cursor.execute("SELECT stdev(TklPlusInt) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(TklPlusInt) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT TklPlusInt FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET TklPlusIntScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET TklPlusIntScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET TklPlusIntScore = ? where Players = ? ", (score, name,))
    return


def clrScore(name):
    weight = 1
    cursor.execute("SELECT stdev(Clr) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(Clr) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT Clr FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET ClrScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET ClrScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET ClrScore = ? where Players = ? ", (score, name,))
    return


def errScore(name):
    weight = 1
    cursor.execute("SELECT stdev(Err) FROM LeagueDefense where Pos LIKE '%DF%' AND Year = '2021'")
    stdev = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(Err) FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    average = cursor.fetchall()[0][0]
    cursor.execute("SELECT Err FROM LeagueDefense WHERE Player = ? AND Year = '2021'", (name,))
    for item in cursor.fetchall():
        score = 0
        if item[0] > average + stdev:
            score += weight
            cursor.execute("UPDATE " + tableName + " SET ErrScore = ? where Players = ? ", (score, name,))
        elif item[0] < average - stdev:
            score -= weight
            cursor.execute("UPDATE " + tableName + " SET ErrScore = ? where Players = ? ", (score, name,))
        else:
            cursor.execute("UPDATE " + tableName + " SET ErrScore = ? where Players = ? ", (score, name,))
    return


def totalScore(name):
    dataPoint = 0
    cursor.execute("""SELECT AgeScore, N90sScore, TacklesTklScore,  TacklesTklWScore,  TacklesDef3rdScore, 
    TacklesMid3rdScore, TacklesAtt3rdScore, VsDribblesTklScore, VsDribblesTklPercentageScore, VsDribblesPastScore, 
    PressuresPressScore, PressuresSuccScore, PressuresPercentageScore, PressuresDef3rdScore, PressuresMid3rdScore, 
    BlocksBlocksScore, BlocksShScore, BlocksPassScore, IntScore, TklPlusIntScore, ClrScore, ErrScore
    FROM """ + tableName + """ WHERE Players = ?""", (name,))
    dataSet = cursor.fetchall()
    for thing in dataSet:
        for item in thing:
            if item is None:
                dataPoint += 0
            else:
                dataPoint += item

    cursor.execute("UPDATE " + tableName + " SET TotalScore = ? where Players = ? ", (dataPoint, name,))


def dataEntry(table):
    cursor.execute("SELECT Player FROM LeagueDefense WHERE Pos LIKE '%DF%' AND Year = '2021'")
    Players = cursor.fetchall()
    listOfPlayers = []
    for item in Players:
        listOfPlayers.append(item[0])
    for i in range(len(listOfPlayers)):
        cursor.execute("""INSERT INTO """ + table + """(Players)
                         VALUES (?)""", Players[i])
    return


def enterScores(scoringFunc):
    cursor.execute("SELECT Player FROM LeagueDefense WHERE Pos LIKE '%DF%'")
    Players = cursor.fetchall()
    listOfPlayers = []
    for item in Players:
        listOfPlayers.append(item[0])
    for i in range(len(listOfPlayers)):
        scoringFunc(listOfPlayers[i])
    return


def allScore(year, pos, datasheet):
    columns = []
    names = []
    data = cursor.execute('SELECT * FROM ' + datasheet)
    for item in data.description:
        columns.append(item[0])
    try:
        columns.remove('Squad')
    except ValueError:
        pass
    try:
        columns.remove('Born')
        columns.remove('Player')
        columns.remove('Pos')
        columns.remove('index')
        columns.remove('Nation')
        columns.remove('League')
        columns.remove('Column1')
        columns.remove('Year')
    except ValueError:
        pass
    cursor.execute("SELECT Player FROM " + datasheet)
    for name in cursor.fetchall():
        names.append(str(name[0]))

    for name in names:
        for column in columns:
            weight = 1
            value = None
            cursor.execute("SELECT stdev(" + column + ") FROM " + datasheet + " where Pos LIKE " + pos + " AND Year = " + year)
            stdev = cursor.fetchone()[0]
            cursor.execute("SELECT AVG(" + column + ") FROM " + datasheet + " WHERE Pos LIKE " + pos + " AND Year = " + year)
            average = cursor.fetchall()[0][0]
            # data = {"column" : column, "name" : name, "year" : year}
            try:
                cursor.execute("SELECT " + column + " FROM " + datasheet + " WHERE Player = " + "'" + name + "'" + " AND Year = " + year)
            except:
                print("bad data")
            items = cursor.fetchall()
            for item in items:
                if item[0] is None:
                    cursor.execute("UPDATE " + tableName + " SET " + column + "Score = ? where Players = ? ",
                                   (value, name,))
                # elif item[0] > average + stdev:
                #     score += weight
                #     cursor.execute("UPDATE " + tableName + " SET " + column + "Score = ? where Players = ? ",
                #                    (score, name,))
                # elif item[0] < average - stdev:
                #     score -= weight
                #     cursor.execute("UPDATE " + tableName + " SET " + column + "Score = ? where Players = ? ",
                #                    (score, name,))
                else:
                    score = (item[0]-average)/stdev
                    cursor.execute("UPDATE " + tableName + " SET " + column + "Score = ? where Players = ? ",
                                   (score, name,))
    return


if __name__ == '__main__':

    tableName = "LeagueDefenseScoring19"
    conn = create_connection('LeagueDefense.db')
    conn.create_aggregate("stdev", 1, StdevFunc)
    # db.to_sql('ActuaryCompetition', conn)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS """ + tableName + """ (Players TEXT, AgeScore REAL, N90sScore REAL, TacklesTklScore
     REAL, TacklesTklWScore REAL,  TacklesDef3rdScore REAL, TacklesMid3rdScore REAL, TacklesAtt3rdScore REAL, VsDribblesAttScore REAL,
     VsDribblesTklScore REAL, VsDribblesTklPercentageScore REAL, VsDribblesPastScore REAL, PressuresPressScore REAL,
     PressuresSuccScore REAL, PressuresPercentageScore REAL, PressuresDef3rdScore REAL, PressuresMid3rdScore REAL, PressuresAtt3rdScore REAL,
     BlocksBlocksScore REAL, BlocksShScore REAL, BlocksShSvScore REAL, BlocksPassScore REAL, IntScore REAL, TklPlusIntScore REAL,
     ClrScore REAL, ErrScore REAL, TotalScore Real)""")

    cursor.execute("DELETE FROM " + tableName)
    dataEntry(tableName)
    # enterScores(ageScore)
    # enterScores(N90sScore)
    # enterScores(tackleTklScore)
    # enterScores(tacklesTklWScore)
    # enterScores(tacklesDef3rdScore)
    # enterScores(tacklesMid3rdScore)
    # enterScores(tacklesAtt3rdScore)
    # enterScores(vsDribblesTklScore)
    # enterScores(vsDribblesTklPercentageScore)
    # enterScores(vsDribblesPastScore)
    # enterScores(pressuresPressScore)
    # enterScores(pressuresSuccScore)
    # enterScores(pressuresPercentageScore)
    # enterScores(pressuresDef3rdScore)
    # enterScores(pressuresMid3rdScore)
    # enterScores(blocksBlocksScore)
    # enterScores(blocksShScore)
    # enterScores(blocksPassScore)
    # enterScores(intScore)
    # enterScores(tklPlusIntScore)
    # enterScores(clrScore)
    # enterScores(errScore)

    allScore("'2021'", "'%DF%'", "LeagueDefense")
    conn.commit()
    enterScores(totalScore)
    conn.commit()
    sql = "SELECT * FROM " + tableName
    df = pd.read_sql_query(sql, conn)
    df.to_csv("LeagueDefenseScoring.csv")

    cursor.execute('SELECT * FROM ' + tableName)
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    print('%s seconds' % (time.time()-start_time))