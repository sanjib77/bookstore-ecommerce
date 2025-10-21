# test_connection.py
import psycopg2

print("Testing PostgreSQL connection...")
print("-" * 50)

try:
    conn = psycopg2.connect(
        dbname="bookstore_db",
        user="bookstore_user",
        password="bookstore123",  # Use the password you set
        host="localhost",
        port="5432"
    )
    print("✅ SUCCESS! Connected to PostgreSQL!")
    print(f"✅ Database: bookstore_db")
    print(f"✅ User: bookstore_user")
    
    # Test if we can query
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"✅ PostgreSQL version: {version[0][:50]}...")
    
    cursor.close()
    conn.close()
    print("\n🎉 Connection test PASSED! You can proceed with migrations.")
    
except psycopg2.OperationalError as e:
    print("❌ FAILED! Could not connect to PostgreSQL")
    print(f"❌ Error: {e}")
    print("\nPossible issues:")
    print("1. PostgreSQL service is not running")
    print("2. Password is incorrect")
    print("3. Database or user doesn't exist")
    print("\nNext steps:")
    print("- Open SQL Shell (psql) from Start Menu")
    print("- Run the commands to create user and database")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")