import psycopg2

class Database:
    def execute_query(self, query):
        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5432',
                database='panda_stocks',
                user='postgres',
                password='postgres'
            )

            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Database error: {e}")


    def execute_select_query(self, query):
        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5432',
                database='panda_stocks',
                user='postgres',
                password='postgres'
            )
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
            return rows

        except Exception as e:
            print(f"Database error: {e}")

    def storeStockData(self, df):
        try:
            data = df.to_dict(orient = "records")
            for row in data:
                query = f"""
                INSERT INTO stock_data
                (ticker, period, avg_price, max_price, min_price, number_of_days, analysis_date)
                VALUES (
                    '{row["ticker"]}',
                    '{row["period"]}',
                    {row["avg price"]},
                    {row["max price"]},
                    {row["min price"]},
                    {row["number of days"]},
                    '{row["analysis date"]}'
                );
                """
                self.execute_query(query)

            print("Stock data stored successfully.")

        except Exception as e:
            print(f"Error storing stock data: {e}")