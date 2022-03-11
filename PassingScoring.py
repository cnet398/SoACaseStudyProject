import sqlite3
from sqlite3 import Error
import pandas as pd
from StdevFunc import StdevFunc
import time
start_time = time.time()

db = pd.read_excel('LeaguePassing.xlsx')


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
    cursor.execute("""SELECT  AgeScore , N90sScore , 
    TotalCmpScore , TotalAttScore, TotalCmpPercentageScore, TotalTotDistScore, TotalPrgDistScore, 
    ShortCmpScore, ShortAttScore, ShortCmpPercentageScore, MediumCmpScore, MediumAttScore, 
    MediumCmpPercentageScore, LongCmpScore, LongAttScore, LongCmpPercentageScore, AstScore, 
    xAScore, AxAScore, KPScore, T1slash3Score, PPAScore, CrsPAScore, ProgScore, TotalScore 
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
    cursor.execute("SELECT Player FROM LeaguePassing WHERE Pos NOT LIKE '%GK%' AND Year = '2021'")
    Players = cursor.fetchall()
    listOfPlayers = []
    for item in Players:
        listOfPlayers.append(item[0])
    for i in range(len(listOfPlayers)):
        cursor.execute("""INSERT INTO """ + table + """(Players)
                         VALUES (?)""", Players[i])
    return



def enterScores(scoringFunc):
    cursor.execute("SELECT Player FROM LeaguePassing WHERE Pos NOT LIKE '%GK%'")
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
            cursor.execute("SELECT stdev(" + column + ") FROM " + datasheet + " where Pos NOT LIKE " + pos + " AND Year = " + year)
            stdev = cursor.fetchone()[0]
            cursor.execute("SELECT AVG(" + column + ") FROM " + datasheet + " WHERE Pos NOT LIKE " + pos + " AND Year = " + year)
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

    tableName = "LeaguePassingScoring"
    conn = create_connection('LeaguePassing.db')
    conn.create_aggregate("stdev", 1, StdevFunc)
    # db.to_sql('LeaguePassing', conn)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS """ + tableName + """ (Players TEXT, AgeScore REAL, N90sScore REAL, 
    TotalCmpScore REAL, TotalAttScore REAL, TotalCmpPercentageScore REAL, TotalTotDistScore REAL, TotalPrgDistScore REAL, 
    ShortCmpScore Real, ShortAttScore Real, ShortCmpPercentageScore Real, MediumCmpScore Real, MediumAttScore Real, 
    MediumCmpPercentageScore Real, LongCmpScore Real, LongAttScore Real, LongCmpPercentageScore Real, AstScore Real, 
    xAScore Real, AxAScore Real, KPScore Real, T1slash3Score Real, PPAScore Real, CrsPAScore Real, ProgScore Real, TotalScore REAL )""")

    # cursor.execute("DELETE FROM " + tableName)
    # dataEntry(tableName)
    # allScore("'2021'", "'%GK%'", "LeaguePassing")
    # conn.commit()
    enterScores(totalScore)
    conn.commit()
    sql = "SELECT * FROM " + tableName
    df = pd.read_sql_query(sql, conn)
    df.to_csv("LeaguePassingScoring.csv")

    cursor.execute('SELECT * FROM ' + tableName)
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    print('%s seconds' % (time.time()-start_time))