import sqlite3
from sqlite3 import Error
import pandas as pd
from StdevFunc import StdevFunc
import time
start_time = time.time()

db = pd.read_excel('LeagueGoalKeeping.xlsx')


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def totalScore(name):
    dataPoint = 0
    cursor.execute("""SELECT  AgeScore, PlayingTimeMPScore, 
    PlayingTimeStartsScore, PlayingTimeMinScore, PlayingTime90sScore, PerformanceGAScore,
    PerformanceGA90Score, PerformanceSoTAScore, PerformanceSavesScore, PerformanceSavepercentageScore,
    WScore, DScore, LScore, PerformanceCSScore, PerformanceCSpercentageScore, PerformancePKattScore,
    PenaltyKicksPKAScore, PenaltyKicksPKsvScore, PenaltyKicksPKmScore, PenaltyKicksSavepercentageScore, TotalScore 
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
    cursor.execute("SELECT Player FROM LeagueGoalKeeping2 WHERE Pos LIKE '%GK%' AND Year = '2021'")
    Players = cursor.fetchall()
    listOfPlayers = []
    print(Players)
    for item in Players:
        listOfPlayers.append(item[0])
    for i in range(len(listOfPlayers)):
        cursor.execute("""INSERT INTO """ + table + """(Players)
                         VALUES (?)""", Players[i])
    return



def enterScores(scoringFunc):
    cursor.execute("SELECT Player FROM LeagueGoalKeeping2 WHERE Pos LIKE '%GK%'")
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
                    try:
                        score = (item[0]-average)/stdev
                        cursor.execute("UPDATE " + tableName + " SET " + column + "Score = ? where Players = ? ",
                                       (score, name,))
                    except ZeroDivisionError:
                        score = None
                        cursor.execute("UPDATE " + tableName + " SET " + column + "Score = ? where Players = ? ",
                                       (score, name,))
    return


if __name__ == '__main__':

    tableName = "LeagueGoalKeepingScoring4"
    conn = create_connection('LeagueGoalKeeping2.db')
    conn.create_aggregate("stdev", 1, StdevFunc)
    # db.to_sql('LeagueGoalKeeping2', conn)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS """ + tableName + """ (Players TEXT, AgeScore REAL, PlayingTimeMPScore Real, 
    PlayingTimeStartsScore Real, PlayingTimeMinScore Real, PlayingTime90sScore Real, PerformanceGAScore Real,
    PerformanceGA90Score Real, PerformanceSoTAScore Real, PerformanceSavesScore Real, PerformanceSavepercentageScore Real,
    WScore Real, DScore Real, LScore Real, PerformanceCSScore Real, PerformanceCSpercentageScore Real, PerformancePKattScore Real,
    PenaltyKicksPKAScore Real, PenaltyKicksPKsvScore Real, PenaltyKicksPKmScore Real, PenaltyKicksSavepercentageScore Real,
    TotalScore REAL )""")

    # cursor.execute("DELETE FROM " + tableName)
    # dataEntry(tableName)
    allScore("'2021'", "'%GK%'", "LeagueGoalKeeping2")
    conn.commit()
    enterScores(totalScore)
    conn.commit()
    sql = "SELECT * FROM " + tableName
    df = pd.read_sql_query(sql, conn)
    df.to_csv("LeagueGoalKeepingScoring.csv")

    cursor.execute('SELECT * FROM ' + tableName)
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    print('%s seconds' % (time.time()-start_time))
