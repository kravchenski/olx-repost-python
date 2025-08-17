import datetime

from mysql.connector.aio import connect

from ..config import mysql_user, mysql_password, mysql_database, mysql_host


class MySQLDatabaseModel:
    @staticmethod
    async def store_ad(index, data):
        for ad in data:
            ad_id = ad['id']
            ad_activated_date = ad['activatedAt']
            ad_validTo_date = ad['validTo']
            ad_title = ad['title']
            ad_price = int(ad['price'])
            ad_views = ad['stats']['views']
            ad_favorites = ad['stats']['observed']
            ad_calls = ad['stats']['phones']
            conn = await connect(user=mysql_user, password=mysql_password, database=mysql_database, host=mysql_host)
            cur = await conn.cursor()
            await cur.execute(
                '''INSERT INTO olx(account_id,advertising_id,title,price,start_date,end_date,views,likes,
                calls,date,time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                (index, ad_id,
                ad_title, ad_price, ad_activated_date, ad_validTo_date, ad_views, ad_favorites, ad_calls,
                str(datetime.datetime.today()),
                str(datetime.datetime.today().strftime("%H:%M"))))
            await conn.commit()
            await conn.close()

    async def select_all_rows_from_transfer_db(self):
        conn = await connect(user=mysql_user, password=mysql_password, database=mysql_database, host=mysql_host)
        cur = await conn.cursor()
        await cur.execute("SELECT * FROM transfer_ads")
        rows = await cur.fetchall()
        await conn.close()
        return rows if rows else []
    
    @staticmethod
    async def check_ad_in_db(ad_id):
        conn = await connect(user=mysql_user, password=mysql_password, database=mysql_database, host=mysql_host)
        cur = await conn.cursor()
        await cur.execute("SELECT * FROM olx WHERE advertising_id = %s", (ad_id,))
        row = await cur.fetchone()

        await conn.close()

        if row is None:
            raise Exception("ID IS NONE")
        else:
            return int(row[2])

    @staticmethod
    async def update_is_transferred_field_in_transfer_db(ad_id: int):
        conn = await connect(user=mysql_user, password=mysql_password, database=mysql_database, host=mysql_host)
        cur = await conn.cursor()
        await cur.execute("UPDATE transfer_ads SET is_transferred = %s WHERE advertising_id = %s", (True, ad_id))
        await conn.commit()
        await conn.close()
