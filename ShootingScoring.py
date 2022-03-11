import sqlite3
from sqlite3 import Error
import pandas as pd
from StdevFunc import StdevFunc
import time
start_time = time.time()

db = pd.read_excel('leagueshootingcleaned.xlsx')


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
    cursor.execute("""SELECT AgeScore , score90sScore , 
    GlsScore, StandardShScore, StandardSoTScore, StandardSoTpercentageScore, StandardSh90Score, 
    StandardSoT90Score, StandardGShScore, StandardGSoTScore, StandardDistScore, StandardFKScore, 
    PerformancePKScore, PerformancePKattScore, ExpectedxGScore, ExpectednpxGScore, 
    ExpectednpxGShScore,  ExpectedGxGScore, ExpectednpGxGScore
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
    cursor.execute("SELECT Player FROM leagueshootingcleaned WHERE Pos LIKE '%FW%' AND Year = '2021'")
    Players = cursor.fetchall()
    listOfPlayers = []
    for item in Players:
        listOfPlayers.append(item[0])
    for i in range(len(listOfPlayers)):
        cursor.execute("""INSERT INTO """ + table + """(Players)
                         VALUES (?)""", Players[i])
    return



def enterScores(scoringFunc):
    cursor.execute("SELECT Player FROM leagueshootingcleaned WHERE Pos LIKE '%FW%'")
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

    tableName = "LeagueShootingScoring3"
    conn = create_connection('leagueshootingcleaned.db')
    conn.create_aggregate("stdev", 1, StdevFunc)
    # db.to_sql('leagueshootingcleaned', conn)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS """ + tableName + """ (Players TEXT, AgeScore REAL, score90sScore REAL, 
    GlsScore REAL, StandardShScore REAL, StandardSoTScore REAL, StandardSoTpercentageScore REAL, StandardSh90Score REAL, 
    StandardSoT90Score REAL, StandardGShScore REAL, StandardGSoTScore REAL, StandardDistScore REAL, StandardFKScore REAL, 
    PerformancePKScore REAL, PerformancePKattScore REAL, ExpectedxGScore REAL, ExpectednpxGScore REAL, 
    ExpectednpxGShScore REAL,  ExpectedGxGScore REAL, ExpectednpGxGScore REAL, TotalScore Real )""")

    cursor.execute("DELETE FROM " + tableName)
    dataEntry(tableName)
    allScore("'2021'", "'%FW%'", "leagueshootingcleaned")
    conn.commit()
    enterScores(totalScore)
    conn.commit()
    sql = "SELECT * FROM " + tableName
    df = pd.read_sql_query(sql, conn)
    df.to_csv("LeagueShootingScoring.csv")

    cursor.execute('SELECT * FROM ' + tableName)
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    print('%s seconds' % (time.time()-start_time))